# Generated by Django 2.2 on 2020-01-25 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0008_auto_20200124_0544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamomaterial',
            old_name='lector_material',
            new_name='usuario',
        ),
    ]