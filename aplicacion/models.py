from django.db import models
from django.contrib.auth.models import User
#LOS TRES MODELOS USADOS PARA EL PROYECTO CON SUS RESPECTIVOS DATOS PARA LA BASE DE DATOS

class Empleos(models.Model):
    cargo = models.CharField(max_length=50)
    detalles = models.TextField()
    ubicacion = models.CharField(max_length=50)
    sueldo = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Curriculum(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField()
    presentacion = models.TextField()
    experiencia = models.TextField()
    estudios = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Empleador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField()
    profesion = models.CharField(max_length=50)
    edad = models.IntegerField()
    nombreEmpresa = models.CharField(max_length=50)
    presentacion = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Avatar(models.Model):
    imagen =  models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return  f"{self.user}{self.imagen}"

class Informacion(models.Model):
    informacion = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return  f"{self.user}{self.informacion}"
    
class MensajeContacto(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asunto
    
