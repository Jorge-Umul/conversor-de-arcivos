from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
#import funciones.convertidores.main as main

# cambio de dormato a PDF
def index(request):
    #return HttpResponse ("hola")
    return render(request,'index.html' )

def jpg_a_pdf(request):
    return render(request, 'jpg_a_pdf.html')

def png_a_pdf(request):
    return render(request, 'a_pdf/png_a_pdf.html')

def Gif_a_pdf(request):
    return render(request, 'a_pdf/Gif_a_pdf.html')

def txt_a_pdf(request):
    return render(request, 'a_pdf/txt_a_pdf.html')

def jpeg_a_pdf(request):
    return render(request, 'a_pdf/jpeg_a_pdf.html')

def tiff_a_pdf(request):
    return render(request, 'a_pdf/tiff_a_pdf.html')