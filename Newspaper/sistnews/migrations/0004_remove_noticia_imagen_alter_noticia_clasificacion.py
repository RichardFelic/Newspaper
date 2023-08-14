# Generated by Django 4.1.1 on 2022-10-09 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistnews', '0003_remove_noticia_file_alter_noticia_clasificacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='imagen',
        ),
        migrations.AlterField(
            model_name='noticia',
            name='clasificacion',
            field=models.CharField(choices=[('Negocio', 'Negocio'), ('Tecnología', 'Tecnología'), ('Salud', 'Salud'), ('Ciencias', 'Ciencia'), ('Política', 'Política'), ('Cultura', 'Cultura')], max_length=20),
        ),
    ]
