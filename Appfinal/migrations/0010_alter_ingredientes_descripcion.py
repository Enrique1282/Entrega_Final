# Generated by Django 4.2.5 on 2023-10-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appfinal', '0009_ingredientes_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientes',
            name='descripcion',
            field=models.TextField(max_length=200),
        ),
    ]
