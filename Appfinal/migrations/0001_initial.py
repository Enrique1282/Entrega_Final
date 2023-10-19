# Generated by Django 4.2.4 on 2023-10-13 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estilos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('amargor', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agua', models.IntegerField()),
                ('malta', models.CharField(max_length=40)),
                ('lupulo', models.CharField(max_length=40)),
                ('levadura', models.CharField(max_length=40)),
            ],
        ),
    ]