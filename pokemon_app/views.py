from django.shortcuts import render, redirect
from .models import Pokemon, Region, Tipo, TipoPokemon, RegionPokemon
from .forms import formularioPokemon

# Create your views here.


def ver_pokemon(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'ver_lista.html', {'pokemons': pokemons})


def ver_region(request):
    regions = Region.objects.all()
    return render(request, 'ver_lista.html', {'regions': regions})


def ver_tipo(request):
    tipos = Tipo.objects.all()
    return render(request, 'ver_lista.html', {'tipos': tipos})


def ver_regpok(request):
    regpoks = RegionPokemon.objects.all()
    return render(request, 'ver_lista.html', {'regpoks': regpoks})


def ver_tippok(request):
    tippoks = TipoPokemon.objects.all()
    return render(request, 'ver_lista.html', {'tippoks': tippoks})


def crear_pokemon(request):
    pokemon = Pokemon(
        id=request.POST['id'],
        nombre=request.POST['nombre'],
        imagen=request.FILES['imagen']
    )
    pokemon.save()
    return redirect('/')


def crear_regpok(request):
    regpokemon = RegionPokemon(
        idRegTipo=request.POST['idRegTipo'],
        nombre_region=request.POST['nombre_region'],
        nombre=request.POST['nombre']
    )
    regpokemon.save()
    return redirect('/')


def crear_tippok(request):
    tippok = TipoPokemon(
        idRegTipo=request.POST['idRegTipo'],
        nombre_region=request.POST['nombre_region'],
        nombre=request.POST['nombre']
    )
    tippok.save()
    return redirect('/')


def borrar_pokemon(request, id):
    borrar_pokemon = Pokemon.objects.get(id=id)
    print(id)
    borrar_pokemon.delete()
    return redirect('/')


def edit_pokemon(request, id):
    pokemon = Pokemon.objects.get(id=id)
    forms = formularioPokemon(request.POST or None, instance=pokemon)
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('/')
    return render(request, 'edit_pokemon.html', {'forms': forms})


def ver_form(request):
    context = {}
    return render(request, 'formulario.html', context)


def ver_vis(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'visualizar.html', {'pokemons': pokemons})


def busqueda(request):
    con = request.GET.get('q')
    resultados = []
    if con:
        resultados = Pokemon.objects.filter(nombre__icontains=con)
    return render(request, 'buscar.html', {'resultados': resultados, 'con':con })
