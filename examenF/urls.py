from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_grado, name ='lista_grado'),
    url(r'^grado/nueva/$', views.grado_nuevo, name='grado_nueva'),
    url(r'^grado/(?P<pk>[0-9]+)/detalle/$', views.detalle_grado, name='detalle_grado'),
    url(r'^grado/(?P<pk>[0-9]+)/eliminar/$', views.Eliminar_grado, name='eliminar_grado'),
    url(r'^grado/(?P<pk>[0-9]+)/editar/$', views.Editar_grado, name='editar_grado'),

    #urls marca_nueva
    #url(r'^materia/lista/$', views.lista_materia, name ='lista_materia'),
    #url(r'^materia/nueva/$', views.materia_nueva, name='materia_nueva'),
    #url(r'^materia/(?P<pk>[0-9]+)/detalle/$', views.detalle_materia, name='detalle_materia'),
    #url(r'^materia/(?P<pk>[0-9]+)/eliminar/$', views.Eliminar_materia, name='eliminar_materia'),
    #url(r'^materia/(?P<pk>[0-9]+)/editar/$', views.Editar_materia, name='editar_materia'),


    ]
