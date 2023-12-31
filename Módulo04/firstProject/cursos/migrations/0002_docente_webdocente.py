# Generated by Django 3.2.20 on 2023-09-22 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('especialidad', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WebDocente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('url_fb', models.URLField(unique=True)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateField()),
                ('ranking', models.IntegerField()),
                ('estado', models.CharField(choices=[('I', 'Implementación'), ('R', 'Revisión'), ('E', 'Error'), ('A', 'Aprobados')], max_length=1)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.docente')),
            ],
        ),
    ]
