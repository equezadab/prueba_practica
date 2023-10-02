# Generated by Django 4.2.5 on 2023-10-01 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_app', '0002_region_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPokemon',
            fields=[
                ('idTipPokemon', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_app.pokemon')),
                ('nombre_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_app.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='RegionPokemon',
            fields=[
                ('idRegTipo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_app.pokemon')),
                ('nombre_region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_app.region')),
            ],
        ),
    ]