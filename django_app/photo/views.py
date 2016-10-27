from django.shortcuts import render
from .models import Album


def album_list(request):
    albums = Album.objects.all()
    context = {
        'album_list': albums,
    }
    return render(request, 'photo/album_list.html', context)