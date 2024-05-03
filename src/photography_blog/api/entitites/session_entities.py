import datetime
import uuid

from pydantic import BaseModel, Field


class SessionRequestEntity(BaseModel):
    """
    Entity for GetSession
    """

    id: uuid.UUID


class CreateSessionRequestEntity(BaseModel):
    """
    Entity for the CreateSession
    """

    name: str = Field(max_length=32)
    date: datetime.date
    location: str = Field(max_length=32)
