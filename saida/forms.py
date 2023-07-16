from django.forms import ModelForm, TextInput, Select, NumberInput
from .models import Saidas

class SaidasForm(ModelForm):
    class Meta:
        model = Saidas
        fields = ['produto', 'quantidade']
        widgets = {
            'produto': Select(attrs={'class': 'select'}),
            'quantidade': NumberInput(attrs={'class': 'input'}),
        }







