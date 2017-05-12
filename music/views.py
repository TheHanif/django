from django.http import HttpResponse
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    html = ''

    for album in all_albums:
        url = '/music/'+str(album.id)
        html += '<a href="'+url+'">'+album.album_title+'</a><br>'

    return HttpResponse(html)

def detail(request, album_id):
    album = Album.objects.filter(id=album_id)

    html = ''
    html = album.id


    return HttpResponse(html)