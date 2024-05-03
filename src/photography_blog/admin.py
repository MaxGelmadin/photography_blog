from django.contrib import admin

from photography_blog.models.picture import Picture
from photography_blog.models.picture_metadata import PictureMetadata
from photography_blog.models.session import Session

# Register your models here.

admin.site.register([Session, Picture, PictureMetadata])
