from django.conf.urls import url

from . import views

# Solo necesitamos que la raiz cargue la funcion main del views
urlpatterns = [
    url(r'^$', views.main, name='main'),
]