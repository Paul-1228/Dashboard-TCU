from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'DW/index.html')

#def TCU(request):
   # return HttpResponse('')

def sesiones(request):
    return render(request, 'DW/sesiones.html')

def apoyo(request):
    return render(request, 'DW/apoyo.html')
