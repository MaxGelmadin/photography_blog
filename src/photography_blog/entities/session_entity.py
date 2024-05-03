"""
Session Entity Module
"""

import datetime
import uuid

from pydantic import BaseModel, Field


class SessionEntity(BaseModel):
    """
    Pydantic model for a Session.
    """

    id: uuid.UUID
    name: str = Field(max_length=32)
    date: datetime.datetime
    location: str = Field(max_length=32)
