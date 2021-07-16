from django.shortcuts import render
from .models import Foto, Video
import datetime

def home(request):
    fecha = datetime.date(2021,7,15)
    fotos = Foto.objects.filter(week="semana 5")
    videos = Video.objects.filter(week="semana 5")
    return render(request, 'benja/home.html', {'fotos':fotos, 'fecha':fecha, 'videos':videos})

def semana6(request):
    fecha = datetime.date(2021,7,22)
    fotos = Foto.objects.filter(week="semana 6")
    videos = Video.objects.filter(week="semana 6")
    return render(request, 'benja/6semanas.html', {'fotos':fotos, 'fecha':fecha, 'videos':videos})
