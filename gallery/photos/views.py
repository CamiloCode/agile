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
    if not request.user.is_authenticated():
        images = Image.filter(public=True)

    paginator = Paginator(images, 10)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        images = paginator.page(page)
    except (InvalidPage, EmptyPage):
        images = paginator.page(paginator.num_pages)

    return render_to_response("list.html", dict(images=images, user=request.user))