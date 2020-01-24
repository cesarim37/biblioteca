# Generated by Django 2.2 on 2020-01-24 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0007_prestamomaterial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamomaterial',
            name='ejemplar_material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_ejemplar', to='catalog.EjemplarMaterial'),
        ),
    ]
