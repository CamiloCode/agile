from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from photos.models import *

# Este unicamente debe llamar el template list.html y pasarle la informacion de las imagenes y el usuario que queremos mostrar (osea todas)
def main(request):
    images = Image.objects.all()
    return render_to_response("list.html", dict(imagenes=images, user=request.user))