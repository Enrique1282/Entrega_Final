# Generated by Django 4.2.4 on 2023-10-20 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appfinal', '0011_remove_ingredientes_estilo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientes',
            name='estilo',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]