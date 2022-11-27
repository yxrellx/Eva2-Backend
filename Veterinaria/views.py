from django.shortcuts import render,redirect
from Veterinaria.models import Animal
from Veterinaria.forms import FormAnimal

# Create your views here.

def index(request):
    return render(request, 'Veterinaria/index.html')

def animalData(request):
    animales = Animal.objects.all()
    #animales = Animal.objects.all().filter(nombre="martina", especie="gato")
    #animales = Animal.objects.all().filter(nombre="Miguel")
    #animales = Animal.objects.all().order_by('-nombre')
    #animales = Animal.objects.all().order_by('nombre')
    data = {'animales' : animales}
    return render(request, 'Veterinaria/animales.html', data)

def Registro(request):
    form = FormAnimal()
    if request.method == 'POST' :
        form = FormAnimal(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Veterinaria/Registro.html', data)

def eliminar(request, id):
    animales = Animal.objects.get(id = id)
    animales.delete()
    return redirect('/animales')

def actualizar(request, id):
    animales = Animal.objects.get(id = id)
    form = FormAnimal(instance=animales)
    if request.method =='POST' :
        form = FormAnimal(request.POST, instance=animales)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'Veterinaria/actualizar.html', data)