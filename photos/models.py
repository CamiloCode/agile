from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# El modelo de una imagen tiene:
# El titulo representado como un CharField
# La imagen que tambien es un CharField puesto que unicamente es una URL
# Una descripcion que es un TextField para almacenar mas caracteres
# Un usuario que es el owner de la imagen y aqui se representa como un ForeignKey
class Image(models.Model):
    titulo = models.CharField(max_length=60, blank=True, null=True)
    imagen = models.CharField(max_length=5000, default="")
    descripcion = models.TextField(default="")
    usuario = models.ForeignKey(User, null=True, blank=True)

# Una clase de administrador de imagenes
class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["titulo", "usuario", "imagen", "descripcion"]

# Se registran las dos clases con el admin
admin.site.register(Image, ImageAdmin)