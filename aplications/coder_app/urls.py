from django.urls import path
from aplications.coder_app.views import *

urlpatterns = [
    path('',inicio, name = 'Inicio'),
    path('profesores/',profesores, name = 'Profesores'),
    path('cursos/',cursos, name= 'Cursos'),
    path('estudiantes/',estudiantes, name = 'Estudiantes'),
    path('entregables/',entregables, name = 'Entregables'),
    path('curso_formulario/',curso_formulario, name = 'CursoFormulario'),
    path('profesor_formulario/',profesor_formulario, name = 'ProfesorFormulario'),
    path('ejemplo/',consulta_db, name = 'Consulta'),
    path('busqueda_camada/',busqueda_camada, name = 'BusquedaCamada'),
    path('buscar/',buscar, name = 'Buscar'),

]
