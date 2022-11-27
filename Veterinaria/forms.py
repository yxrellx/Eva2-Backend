from django import forms
from Veterinaria.models import Animal
from django.forms import ValidationError

class FormAnimal(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
    nombre = forms.CharField(min_length=3, max_length=20)
    especie = forms.CharField(max_length=20)
    sexo = forms.CharField()
    raza = forms.CharField(min_length=3, max_length=20)
    edad = forms.CharField(min_length=2, max_length=50)
    ciudad = forms.CharField(min_length=3, max_length=20)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Animal.objects.filter(nombre=nombre).exists()

        if existe:
            raise ValidationError("ESte nombre ya existe")
        return nombre