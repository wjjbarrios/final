from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import GradoForm
from examenF.models import Grado, Seccion, Materia


def lista_grado(request):
    grado = Grado.objects.all()
    return render(request, 'productos/listagrado.html', {'grado': grado})

def detalle_grado(request, pk):
     grado = get_object_or_404(Grado,pk=pk)
     seccion = Seccion.objects.all()
     materia = Materia.objects.all()
     return render(request,"productos/detalle_grado.html",{'grado':grado,'seccion':seccion,'materia':materia})

def Eliminar_grado(request, pk):
    grado = get_object_or_404(Grado, pk=pk)
    producto.delete()
    return redirect('lista_grado')

def grado_nuevo(request):
    if request.method == 'POST':
        formulario = GradoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_grado')
            messages.add_message(request, messages.SUCCESS, 'grado Guardada Exitosamente')
    else:
        formulario = GradoForm()
    return render(request, 'productos/grado_editar.html', {'formulario': formulario})

def Editar_grado(request, pk):
    grado = get_object_or_404(Grado, pk=pk)
    if request.method == 'POST':
        formulario = GradoForm(request.POST, request.FILES, instance=grado)
        if formulario.is_valid():
            grado = formulario.save()
            grado.save()
            return redirect('detalle_grado', pk=grado.pk)

    else:
        formulario = GradoForm(instance=grado)
    return render(request, 'productos/grado_editar.html', {'formulario': formulario})
