from django import forms

from bus.models import Bus
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'cid', 'driver_licence', 'bus']
        widgets = {
            'bus': forms.Select(attrs={'class': 'form-select'}),
        }


class EmployeeEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'cid', 'driver_licence', 'bus']
        widgets = {
            'bus': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bus'].queryset = Bus.objects.all()
