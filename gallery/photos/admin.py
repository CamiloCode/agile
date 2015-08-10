from string import join

import os
from PIL import Image as PImage
from settings import MEDIA_ROOT
from photos.models import models
from django.contrib import admin

class ImageAdmin(admin.ModelAdmin):
    # search_fields = ["title"]
    list_display = ["titulo", "usuario", "descripcion", "imagen"]
    list_filter = ["usuario"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()