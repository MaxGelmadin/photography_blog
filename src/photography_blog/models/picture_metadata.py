"""
Picture Metadata Module
"""

import uuid

from django.db import models


class Lenses(models.TextChoices):
    """
    This is a class that represents the choices of different lenses.
    """

    SIGMA_16_28 = "SIGMA_16_28", "Sigma 16-28mm f/2.8"
    TAMRON_28_75 = "TAMRON_28_75", "Tamron 28-75 f/2.8"
    TAMRON_70_180 = "TAMRON_70_180", "Tamron 70-180 f/2.8 G2"
    SONY_200_600 = "SONY_200_600", "Sony 200-600 f/5.6-6.3 G OSS"


class PictureMetadata(models.Model):
    """
    This is a class that represents the Picture Metadata model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    iso = models.IntegerField()
    shutter_speed = models.FloatField()
    aperture = models.FloatField()
    lens_type = models.CharField(choices=Lenses.choices)
    width = models.FloatField()
    height = models.FloatField()
    focal_length = models.FloatField()
