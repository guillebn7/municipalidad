from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from . models import Publicacion

def lista_publicaciones(request):
	publicaciones = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
	return render(request, 'blog/lista_publicaciones.html', {'publicaciones':publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_publicacion.html', {'publicacion': publicacion})	

def admin_publicacion(request):
	adm_publicacion = Publicacion.objects.filter(autor=1)
	return render(request, 'blog/admin_publicacion.html', {'adm_publicacion': adm_publicacion})
