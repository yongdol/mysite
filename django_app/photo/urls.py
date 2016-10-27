from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.album_list, name='album_list'),
    url(r'^album/add/$', views.album_add, name='album_add'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.album_detail, name='album_detail'),
]
