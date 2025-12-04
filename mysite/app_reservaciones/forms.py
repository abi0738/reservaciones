from django import forms
from .models import Cliente, Habitacion, Reserva, Pago, Empleado

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email', 'direccion']

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['numero', 'tipo', 'precio_noche', 'estado']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'habitacion', 'id_empleado', 'fecha_entrada', 'fecha_salida']
        widgets = {
            'fecha_entrada': forms.DateInput(attrs={'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
        }

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['reserva', 'monto', 'fecha_pago', 'metodo_pago']
        widgets = {
            'fecha_pago': forms.DateInput(attrs={'type': 'date'}),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'puesto', 'salario', 'fecha_contratacion', 'email']
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
        }