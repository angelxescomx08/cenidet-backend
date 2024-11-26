from django.http import JsonResponse
from django.views import View
import json

from app.models import Usuario, Rol

class Login(View):
    def post(self, request):
        data = json.loads(request.body)

        # Obtener email y password desde el JSON
        email = data.get('email')
        password = data.get('password')

        usuario = Usuario.objects.filter(email=email, password=password)
        # usuario = Usuario.objects.all().values()

        return JsonResponse({
            'token': "token",
        })

class PopulateTables(View):
    def get(self, request):
        profesor_rol = Rol(nombre="Profesor")
        profesor_rol.save()

        administrador_rol = Rol(nombre="Administrador")
        administrador_rol.save()

        alumno_rol = Rol(nombre="Alumno")
        alumno_rol.save()

        alumno = Usuario(
            nombre = "Kary",
            apellido = "Hernández",
            email = "ninfayuka@gmail.com",
            password = "123456789",
            rol = alumno_rol
        )
        alumno.save()

        profesor = Usuario(
            nombre = "Profesor",
            apellido = "Perez",
            email = "profesor@gmail.com",
            password = "123456789",
            rol = profesor_rol
        )
        profesor.save()

        administrador = Usuario(
            nombre = "Administrador",
            apellido = "Perez",
            email = "administrador@gmail.com",
            password = "123456789",
            rol = administrador_rol
        )
        administrador.save()


        return JsonResponse({
            'message': "Base de datos poblada"
        })



