from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # URLs para Cliente
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/detalle/<int:id>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    
    # URLs para Habitacion
    path('habitaciones/', views.listar_habitaciones, name='listar_habitaciones'),
    path('habitaciones/crear/', views.crear_habitacion, name='crear_habitacion'),
    path('habitaciones/editar/<int:id>/', views.editar_habitacion, name='editar_habitacion'),
    path('habitaciones/detalle/<int:id>/', views.detalle_habitacion, name='detalle_habitacion'),
    path('habitaciones/eliminar/<int:id>/', views.eliminar_habitacion, name='eliminar_habitacion'),
    
    # URLs para Reserva
    path('reservas/', views.listar_reservas, name='listar_reservas'),
    path('reservas/crear/', views.crear_reserva, name='crear_reserva'),
    path('reservas/editar/<int:id>/', views.editar_reserva, name='editar_reserva'),
    path('reservas/detalle/<int:id>/', views.detalle_reserva, name='detalle_reserva'),
    path('reservas/eliminar/<int:id>/', views.eliminar_reserva, name='eliminar_reserva'),
    
    # URLs para Pago
    path('pagos/', views.listar_pagos, name='listar_pagos'),
    path('pagos/crear/', views.crear_pago, name='crear_pago'),
    path('pagos/editar/<int:id>/', views.editar_pago, name='editar_pago'),
    path('pagos/detalle/<int:id>/', views.detalle_pago, name='detalle_pago'),
    path('pagos/eliminar/<int:id>/', views.eliminar_pago, name='eliminar_pago'),

    # URLs para Empleado
    path('empleados/', views.listar_empleados, name='listar_empleados'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('empleados/editar/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('empleados/detalle/<int:id>/', views.detalle_empleado, name='detalle_empleado'),
    path('empleados/eliminar/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),
]
