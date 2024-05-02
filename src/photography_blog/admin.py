from django.contrib import admin
from photography_blog.models.session import Session
from photography_blog.models.picture import Picture
from photography_blog.models.picture_metadata import PictureMetadata

# Register your models here.

admin.site.register([Session, Picture, PictureMetadata])
