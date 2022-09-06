from django.shortcuts import render

# Create your views here.

def calculadora(request):
    return render(request, 'calculadora/calculadora.html')

def result(request):
    operation = request.POST['operation']
    num1 = request.POST['numberone']
    num2 = request.POST['numbertwo']
    res = 0
    # a = int(num1)
    # b = int(num2)
    # res = a+b
    # return render(request, 'calculadora/resultado.html',{'result':operation})
    if operation == 'suma':
        a = int(num1)
        b = int(num2)
        res = a+b
        return render(request, 'calculadora/resultado.html',{'result':res})
    elif operation == 'resta':
        a = int(num1)
        b = int(num2)
        res = a-b
        return render(request, 'calculadora/resultado.html',{'result':res})
    elif operation == 'multi':
        a = int(num1)
        b = int(num2)
        res = a*b
        return render(request, 'calculadora/resultado.html',{'result':res})

def calcularVolumen(request):
    return render(request, 'calculadora/volumen.html')

def resultVolumen(request):
    diam = request.POST['diametro']
    alt = request.POST['altura']

    a = int(diam)
    b = int(alt)

    res = a * b
    print(res)
    context = {
        'volresult' : res
    }
    return render(request, 'calculadora/volresult.html', context)
