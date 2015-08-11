from string import join

import os
from settings import MEDIA_ROOT
from photos.models import models
from django.contrib import admin

# Esto nos permite manipular el listado a mostrar para los admins
class ImageAdmin(admin.ModelAdmin):
    list_display = ["titulo", "usuario", "descripcion", "imagen"]
    list_filter = ["usuario"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()