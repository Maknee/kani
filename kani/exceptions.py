class KaniException(Exception):
    """Base class for all Kani exceptions/errors."""


# ==== HTTP ====
class HTTPException(KaniException):
    """Base class for all HTTP errors (for HTTP engines)."""


class HTTPTimeout(HTTPException):
    """Timeout occurred connecting to or waiting for a response from an HTTP request."""


class HTTPStatusException(HTTPException):
    """The HTTP server returned a non-200 status code."""

    def __init__(self, status_code: int, msg: str):
        super().__init__(msg)
        self.status_code = status_code


# ==== function calling ====
class FunctionCallException(KaniException):
    """Base class for exceptions that occur when a model calls an @ai_function."""

    def __init__(self, retry: bool):
        self.retry = retry


class WrappedCallException(FunctionCallException):
    """The @ai_function raised an exception."""

    def __init__(self, retry, original):
        super().__init__(retry)
        self.original = original

    def __str__(self):
        return str(self.original)


class NoSuchFunction(FunctionCallException):
    """The model attempted to call a function that does not exist."""

    def __init__(self, name):
        super().__init__(True)
        self.name = name


# ==== programmer errors ====
class FunctionSpecError(KaniException):
    """This @ai_function spec is invalid."""


class MissingModelDependencies(KaniException):
    """You are trying to use an engine but do not have engine-specific packages installed."""
