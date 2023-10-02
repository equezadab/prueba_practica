from django.urls import path
from .views import ver_pokemon, crear_pokemon, borrar_pokemon, edit_pokemon, ver_form, crear_regpok, ver_vis, busqueda
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ver_pokemon, name='ver'),
    path('nuevo_pokemon/', crear_pokemon, name='crear_pokemon'),
    path('borrar_pokemon/<int:id>', borrar_pokemon, name='borrar_pokemon'),
    path('edit_pokemon/<int:id>', edit_pokemon, name='edit_pokemon'),
    path('form/', ver_form, name='ver_form'),
    path('visualizar/', ver_vis, name='ver_vis'),
    path('crear_regpok/', crear_regpok, name='crear_regpok'),
    path('buscar/', busqueda, name='busqueda'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

