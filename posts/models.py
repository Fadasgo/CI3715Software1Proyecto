from django.db import models

# Create your models here.

class Departamento(models.Model):
	codigoDepartamento = models.IntegerField(primary_key=True)
	nombreDepartamento = models.CharField(max_length=60)

class Maestria(models.Model):
	"""docstring for maestria"""
	codigoMaestria = models.IntegerField(primary_key=True)
	nombreMaestria = models.CharField(max_length=60)
	codigoDepartamentoPertenece = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class Rol(models.Model):
	codigoRol = models.IntegerField(primary_key=True)
	nombreRol = models.CharField(max_length=60) # Profesor, Estudiante, Jefe del departamento

class Asignatura(models.Model):
    codigoMateria = models.IntegerField(primary_key=True)
    nombreMateria = models.CharField(max_length=60)
    unidadesCredito = models.IntegerField()
    area = models.CharField(max_length=60) 
    maestriaPertenece = models.ForeignKey(Maestria, on_delete=models.CASCADE)
    # Entre las areas segun el pdf se encuentran asignaturas basicas, inteligencia artificial
    # bases de datos entre otras

class Usuario(models.Model):
	cedulaIdentidad = models.IntegerField(primary_key=True)
	primerNombre = models.CharField(max_length=15)
	segundoNombre = models.CharField(max_length=15, null = True)
	primerApellido = models.CharField(max_length=15)
	segundoApellido = models.CharField(max_length=15)
	correo = models.EmailField(unique = True)
	password = models.CharField(max_length = 16)
	rol1 = models.ForeignKey(Rol, on_delete=models.CASCADE)
	codigoDepartamento1 = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	#create = models.DateTimeField(auto_now_add = True)  guarda la fecha en la cual se crea un usuario
	# modificado = models.DateField(auto_now = True) guarda la fecha en la que se modifico por ultima vez el usuario


		