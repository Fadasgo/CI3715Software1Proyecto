from django.db import models

# Create your models here.

class Departamento(models.Model):
	codigoDepartamento = models.CharField(primary_key=True, max_length=15)
	nombreDepartamento = models.CharField(max_length=60)

	def __str__(self):
		return self.codigoDepartamento + ", " + self.nombreDepartamento

class Programa(models.Model):
	"""docstring for maestria"""
	codigoPrograma = models.IntegerField(primary_key=True)
	nombrePrograma = models.CharField(max_length=60)
	#codigoDepartamentoPertenece = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.codigoPrograma) + ", " + self.nombrePrograma

#class Rol(models.Model):
#	codigoRol = models.IntegerField(primary_key=True)
#	nombreRol = models.CharField(max_length=60) # Profesor (2), Estudiante (3), Jefe del departamento (1)

class Asignatura(models.Model):
    codigoMateria = models.CharField(primary_key=True,max_length=7)
    nombreMateria = models.CharField(max_length=60)
    unidadesCredito = models.IntegerField()
    area = models.CharField(max_length=60) 
    programaPertenece = models.ForeignKey(Programa, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, default="",on_delete=models.CASCADE)
    # Entre las areas segun el pdf se encuentran asignaturas basicas, inteligencia artificial
    # bases de datos entre otras
    def __str__(self):
    	return self.codigoMateria + ", " + self.nombreMateria + ", " + str(self.unidadesCredito) + ", " + self.departamento_id + ", " + self.programaPertenece_id + ", " + self.area 

class Usuario(models.Model):
	cedulaIdentidad = models.IntegerField(primary_key=True)
	primerNombre = models.CharField(max_length=15)
	segundoNombre = models.CharField(max_length=15, null = True)
	primerApellido = models.CharField(max_length=15)
	segundoApellido = models.CharField(max_length=15)
	correo = models.EmailField(unique = True)
	password = models.CharField(max_length = 16)
	#rol1 = models.ForeignKey(Rol, on_delete=models.CASCADE)
	rol = models.CharField(max_length = 25, default="")
	codigoDepartamento1 = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	#create = models.DateTimeField(auto_now_add = True)  guarda la fecha en la cual se crea un usuario
	# modificado = models.DateField(auto_now = True) guarda la fecha en la que se modifico por ultima vez el usuario

	def __str__(self):
		return str(self.cedulaIdentidad) + ", "+ self.primerNombre+", "+ self.primerApellido +", "+ self.segundoApellido +", "+ self.correo+", "+ self.rol+", "+ self.codigoDepartamento1_id

		