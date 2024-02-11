from functools import wraps


def decorate_api_call(f):
    @wraps(f)
    def call_wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return call_wrapper


class AnyApiWrapperMixin:
    ...

    def __getattribute__(self, name):
        result = super(AnyApiWrapperMixin, self).__getattribute__(name)

        if name.startswith("_") or name in {
            "api_client",
        }:
            return result

        return decorate_api_call(result)
