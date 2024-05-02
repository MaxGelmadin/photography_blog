from django.db import models
from photography_blog.models.session import Session
from photography_blog.models.picture_metadata import PictureMetadata


class Extensions(models.TextChoices):
    """
    Supported extensions of a picture.
    """

    JPG = "jpg", "jpg"
    JPEG = "jpeg", "jpeg"
    ARW = "arw", "arw"


class Picture(models.Model):
    """
    This is the model class of a Picture.
    """

    id = models.UUIDField(primary_key=True)
    session = models.ForeignKey(
        to=Session, on_delete=models.CASCADE, verbose_name="related session"
    )
    metadata = models.OneToOneField(to=PictureMetadata, on_delete=models.CASCADE)
    s3_url = models.CharField(unique=True, blank=False)
    extension = models.CharField(max_length=5, choices=Extensions.choices)
