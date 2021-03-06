# Generated by Django 3.2.5 on 2021-07-04 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('isbn', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ISBN')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre del libro')),
                ('autor', models.CharField(blank=True, max_length=20, null=True, verbose_name='autor')),
                ('descripcion', models.CharField(blank=True, max_length=20, null=True, verbose_name='descripcion')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
