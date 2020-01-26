# Generated by Django 2.2 on 2020-01-24 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_auto_20200124_0418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('material', models.CharField(max_length=100, verbose_name='Material')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción')),
                ('categoria', models.CharField(blank=True, choices=[('mapas', 'Mapas'), ('meni', 'Material Educativo no Impreso'), ('juegos', 'Juegos Didacticos'), ('otros', 'Otros')], max_length=20)),
            ],
            options={
                'verbose_name': 'Material no Bibliografico',
                'verbose_name_plural': 'Material no Bibliografico',
            },
        ),
        migrations.RemoveField(
            model_name='ejemplarmaterial',
            name='no_bibliografico',
        ),
        migrations.DeleteModel(
            name='NoBibliografico',
        ),
        migrations.AddField(
            model_name='ejemplarmaterial',
            name='material',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, related_name='ejemplar_material', to='catalog.Material'),
            preserve_default=False,
        ),
    ]