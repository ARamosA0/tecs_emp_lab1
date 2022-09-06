from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def suma(request, num1, num2):
    result = num1+num2
    return HttpResponse("La suma de %s + %d es: %a" %(num1,num2,result))

def resta(request, num1, num2):
    result = num1-num2
    return HttpResponse("La resta de %s - %d es: %a" %(num1,num2,result))

def multi(request, num1, num2):
    result = num1*num2
    return HttpResponse("El producto entre %s * %d es: %a" %(num1,num2,result))

def divi(request, num1, num2):
    if num1==0:
        result = 'No se puede entre 0'
    
    result = num1/num2


    return HttpResponse("La division de %s / %d es: %a" %(num1,num2,result))
