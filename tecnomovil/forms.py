from django import forms
from .models import Carrito

class AñadirAlCarritoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = ['celular', 'cantidad']