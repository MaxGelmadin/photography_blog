from django.db import models


class Session(models.Model):
    """
    This is the model class of Session.
    """

    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=32)
    date = models.DateField()
    location = models.CharField(max_length=32)
