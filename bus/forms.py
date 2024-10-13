from django import forms

from route.models import Route
from .models import Bus


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['plate', 'number', 'capacity', 'route']
        widgets = {
            'route': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'plate': 'Chapa del bus',
            'number': 'Número del bus',
            'capacity': 'Capacidad',
            'route': 'Ruta',
        }
        help_texts = {
            'plate': 'Ejemplo: ABC123',
            'number': 'Ejemplo: BUS001',
            'capacity': 'Maxima capacidad de pasajeros',
            'route': 'Seleccione una ruta existente',
        }


class EditBusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['plate', 'number', 'capacity', 'route']
        widgets = {
            'route': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'plate': 'Chapa del bus',
            'number': 'Número del bus',
            'capacity': 'Capacidad',
            'route': 'Ruta',
        }
        help_texts = {
            'plate': 'Ejemplo: ABC123',
            'number': 'Ejemplo: BUS001',
            'capacity': 'Maxima capacidad de pasajeros',
            'route': 'Seleccione una ruta existente',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['route'].queryset = Route.objects.all()
