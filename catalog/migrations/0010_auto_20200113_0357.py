# Generated by Django 2.2 on 2020-01-13 08:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20200111_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='cota',
        ),
        migrations.AddField(
            model_name='ejemplarlibro',
            name='cota',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Cota'),
            preserve_default=False,
        ),
    ]
