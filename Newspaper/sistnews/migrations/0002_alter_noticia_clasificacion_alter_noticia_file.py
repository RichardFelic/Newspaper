# Generated by Django 4.1.1 on 2022-10-09 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistnews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='clasificacion',
            field=models.CharField(choices=[('Cultura', 'Cultura'), ('Política', 'Política'), ('Negocio', 'Negocio'), ('Ciencias', 'Ciencia'), ('Salud', 'Salud'), ('Tecnología', 'Tecnología')], max_length=20),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='file',
            field=models.FileField(null=True, upload_to=None),
        ),
    ]