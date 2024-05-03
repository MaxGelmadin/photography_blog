from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from photography_blog.logic.sessions_logic import SessionsLogic


class SessionsView(APIView):
    """
    This is the class the represents the view of Sessionsn
    """

    def get(self, request):
        response_entity = SessionsLogic.get_sessions()
        response_entity = [entity.model_dump() for entity in response_entity]
        return Response(response_entity, HTTPStatus.OK)

    def delete(self, request):
        SessionsLogic.delete_sessions()
        return Response(status=HTTPStatus.OK)
