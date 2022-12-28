from django.shortcuts import render
from .models import Anime

def index(request):
    context = {
        "animePosts": Anime.objects.all(),
    }
    print("luygfcghh")
    return render(request, 'blogapp/index.html', context)