from secrets import choice
from django.db import models 
from tinymce import models as tinymce_models
from django.contrib.auth.models import User

# Create your models here.
class Clasificacion(models.Model):
    clasificacion=models.CharField(max_length=50, null=True)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.clasificacion

class Noticia(models.Model):
    CATEGORIA=(
        ('General', 'General'),
        ('Tecnologia', 'Tecnologia'),
        ('Cultura', 'Cultura'),
        ('Ciencia', 'Ciencia'),
        ('Negocio', 'Negocio'),
        ('Salud', 'Salud'),
    )
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, editable=False, verbose_name='Autor')
    fecha = models.DateField(auto_now_add=False, null= True, verbose_name='Fecha')
    epigrafe = models.CharField(max_length=200, null=True, verbose_name='Epígrafe')
    titular=models.CharField(max_length=200, verbose_name='Título')
    subtitulo=models.CharField(max_length=200, verbose_name='Subtítulo')
    cuerpo=tinymce_models.HTMLField(verbose_name='Descripción')
    imagen=models.ImageField(upload_to="img", null=True)
    piefoto=models.CharField(max_length=100, verbose_name='Pie de Foto')
    clasificacion=models.CharField(max_length=20, choices=CATEGORIA, null=True, verbose_name='Clasificación')
    
    def __str__(self):
        return self.titular

