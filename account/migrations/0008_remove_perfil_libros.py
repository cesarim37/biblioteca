# Generated by Django 2.2 on 2020-01-20 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_perfil_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='libros',
        ),
    ]
