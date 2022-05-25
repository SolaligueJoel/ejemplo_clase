from aplications.coder_app.models import Curso, Profesor
from aplications.coder_app.forms import CursoFormulario, ProfesorFormulario
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader




def inicio(request):
    return render(request, 'app_coder/index.html')

def cursos(request):
    return render(request, 'app_coder/cursos.html')

def profesores(request):
    return render(request, 'app_coder/profesores.html')

def estudiantes(request):
    return render(request, 'app_coder/estudiantes.html')

def entregables(request):
    return render(request, 'app_coder/entregables.html')

def curso_formulario(request):
    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, 'app_coder/index.html')
        
    else:
        mi_formulario = CursoFormulario()
    
    return render(request, 'app_coder/curso_formulario.html',{'mi_formulario':mi_formulario})


def profesor_formulario(request):
    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],
                             email=informacion['email'], profesion=informacion['profesion'])
            profesor.save()
            return render(request, 'app_coder/index.html')
        
    else:
        mi_formulario = ProfesorFormulario()
        return render(request, 'app_coder/profesor_formulario.html',{'mi_formulario':mi_formulario})
    

def consulta_db(request):
    query_set = Curso.objects.all()    

    return render(request, 'app_coder/ejemplo.html', {'datos':query_set})


def busqueda_camada(request):
    return render(request, 'app_coder/busqueda_camada.html')

def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        curso_nuevo = Curso.objects.filter(camada = camada)
        return render(request, 'app_coder/buscar.html',{'cursos':curso_nuevo, 'camada':camada})
    else:
        respuesta = 'Datos invalidos'
    return HttpResponse(respuesta)

def ejemplo(request):
    pass
