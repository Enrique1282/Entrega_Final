# Generated by Django 4.2.4 on 2023-10-20 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appfinal', '0009_ingredientes_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resenacerveza',
            name='creado_en',
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='descripcion',
            field=models.TextField(max_length=200),
        ),
    ]