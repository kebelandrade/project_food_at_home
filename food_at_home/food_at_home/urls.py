"""food_at_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views.usuario import *
from .views.empleado import *
from .views.restaurante import *
from .views.index import *
# from .views.login import *
from django.conf.urls import url
from .views.administrador import *
# willaims

urlpatterns = [

    # Index
    path('', inicio, name='index'),
    path('login', login, name='login'),
    #administrador
    path('administrador/index', index, name='admiIndex' ),
    path('administrador/gestion-usuarios', gestionUsuarios, name='gestionUsuarios'),
    # path('verificar', verificar, name="verificar"),
    path('login/crear.html', usuario_nuevo), #esta url muestra el formualario para crear el usuario
    path('cliente/inicio_usuario_cliente.html', iniciousuario),
    path('cliente/configuracion_cliente.html', configuracion),
    path('administrador/root.html', root),
    path('administrador/Empleado.html', empleado),
    # Usuario
    path('usuario/crear', crear_usuario),
    path('usuario/actualizar/<int:id>', actualizar_usuario),
    path('usuario/ver_usuario/<int:id>', ver_usuario),
    path('usuario/eliminar_usuario/<int:id>', eliminar_usuario),
    # Empleados
    path('administrador/Empleado.html', gestion_empleado),
    path('empleado/crear_empleado', crear_empleado),
    path('empleado/actualizar_empleado/<int:id>', actualizar_empleado),
    path('empleado/act_empleados', actualizar_empleados),
    # Restaurante
    path('restaurante/crear', crear_restaurante),
    path('admin/', admin.site.urls),

    path('formulario.html', form, name='formulario'),
    path('save_usuario', guardar_user, name='save'),
    # path('guardar_user', guardar_user),
    # url(r'^guardar_user/', guardar_user),
]
