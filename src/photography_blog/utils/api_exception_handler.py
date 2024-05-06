from http import HTTPStatus

from rest_framework.response import Response

from photography_blog.utils.api_exceptions import PhotographyBlogGeneralError


def custom_exception_handler(exc, context):
    """
    Custom exception handler for Photography Blog app.
    """
    if not isinstance(exc, PhotographyBlogGeneralError):
        response_data = {"message": "An unexpected error occurred. Please try again."}
        return Response(response_data, status=HTTPStatus.INTERNAL_SERVER_ERROR)
    else:
        response = {
            "message": exc.message,
            "args": exc.args,
            "kwargs": exc.kwargs,
        }
        return Response(response, exc.error_code)
