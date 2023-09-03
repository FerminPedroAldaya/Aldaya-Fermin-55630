from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LogoutView

#SEPARE DE 3 CADA URL PARA TENER MAS ORGANIZADO CADA MODELO. EMPLEADO EMPLEADOR EMPLEO
urlpatterns = [
    path('inicio/', inicio, name="inicio"),      
    path('sobreMi/', sobreMi, name="sobreMi"),

    
    path('lista_empleados/', lista_empleados, name='lista_empleados'),
    path('empleado/<int:curriculum_id>/', detalle_empleado, name='detalle_empleado'),
    path('empleadoForm/', empleadoForm, name='empleadoForm'),
    path('updateEmpleado/<int:curriculum_id>/', updateEmpleado, name='updateEmpleado'),
    path('deleteEmpleado/<int:curriculum_id>/', deleteEmpleado, name='deleteEmpleado'),

    path('lista_empleos/', lista_empleos, name='lista_empleos'),
    path('trabajo/<int:trabajo_id>/', detalle_empleo, name='detalle_empleo'),
    path('trabajoForm/', trabajoForm, name='trabajoForm'),
    path('updateEmpleo/<int:trabajo_id>/', updateEmpleo, name='updateEmpleo'),
    path('deleteEmpleo/<int:trabajo_id>/', deleteEmpleo, name='deleteEmpleo'),

    path('lista_empleadores/', lista_empleadores, name='lista_empleadores'),
    path('empleador/<int:empleador_id>/', detalle_empleador, name='detalle_empleador'),
    path('empleadorForm/', empleadorForm, name='empleadorForm'),
    path('updateEmpleador/<int:empleador_id>/', updateEmpleador, name='updateEmpleador'),
    path('deleteEmpleador/<int:empleador_id>/', deleteEmpleador, name='deleteEmpleador'),

    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('registro/', registro, name="registro"),
    path('eliminar_usuario/', eliminar_usuario, name="eliminar_usuario"),    
    path('editar_perfil/', editar_perfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

    path('lista_usuarios/', lista_usuarios, name="lista_usuarios"),
    path('perfil/<int:usuario_id>/', detalle_usuario, name='detalle_usuario'),
    path('perfil/', perfil, name="perfil"),
    path('contactar_usuario/<int:destinatario_id>/', contactar_usuario, name='contactar_usuario'),
    path('agregarInformacion/', agregarInformacion, name="agregarInformacion"),
]
