"""aprendindoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
import convertidor_pdf.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', convertidor_pdf.views.index, name= 'index'),
    
    #url para los cambios a pdf
    path('jpg_a_pdf/', convertidor_pdf.views.jpg_a_pdf, name='jpg_a_pdf'),
    path('png_a_pdf/', convertidor_pdf.views.png_a_pdf, name='png_a_pdf'),
    path('Gif_a_pdf/', convertidor_pdf.views.Gif_a_pdf, name='Gif_a_pdf'),
    path('txt_a_pdf/', convertidor_pdf.views.txt_a_pdf, name='txt_a_pdf'),
    path('jpeg_a_pdf/', convertidor_pdf.views.jpeg_a_pdf, name='jpeg_a_pdf'),
    path('tiff_a_pdf/', convertidor_pdf.views.tiff_a_pdf, name='tiff_a_pdf')

]
