# Generated by Django 4.2.4 on 2023-10-22 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appfinal', '0013_ingredientes_author_ingredientes_upload_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('autor', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='mensaje',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='descripcion',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='estilo',
            field=models.CharField(blank=True, default=2, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='levadura',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='lupulo',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='malta',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
