# Generated by Django 4.2.4 on 2023-10-19 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appfinal', '0008_categoria_tema_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientes',
            name='descripcion',
            field=models.TextField(blank=True, default=0, max_length=200),
        ),
    ]