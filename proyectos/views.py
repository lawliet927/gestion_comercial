from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Edificacion, Tienda, Propietario, FechaEntrega
from .forms import EdificacionForm, TiendaForm, PropietarioForm, FechaEntregaForm

# Vista para la página de inicio
def home(request):
    return render(request, 'home.html')

# Edificaciones
def lista_edificaciones(request):
    edificaciones = Edificacion.objects.all()
    return render(request, 'edificacion_lista.html', {'edificaciones': edificaciones})

def agregar_edificacion(request):
    if request.method == 'POST':
        form = EdificacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Edificación agregada con éxito.")
            return redirect('lista_edificaciones')
    else:
        form = EdificacionForm()
    return render(request, 'edificacion_form.html', {'form': form})

def detalles_edificacion(request, id):
    edificacion = get_object_or_404(Edificacion, id=id)
    return render(request, 'edificacion_detalle.html', {'edificacion': edificacion})

def editar_edificacion(request, id):
    edificacion = get_object_or_404(Edificacion, id=id)
    if request.method == 'POST':
        form = EdificacionForm(request.POST, instance=edificacion)
        if form.is_valid():
            form.save()
            messages.success(request, "Edificación actualizada con éxito.")
            return redirect('lista_edificaciones')
    else:
        form = EdificacionForm(instance=edificacion)
    return render(request, 'edificacion_form.html', {'form': form})

def eliminar_edificacion(request, id):
    edificacion = get_object_or_404(Edificacion, id=id)
    if request.method == 'POST':
        edificacion.delete()
        messages.success(request, "Edificación eliminada con éxito.")
        return redirect('lista_edificaciones')
    return render(request, 'edificacion_confirmar_eliminar.html', {'edificacion': edificacion})


# Tiendas
def agregar_tienda(request):
    if request.method == 'POST':
        form = TiendaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tienda agregada exitosamente.')
            return redirect('lista_tiendas')
    else:
        form = TiendaForm()
    return render(request, 'agregar_tienda.html', {'form': form})

def editar_tienda(request, tienda_id):
    tienda = get_object_or_404(Tienda, id=tienda_id)
    if request.method == 'POST':
        form = TiendaForm(request.POST, instance=tienda)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tienda editada exitosamente.')
            return redirect('lista_tiendas')
    else:
        form = TiendaForm(instance=tienda)
    return render(request, 'editar_tienda.html', {'form': form})

def eliminar_tienda(request, tienda_id):
    tienda = get_object_or_404(Tienda, id=tienda_id)
    if request.method == 'POST':
        tienda.delete()
        messages.success(request, 'Tienda eliminada exitosamente.')
        return redirect('lista_tiendas')
    return render(request, 'eliminar_tienda.html', {'tienda': tienda})

def lista_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'lista_tiendas.html', {'tiendas': tiendas})


# Propietarios
def lista_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'lista_propietarios.html', {'propietarios': propietarios})

def agregar_propietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Propietario agregado exitosamente.")
            return redirect('lista_propietarios')
    else:
        form = PropietarioForm()
    return render(request, 'agregar_propietario.html', {'form': form})

def editar_propietario(request, propietario_id):
    propietario = get_object_or_404(Propietario, id=propietario_id)
    if request.method == 'POST':
        form = PropietarioForm(request.POST, request.FILES, instance=propietario)
        if form.is_valid():
            form.save()
            messages.success(request, "Propietario editado exitosamente.")
            return redirect('lista_propietarios')
    else:
        form = PropietarioForm(instance=propietario)
    return render(request, 'editar_propietario.html', {'form': form})

def eliminar_propietario(request, propietario_id):
    propietario = get_object_or_404(Propietario, id=propietario_id)
    propietario.delete()
    messages.success(request, "Propietario eliminado exitosamente.")
    return redirect('lista_propietarios')


# Fechas de Entrega
def lista_fechas_entrega(request):
    fechas = FechaEntrega.objects.all()
    return render(request, 'lista_fechas.html', {'fechas': fechas})

def agregar_fecha_entrega(request):
    if request.method == 'POST':
        form = FechaEntregaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Fecha de entrega agregada exitosamente.")
            return redirect('lista_fechas_entrega')
    else:
        form = FechaEntregaForm()
    return render(request, 'agregar_fecha.html', {'form': form})

def editar_fecha_entrega(request, fecha_id):
    fecha_entrega = get_object_or_404(FechaEntrega, id=fecha_id)
    if request.method == 'POST':
        form = FechaEntregaForm(request.POST, instance=fecha_entrega)
        if form.is_valid():
            form.save()
            messages.success(request, "Fecha de entrega editada exitosamente.")
            return redirect('lista_fechas_entrega')
    else:
        form = FechaEntregaForm(instance=fecha_entrega)
    return render(request, 'agregar_fecha.html', {'form': form})

def eliminar_fecha_entrega(request, fecha_id):
    fecha_entrega = get_object_or_404(FechaEntrega, id=fecha_id)
    if request.method == 'POST':
        fecha_entrega.delete()
        messages.success(request, "Fecha de entrega eliminada exitosamente.")
        return redirect('lista_fechas_entrega')
    return render(request, 'eliminar_fecha.html', {'fecha_entrega': fecha_entrega})
