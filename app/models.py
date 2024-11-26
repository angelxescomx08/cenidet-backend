from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    profesores = models.ManyToManyField('Usuario')

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    semestre = models.CharField(max_length=100)
    anio = models.CharField(max_length=100)
    profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
