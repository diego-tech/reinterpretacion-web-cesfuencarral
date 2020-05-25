# Generated by Django 3.0.6 on 2020-05-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200525_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesGrados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('smr', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='SMR')),
                ('dependencia', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='DEPENDENCIA')),
                ('enfermeria', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='ENFERMERÍA')),
                ('dam', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='DAM')),
                ('integracion', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='INTEGRACIÓN')),
                ('infantil', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='INFANTIL')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
            ],
            options={
                'verbose_name': 'imágen',
                'verbose_name_plural': 'imágenes',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ImagenesNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('new1', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='new1')),
                ('new2', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='new2')),
                ('new3', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='new3')),
                ('new4', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='new4')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
            ],
            options={
                'verbose_name': 'imágen',
                'verbose_name_plural': 'imágenes',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='Imagenes',
        ),
    ]