from django.urls import path 

from . import views

urlpatterns = [
    path('<int:num1>/<int:num2>/suma/', views.suma, name='suma'),
    path('<int:num1>/<int:num2>/resta/', views.resta, name='resta'),
    path('<int:num1>/<int:num2>/multi/', views.multi, name='multi'),
    path('<int:num1>/<int:num2>/divi/', views.divi, name='divi'),
]