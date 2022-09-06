from django.urls import path

from . import views

app_name="encuesta"

urlpatterns = [
    path('',views.calculadora,name='calculadora'),
    path('resultado/',views.result,name='resultado'),
    path('volumen/',views.calcularVolumen, name='volumen'),
    path('resultVol/',views.resultVolumen,name='resultVol'),
]