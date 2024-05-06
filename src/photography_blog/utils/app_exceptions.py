from typing import Optional


class DatabaseError(Exception):
    """
    Common exception for database accesses
    """

    def __init__(self, message: Optional[str] = None, *args, **kwargs):
        self.message = message
        self.args = args
        self.kwargs = kwargs
        super().__init__(self.message, self.args, self.kwargs)


class ModelNotFoundError(DatabaseError):
    """
    Model not found error
    """
