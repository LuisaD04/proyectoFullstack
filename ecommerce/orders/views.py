from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# from core.users.models import Profile, User
from django.views.generic import ListView
from django.urls import reverse_lazy
from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView)    # GenericAPIView
from .models import Voluntarios,Delegados,Proyectos,Categorias,Seguimiento,ZonasRecuperadas
from django.contrib import messages

from .serializers import VoluntarioSerializer, DelegadoSerializer, SeguimientoSerializer
# Create your views here.
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'object_list'
    paginate_by = 10 # usuarios por pagina
    queryset = User.objects.all() #consulta para obtener lista de usuarios
    ordering = ['username']

# @permission_classes((AllowAny, ))
class VoluntariosListApi(ListAPIView):
    serializer_class = VoluntarioSerializer
    queryset = Voluntarios.objects.all()

class SeguimientoListApi(ListAPIView):
    serializer_class = SeguimientoSerializer
    queryset = Delegados.objects.all()
 
class DelegadosListApi(ListAPIView):
    serializer_class = DelegadoSerializer
    queryset = Seguimiento.objects.all()

class VoluntariosCreateAPIView(CreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = VoluntarioSerializer


def home(request):
    voluntarioListado = Voluntarios.objects.all()
    # proyectosListado = Proyectos.objects.all()
    # messages.success(request, '¡Voluntarios listados!')
    return render(request, "user_list.html", {"voluntarios": voluntarioListado})

def registrarVoluntarios(request):
    cedulaVoluntario = request.POST['txtcedulaVoluntario']
    nombreVoluntario = request.POST['txtnombreVoluntario']
    apellidoVoluntario = request.POST['txtapellidoVoluntario']
    edadVoluntario = request.POST['txtedadVoluntario']
    correoVoluntario = request.POST['txtcorreoVoluntario']
    ciudadVoluntario = request.POST['txtciudadVoluntario']

    voluntarios = Voluntarios.objects.create(
        cedulaVoluntario=cedulaVoluntario, nombreVoluntario=nombreVoluntario, apellidoVoluntario=apellidoVoluntario,edadVoluntario=edadVoluntario, correoVoluntario=correoVoluntario, ciudadVoluntario=ciudadVoluntario)
    messages.success(request, '¡Voluntario registrado!')
    return redirect('/')


def edicionVoluntarios(request, cedulaVoluntario):
    voluntarios = Voluntarios.objects.get(cedulaVoluntario=cedulaVoluntario)
    return render(request, "edicionVoluntarios.html", {"voluntarios": voluntarios})


def editarVoluntarios(request):
    cedulaVoluntario = request.POST['txtcedulaVoluntario']
    nombreVoluntario = request.POST['txtnombreVoluntario']
    apellidoVoluntario = request.POST['txtapellidoVoluntario']
    edadVoluntario = request.POST['txtedadVoluntario']
    correoVoluntario = request.POST['txtcorreoVoluntario']
    ciudadVoluntario = request.POST['txtciudadVoluntario']

    voluntarios = Voluntarios.objects.get(cedulaVoluntario=cedulaVoluntario)
    voluntarios.nombreVoluntario = nombreVoluntario
    voluntarios.apellidoVoluntario = apellidoVoluntario
    voluntarios.edadVoluntario = edadVoluntario
    voluntarios.correoVoluntario = correoVoluntario
    voluntarios.ciudadVoluntario = ciudadVoluntario
    voluntarios.save()

    messages.success(request, '¡Voluntario actualizado!')

    return redirect('/')


def eliminarVoluntarios(request, cedulaVoluntario):
    voluntarios = Voluntarios.objects.get(cedulaVoluntario=cedulaVoluntario)
    voluntarios.delete()

    messages.success(request, '¡Voluntario eliminado!')

    return redirect('/')

def galeria(request):
    categoriasListado = Categorias.objects.all()
    # messages.success(request, '¡Voluntarios listados!')
    return render(request, "galeria.html", {"categorias": categoriasListado})

def portafolio(request):
    proyectosListado = Proyectos.objects.all()
    # messages.success(request, '¡Voluntarios listados!')
    return render(request, "portafolio.html", {"proyectos": proyectosListado})

# proyecto


def registrarProyectos(request):
    # idProyecto = request.POST['txtidProyecto']
    nombreProyecto = request.POST['txtnombreProyecto']
    descripcionProyecto = request.POST['txtdescripcionProyecto']

    proyectos = Proyectos.objects.create(
        # idProyecto=idProyecto, 
        nombreProyecto=nombreProyecto, descripcionProyecto=descripcionProyecto)
    messages.success(request, '¡Proyecto registrado!')
    return redirect('/portafolio/')


def edicionProyectos(request, idProyecto):
    proyectos = Proyectos.objects.get(idProyecto=idProyecto)
    return render(request, "edicionProyectos.html", {"proyectos": proyectos})


def editarProyectos(request):
    idProyecto = request.POST['txtidProyecto']
    nombreProyecto = request.POST['txtnombreProyecto']
    descripcionProyecto = request.POST['txtdescripcionProyecto']

    proyectos = Proyectos.objects.get(idProyecto=idProyecto)
    proyectos.nombreProyecto = nombreProyecto
    proyectos.descripcionProyecto = descripcionProyecto
    proyectos.save()

    messages.success(request, '¡Proyecto actualizado!')

    return redirect('/portafolio/')


def eliminarProyectos(request, idProyecto):
    proyectos = Proyectos.objects.get(idProyecto=idProyecto)
    proyectos.delete()

    messages.success(request, '¡Proyecto eliminado!')

    return redirect('/portafolio/')


# categorias



def registrarCategorias(request):
    # idCategoria = request.POST['txtidCategoria']
    nombreCategoria = request.POST['txtnombreCategoria']
    nombreContenido = request.POST['txtnombreContenido']
    descripciónContenido = request.POST['txtdescripcionContenido']
    imagenContenido = request.FILES['txtimagenContenido']

    try:
        imagenContenido = request.FILES['txtimagenContenido']
    except:
        imagenContenido = "images/IMG.jpg"

    categorias = Categorias.objects.create(
        # idCategoria=idCategoria, 
        nombreCategoria=nombreCategoria, nombreContenido=nombreContenido, descripciónContenido=descripciónContenido, imagenContenido=imagenContenido)
    messages.success(request, '¡Categoria registrada!')
    return redirect('/galeria/')


def edicionCategorias(request, idCategoria):
    categorias = Categorias.objects.get(idCategoria=idCategoria)
    return render(request, "edicionCategorias.html", {"categorias": categorias})


def editarCategorias(request):
    idCategoria = request.POST['txtidCategoria']
    nombreCategoria = request.POST['txtnombreCategoria']
    nombreContenido = request.POST['txtnombreContenido']
    descripciónContenido = request.POST['txtdescripcionContenido']
    # imagenContenido = request.FILES['txtimagenContenido']
    try:
        imagenContenido = request.FILES['txtimagenContenido']
        categorias = Categorias.objects.get(idCategoria=idCategoria)
        categorias.imagenContenido = imagenContenido
        categorias.save()
    except:
        imagenContenido = "images/IMG.jpg"
        
    categorias = Categorias.objects.get(idCategoria=idCategoria)
    categorias.nombreCategoria = nombreCategoria
    categorias.nombreContenido = nombreContenido
    categorias.descripciónContenido = descripciónContenido
    
    categorias.save()

    messages.success(request, '¡Categoria actualizada!')

    return redirect('/galeria/')


def eliminarCategorias(request, idCategoria):
    categorias = Categorias.objects.get(idCategoria=idCategoria)
    categorias.delete()

    messages.success(request, '¡Categoria eliminada!')

    return redirect('/galeria/')

