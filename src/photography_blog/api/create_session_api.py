from http import HTTPStatus

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from photography_blog.api.entitites.session_entities import CreateSessionRequestEntity
from photography_blog.logic.session_logic import SessionLogic


class CreateSessionView(APIView):
    """
    Create Session API
    """

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "date": openapi.Schema(type=openapi.TYPE_STRING),
                "location": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=["name", "date", "location"],
        )
    )
    def post(self, request):
        """
        Create a new session API
        """
        request_entity = CreateSessionRequestEntity(**request.data)
        response_entity = SessionLogic.create_session(request_entity=request_entity)
        return Response(response_entity.model_dump(), HTTPStatus.OK)
