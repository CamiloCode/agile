from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.forms import ModelForm
from settings import MEDIA_URL
from photos.models import *

def main(request):
    """Main listing."""
    images = Image.objects.all()
    return render_to_response("list.html", dict(images=images, user=request.user))