# Generated by Django 4.2.6 on 2023-10-20 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bebidas',
            old_name='nombre',
            new_name='nombre_bebida',
        ),
    ]
