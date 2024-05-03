from photography_blog.api.entitites.session_entities import (
    CreateSessionRequestEntity,
    SessionRequestEntity,
)
from photography_blog.business_logic.session_business_logic import SessionBusinssLogic
from photography_blog.entities.session_entity import SessionEntity


class SessionLogic:
    """
    Session Logic Class
    """

    @staticmethod
    def create_session(request_entity: CreateSessionRequestEntity) -> SessionEntity:
        """
        Create a new Session
        """
        logic = SessionBusinssLogic()
        created = logic.create(request_entity)
        response_entity = SessionEntity(
            id=created.id,
            name=created.name,
            date=created.date,
            location=created.location,
        )

        return response_entity

    @staticmethod
    def delete_session(request_entity: SessionRequestEntity):
        """
        Delete a session
        """
        logic = SessionBusinssLogic()
        logic.delete_by_id(id=request_entity.id)

    @staticmethod
    def get_session(request_entity: SessionRequestEntity) -> SessionEntity:
        """
        Get a session
        """
        logic = SessionBusinssLogic()
        session = logic.get_by_id(id=request_entity.id)
        response_entity = SessionEntity(
            id=session.id,
            name=session.name,
            date=session.date,
            location=session.location,
        )

        return response_entity
