from django.forms import ModelForm, Select, NumberInput
from .models import Entradas

class EntradaForm(ModelForm):
    class Meta:
        model = Entradas
        fields = ['produto', 'quantidade', 'preco']
        widgets = {
            'produto': Select(attrs={'class': 'select'}),
            'quantidade': NumberInput(attrs={'class': 'input'}),
            'preco': NumberInput(attrs={'class':'input'}),
        }
