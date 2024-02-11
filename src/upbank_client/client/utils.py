import functools
from typing import TypeVar, Callable, Any, Generic, ParamSpec, Optional

from typing_extensions import Coroutine
from urllib.parse import urlparse, parse_qs

T_Retval = TypeVar("T_Retval")
T_ParamSpec = ParamSpec("T_ParamSpec")


def _extract_next_from_url(url: str) -> str:
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    return query["page[after]"][0]


class Paginator(Generic[T_Retval]):
    def __init__(
        self,
        func: Callable[T_ParamSpec, Coroutine[Any, Any, T_Retval]],
        *args: T_ParamSpec.args,
        **kwargs: T_ParamSpec.kwargs,
    ):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.next_from: Optional[str] = None

    def __aiter__(self):
        return self

    async def __anext__(self) -> T_Retval:
        response = await self.func(  # type: ignore[call-arg] # paginator only for methods with page
            *self.args, page_after=self.next_from, **self.kwargs  # type: ignore[arg-type]
        )
        next_link: Optional[str] = response.links.next  # type: ignore[attr-defined]

        if not next_link:
            raise StopAsyncIteration

        self.next_from = _extract_next_from_url(next_link)
        return response


# FIXME: types drops in some cases (pycharm?)
# The type definition eventually stop introspect when input is too complicated
# it works well with simple function like paginate(sleep)(unexpected_argument=3)


def paginate(func: Callable[T_ParamSpec, Coroutine[Any, Any, T_Retval]]) -> Callable[T_ParamSpec, Paginator[T_Retval]]:
    @functools.wraps(func)
    def wrapper(*args: T_ParamSpec.args, **kwargs: T_ParamSpec.kwargs) -> Paginator[T_Retval]:
        return Paginator(func, *args, **kwargs)

    return wrapper
