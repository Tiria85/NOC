# Generated by Django 4.2.5 on 2023-10-30 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_bebidas_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('reservation_time', models.DateTimeField(auto_now=True)),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
    ]
