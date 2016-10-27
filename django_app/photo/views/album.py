from django.shortcuts import render, redirect, get_object_or_404
from ..models import Album
from ..forms import AlbumForm
from django.contrib.auth.decorators import login_required



__all__ = [
    'album_list',
    'album_add',
]


def album_list(request):
    albums = Album.objects.all()
    context = {
        'albums': albums,
    }
    return render(request, 'photo/album_list.html', context)

