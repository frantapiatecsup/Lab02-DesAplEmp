from django.shortcuts import render

def vista(request):
    context ={
        'titulo' : "Calculadora Simple",
    }
    return render(request, 'seramio/primer.html', context)


def pops(request):
    context ={
        'titulo' : "Calculadora Cilindro",
    }
    return render(request, 'seramio/segundo.html', context)


def ejer1(request):
    context = {
        'titulo': 'Calculadora simple',
        'n1' : request.POST[ 'n1'],
        'n2': request.POST[ 'n2'],
        'operaciones': request.POST[ 'operaciones'],
        'resultado':request.POST['resultado'],
    }
    return render(request, 'seramio/rpta1.html', context)

def ejer2(request):
    context = {
        'titulo': 'Calculo de volumen de un cilindro',
        'n1' : request.POST[ 'n1'],
        'n2' : request.POST[ 'n2'],
        'radio' : 3.14,
        'resultado':request.POST['resultado'],
    }
    return render(request, 'seramio/rpta2.html', context)
