from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from photography_blog.api.entitites.session_entities import SessionRequestEntity
from photography_blog.logic.session_logic import SessionLogic


class SessionView(APIView):
    """
    This is the class the represents the view of a single Session.
    """

    def get(self, request, id):
        """
        Get Session with id API
        """
        request_entity = SessionRequestEntity(id=id)
        response_entity = SessionLogic.get_session(request_entity=request_entity)

        return Response(response_entity.model_dump(), HTTPStatus.OK)

    def delete(self, request, id):
        """
        Delete session API
        """
        request_entity = SessionRequestEntity(id=id)
        SessionLogic.delete_session(request_entity=request_entity)

        return Response(status=HTTPStatus.OK)
