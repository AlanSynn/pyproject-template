class BaseException(Exception):
    """Base exception class that other exception classes can inherit from."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
