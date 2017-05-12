from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Music home page</h1>")

def detail(request, album_id):
    return HttpResponse("<h2>Album Detail: " +album_id+"</h2>")