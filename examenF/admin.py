from django.contrib import admin
from examenF.models import Materia, Nota, Seccion, Profesor, Grado

#Registramos nuestras clases principales.
admin.site.register(Materia)
admin.site.register(Nota)
admin.site.register(Seccion)
admin.site.register(Profesor)

admin.site.register(Grado)
