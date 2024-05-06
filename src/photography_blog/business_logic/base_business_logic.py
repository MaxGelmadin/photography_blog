import uuid
from abc import ABC
from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import QuerySet
from pydantic import BaseModel

from photography_blog.utils.app_exceptions import ModelNotFoundError


class BaseBusinessLogic(ABC):
    """
    This is the base class of a business logic.
    """

    def __init__(self, model_entity: models.Model) -> None:
        self._model_entity = model_entity

    @property
    def model_entity(self) -> models.Model:
        return self._model_entity

    def create(self, entity: BaseModel) -> model_entity:
        """
        Creates a model in the DB, derived from the entity.
        """
        created = self._model_entity.objects.create(**entity.model_dump())
        return created

    def get_all(self) -> QuerySet[model_entity]:
        """
        Returns a QuerySet of all the models in the DB.
        """
        return self._model_entity.objects.all()

    def delete_all(self) -> None:
        """
        Deletes all models from the DB.
        """
        self._model_entity.objects.all().delete()

    def get_by_id(self, id: uuid.UUID) -> Optional[model_entity]:
        """
        Gets a model by its ID.
        """
        try:
            return self._model_entity.objects.get(id=id)
        except ObjectDoesNotExist:
            raise ModelNotFoundError(missing_id=id)

    def delete_by_id(self, id: uuid.UUID) -> None:
        """
        Deletes a model by its ID.
        """
        self._model_entity.objects.filter(id=id).delete()
