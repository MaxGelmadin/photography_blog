from typing import List

from django.db.models import QuerySet

from photography_blog.business_logic.session_business_logic import SessionBusinssLogic
from photography_blog.entities.session_entity import SessionEntity
from photography_blog.models.session import Session


class SessionsLogic:
    """
    Session Logic Class
    """

    @staticmethod
    def get_sessions() -> List[SessionEntity]:
        """
        Returns all Sessions as a list
        """
        logic = SessionBusinssLogic()
        sessions: QuerySet[Session] = logic.get_all()
        response_entity: List[SessionEntity] = [
            SessionEntity(
                id=session.id,
                name=session.name,
                date=session.date,
                location=session.location,
            )
            for session in sessions
        ]
        return response_entity

    @staticmethod
    def delete_sessions() -> None:
        """
        Deletes all Sessions
        """
        logic = SessionBusinssLogic()
        logic.delete_all()
