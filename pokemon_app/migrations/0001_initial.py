# Generated by Django 4.2.5 on 2023-09-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img/')),
            ],
        ),
    ]
