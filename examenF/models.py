from django.db import models
from django.contrib import admin

class Seccion(models.Model):

    nombre  =   models.CharField(max_length=60)


    class Meta:
                verbose_name="Seccion"
                verbose_name_plural="Secciones"
                ordering = ["nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre

    def __str__(self):

        return self.nombre

class Materia(models.Model):

    nombre  =   models.CharField(max_length=60, verbose_name="Nombre")

    class Meta:
                verbose_name="Materia"
                verbose_name_plural="Materias"
                ordering = ["-nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre

class Nota(models.Model):

    nombre  =   models.IntegerField()

    class Meta:
                verbose_name="Nota"
                verbose_name_plural="Notas"
                ordering = ["-nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre

class Profesor(models.Model):

    nombre  =   models.CharField(max_length=60)


    class Meta:
                verbose_name="Profesor"
                verbose_name_plural="Profesores"
                ordering = ["nombre"]

    def __str__(self): #devuelve el nombre del proyecto
        return self.nombre

    def __str__(self):

        return self.nombre

class Grado(models.Model):

    nombre = models.CharField(max_length=100)
    seccion = models.ForeignKey(Seccion,on_delete=models.CASCADE,related_name="keyseccion",max_length=60)
    materia = models.ManyToManyField(Materia,verbose_name="Materia",related_name="keymateria")
    class Meta:
                verbose_name="Grado"
                verbose_name_plural="Grados"
                ordering = ["-nombre"]

    def __str__(self):
        return self.nombre


#class Alumno(models.Model):

#    nombre = models.CharField(max_length=100)
#    apellido = models.CharField(max_length=100)
#    imagen = models.ImageField(verbose_name="Imagen",upload_to="prod",null=True,blank=True)
#    carne = models.CharField(max_length=60)
#    fecha = models.CharField(max_length=200)
#    seccion = models.ForeignKey(Seccion,on_delete=models.CASCADE,related_name="keyseccion")
#    nota = models.ForeignKey(Nota,on_delete=models.CASCADE,related_name="keynota")
#    materia = models.ManyToManyField(Materia,verbose_name="Materia",related_name="keymateria")
#    grado =  models.ForeignKey(Grado,on_delete=models.CASCADE,related_name="keygrado")
#    profesor =  models.ForeignKey(Profesor,on_delete=models.CASCADE,related_name="keyprofesor")
#    class Meta:
#                verbose_name="Alumno    "
#                verbose_name_plural="Alumnos"
#                ordering = ["-nombre"]

#    def __str__(self):
#        return self.nombre
