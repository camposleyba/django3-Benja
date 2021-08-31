from django.shortcuts import render, redirect
from .models import Foto, Video
import datetime

def home(request):
    if request.method == "GET":
        fecha = datetime.date(2021,7,15)
        fotos = Foto.objects.filter(week="semana 5")
        videos = Video.objects.filter(week="semana 5")
        return render(request, 'benja/home.html', {'fotos':fotos, 'fecha':fecha, 'videos':videos})
    else:
        return redirect('semana6')

def semana6(request):
    if request.method == "GET":
        fecha = datetime.date(2021,7,22)
        fotos = Foto.objects.filter(week="semana 6")
        videos = Video.objects.filter(week="semana 6")
        return render(request, 'benja/6semanas.html', {'fotos':fotos, 'fecha':fecha, 'videos':videos})

def semana8(request):
    if request.method == "GET":
        fecha = datetime.date(2021,8,3)
        fotos = Foto.objects.filter(week="semana 8")
        videos = Video.objects.filter(week="semana 8")
        return render(request, 'benja/8semanas.html', {'fotos':fotos, 'fecha':fecha, 'videos':videos})


def semana12(request):
    if request.method == "GET":
        fecha = datetime.date(2021,8,31)
        fotos = Foto.objects.filter(week="semana 12")
        videos = Video.objects.filter(week="semana 12")
        return render(request, 'benja/12semanas.html', {'fotos':fotos, 'fecha':fecha, 'videos':videos})

def semana16(request):
    if request.method == "GET":
        fecha = datetime.date(2021,8,31)
        fotos = Foto.objects.filter(week="semana 16")
        videos = Video.objects.filter(week="semana 16")
        return render(request, 'benja/16semanas.html', {'fotos':fotos, 'fecha':fecha, 'videos':videos})
