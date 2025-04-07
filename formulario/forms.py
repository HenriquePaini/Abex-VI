from django import forms
from .models import DadosDiabetes

class DadosDiabetesForm(forms.ModelForm):
    class Meta:
        model = DadosDiabetes
        fields = [
            'gravidez', 'glicose', 'pressao', 'espessura_pele',
            'insulina', 'imc', 'pedigree', 'idade', 'resultado'
        ]
