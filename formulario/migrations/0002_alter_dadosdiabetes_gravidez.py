# Generated by Django 5.1.7 on 2025-04-07 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadosdiabetes',
            name='gravidez',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número de gestações'),
        ),
    ]
