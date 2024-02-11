def decorate(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper


class AnyApiWrapperMixin:
    ...
    def __getattribute__(self, name):
        result = super(AnyApiWrapperMixin, self).__getattribute__(name)

        if name.startswith("_") or name in {
            "api_client",
        }:
            return result

        return decorate(result)
