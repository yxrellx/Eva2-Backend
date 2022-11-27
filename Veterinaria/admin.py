from django.contrib import admin
from Veterinaria.models import Animal

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especie', 'sexo', 'raza', 'edad', 'ciudad']

# Register your models here.
admin.site.register(Animal,AnimalAdmin)