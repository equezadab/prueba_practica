from django.contrib import admin
from .models import Pokemon, Region, Tipo, RegionPokemon, TipoPokemon

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Region)
admin.site.register(Tipo)
admin.site.register(RegionPokemon)
admin.site.register(TipoPokemon)
