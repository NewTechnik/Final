from django.db import models

# Create your models here.
class Alumno(models.Model):
	dni = models.CharField('Documento de Identidad', max_length=8)
	nombre = models.CharField('Nombre', max_length=30, blank=False, null=False)
	apellido = models.CharField('Apellido', max_length=30, blank=False, null=False)
	matriculado = models.BooleanField('Matriculado', default=False)
	def __str__(self):
		return '%s - %s / %s' % (self.dni, self.apellido, self.nombre)

class Contacto(models.Model):
	id = models.AutoField(primary_key=True)
	nombreu = models.CharField(max_length=50, blank=False, null=False)
	correou = models.CharField(max_length=50, blank=False, null=False)
	mensajeu = models.TextField(max_length=400, blank=False, null=False)
	estado = models.BooleanField('Estado', default=True)
	fecha_creacion = models.DateField('Fecha de creacion', auto_now=True, blank=False, null=False)
	class Meta:
		verbose_name = "Contacto"
		verbose_name_plural = "Contactos"
	def __str__(self):
		return self.nombreu