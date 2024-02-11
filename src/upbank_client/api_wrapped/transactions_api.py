import upbank_spec
from upbank_client.wrapper.AnyApiWrapperMixin import AnyApiWrapperMixin


class AsyncTransactionsApi(
    AnyApiWrapperMixin,
    upbank_spec.TransactionsApi,
):
    ...


if __name__ == "__main__":
    a = AsyncTransactionsApi()
    a.geta()
