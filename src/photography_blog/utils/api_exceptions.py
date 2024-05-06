from http import HTTPStatus


class PhotographyBlogGeneralError(Exception):
    """
    General API Error
    """

    def __init__(self, message: str, error_code: HTTPStatus, *args, **kwargs):
        self.message = message
        self.error_code = error_code
        self.args = args
        self.kwargs = kwargs
        super().__init__(self.message, self.error_code, self.args, self.kwargs)


class NotFoundErrorApi(PhotographyBlogGeneralError):
    """
    Model not found Error
    """
