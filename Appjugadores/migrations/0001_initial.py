# Generated by Django 4.0.4 on 2022-06-06 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='antecedentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año_de_debut', models.DateField()),
                ('club_debutante', models.CharField(max_length=30)),
                ('club_actual', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='estadisticas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goles', models.IntegerField()),
                ('velocidad', models.IntegerField()),
                ('posicion', models.CharField(max_length=30)),
                ('precisiondepase', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='jugadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=50)),
                ('fechadenacimiento', models.DateField()),
                ('peso', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('nacionalidad', models.CharField(max_length=30)),
            ],
        ),
    ]
