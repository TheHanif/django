from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums
    }

    return render(request, 'music/index.html', context)

def detail(request, album_id):
    album = Album.objects.filter(id=int(album_id))

    html = '<h1>Detail of '
    html += str(album[0].album_title)
    html += '</h1>'

    html += '<h2>Artist: ' + str(album[0].artist) + '</h2>'

    html += '<hr>'
    return HttpResponse(html)