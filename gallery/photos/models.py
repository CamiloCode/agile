from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Image(models.Model):
    titulo = models.CharField(max_length=60, blank=True, null=True)
    imagen = models.CharField(max_length=5000, default="")
    descripcion = models.TextField(default="")
    usuario = models.ForeignKey(User, null=True, blank=True)

class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["titulo", "usuario", "imagen", "descripcion"]

admin.site.register(Image, ImageAdmin)