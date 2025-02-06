import datetime
from django import forms
from .models import Edificacion, Tienda, Propietario, FechaEntrega

class EdificacionForm(forms.ModelForm):
    class Meta:
        model = Edificacion
        fields = ['nombre', 'direccion', 'descripcion']  # Campos que serán mostrados en el formulario
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Ajuste del campo de texto de descripción
        }


class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = '__all__'


class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'


class FechaEntregaForm(forms.ModelForm):
    class Meta:
        model = FechaEntrega
        fields = ['fecha', 'proyecto']  # Los campos que se incluirán en el formulario

        # Aquí puedes agregar configuraciones adicionales, como widgets, por ejemplo:
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),  # Para el campo fecha
            'proyecto': forms.Select(attrs={'class': 'form-control'}),  # Estilo de clase para el campo de proyecto
        }

    # Si deseas agregar validaciones personalizadas o métodos, puedes hacerlo aquí:
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha < datetime.date.today():
            raise forms.ValidationError("La fecha de entrega no puede ser anterior a la fecha actual.")
        return fecha
