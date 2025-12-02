from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Habitacion, Reserva, Pago, Empleado
from .forms import ClienteForm, HabitacionForm, ReservaForm, PagoForm, EmpleadoForm

def home(request):
    return render(request, 'index.html')

# Vistas para Cliente
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/crear_cliente.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(instance=cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    return render(request, 'clientes/editar_cliente.html', {'form': form, 'cliente': cliente})

def detalle_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'clientes/detalle_cliente.html', {'cliente': cliente})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return redirect('listar_clientes')

# Vistas para Habitacion
def listar_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'habitaciones/listar_habitaciones.html', {'habitaciones': habitaciones})

def crear_habitacion(request):
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_habitaciones')
    else:
        form = HabitacionForm()
    return render(request, 'habitaciones/crear_habitacion.html', {'form': form})

def editar_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id=id)
    form = HabitacionForm(instance=habitacion)
    if request.method == 'POST':
        form = HabitacionForm(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
            return redirect('listar_habitaciones')
    return render(request, 'habitaciones/editar_habitacion.html', {'form': form, 'habitacion': habitacion})

def detalle_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id=id)
    return render(request, 'habitaciones/detalle_habitacion.html', {'habitacion': habitacion})

def eliminar_habitacion(request, id):
    habitacion = get_object_or_404(Habitacion, id=id)
    if request.method == 'POST':
        habitacion.delete()
        return redirect('listar_habitaciones')
    return redirect('listar_habitaciones')

# Vistas para Reserva
def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/listar_reservas.html', {'reservas': reservas})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm()
    return render(request, 'reservas/crear_reserva.html', {'form': form})

def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    form = ReservaForm(instance=reserva)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    return render(request, 'reservas/editar_reserva.html', {'form': form, 'reserva': reserva})

def detalle_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    return render(request, 'reservas/detalle_reserva.html', {'reserva': reserva})

def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('listar_reservas')
    return redirect('listar_reservas')

# Vistas para Pago
def listar_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'pagos/listar_pagos.html', {'pagos': pagos})

def crear_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pagos')
    else:
        form = PagoForm()
    return render(request, 'pagos/crear_pago.html', {'form': form})

def editar_pago(request, id):
    pago = get_object_or_404(Pago, id=id)
    form = PagoForm(instance=pago)
    if request.method == 'POST':
        form = PagoForm(request.POST, instance=pago)
        if form.is_valid():
            form.save()
            return redirect('listar_pagos')
    return render(request, 'pagos/editar_pago.html', {'form': form, 'pago': pago})

def detalle_pago(request, id):
    pago = get_object_or_404(Pago, id=id)
    return render(request, 'pagos/detalle_pago.html', {'pago': pago})

def eliminar_pago(request, id):
    pago = get_object_or_404(Pago, id=id)
    if request.method == 'POST':
        pago.delete()
        return redirect('listar_pagos')
    return redirect('listar_pagos')

# Vistas para Empleado
def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/listar_empleados.html', {'empleados': empleados})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/crear_empleado.html', {'form': form})

def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    form = EmpleadoForm(instance=empleado)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    return render(request, 'empleados/editar_empleado.html', {'form': form, 'empleado': empleado})

def detalle_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    return render(request, 'empleados/detalle_empleado.html', {'empleado': empleado})

def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('listar_empleados')
    return redirect('listar_empleados')