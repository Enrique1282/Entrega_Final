from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Estilos(models.Model):
    nombre = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    amargor = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=200)
    def __str__(self) -> str:
        return f"nombre: {self.nombre} - Color: {self.color} - Amargor: {self.amargor} - descripcion: {self.descripcion}"
    

class Ingredientes(models.Model):
    estilo = models.CharField(max_length=40, blank=True, null=True)
    malta = models.CharField(max_length=40)
    lupulo = models.CharField(max_length=40)
    levadura = models.CharField(max_length=40)
    descripcion = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    upload_time = models.DateTimeField(auto_now_add=True)  

    def __str__(self) -> str:
        return f"Estilo: {self.estilo} -Malta: {self.malta} - Lupulo: {self.lupulo} - Levadura: {self.levadura}"


class Imagen(models.Model):
    # vinvulo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)


    def __str__(self):
        return f"{settings.MEDIA_URL}{self.imagen}"


class ResenaCerveza(models.Model):
    titulo = models.CharField(max_length=200)
    cerveceria = models.CharField(max_length=100)
    estilo = models.CharField(max_length=50)
    contenido = models.TextField()
    calificacion = models.FloatField()

    def __str__(self):
        return f"{self.titulo}"
    

#############################################
 # foro

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}"

class Tema(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.categoria}-{self.titulo}"

class Mensaje(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tema}-{self.contenido}"