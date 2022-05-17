from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from coder_app.models import Familiar

def mostrar_familiares(self):
    familiar1=Familiar(nombre="Pepe",apellido="Lopez",dni="1234567",fecha_nacimiento="1999-07-10",color_de_ojos="Marrones",altura="1.60",ocupacion="carpintero")
    familiar1.save()
    familiar2=Familiar(nombre="Juan",apellido="Perez",dni="9874563",fecha_nacimiento="1993-02-22",color_de_ojos="Verdes",altura="1.77",ocupacion="estudiante")
    familiar2.save()
    familiar3=Familiar(nombre="Roberto",apellido="Gomez",dni="96687741",fecha_nacimiento="1975-12-15",color_de_ojos="Celestes",altura="1.82",ocupacion="emprendedor")
    familiar3.save()
   
    familiares=Familiar.objects.all()
    diccionario={"hoy":datetime.now(),"familiares":familiares}
    
    plantilla=loader.get_template('template.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)