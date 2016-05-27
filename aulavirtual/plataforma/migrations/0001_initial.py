# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 20:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Acceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('terminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('codigo', models.CharField(max_length=100, verbose_name='Codigo')),
                ('logo', models.ImageField(upload_to='cursos/logos/', verbose_name='Logo')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_matricula', models.DateField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.Alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_membresia', models.CharField(max_length=100, verbose_name='Tipo')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profesores',
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.Profesor'),
        ),
        migrations.AddField(
            model_name='acceso',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.Alumno'),
        ),
        migrations.AddField(
            model_name='acceso',
            name='membresia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.Membresia'),
        ),
    ]
