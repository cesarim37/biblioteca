# Generated by Django 2.2 on 2020-01-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_perfil_libros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='libros',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.EjemplarLibro'),
        ),
    ]
