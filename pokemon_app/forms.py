from django import forms
from .models import Pokemon


class formularioPokemon(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
