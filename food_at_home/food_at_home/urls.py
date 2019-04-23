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
from .views.cliente import *
# from .views.login import *
from django.conf.urls import url
from .views.administrador import *
# willaims
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Index
    path('', inicio, name='index'),
    path('inicio', Inicio2, name='inicio2'),
    path('inicio/<int:id>', inicio3),
    path('login', login, name='login'),
    path('categorias', categorias),
    path('todos-res', allrestaurante),
    path('espacio', espacio, name="espacio"),
    # administrador
    path('administrador/index', index, name='admiIndex'),
    path('administrador/gestion-usuarios', gestion_usuarios, name='gestionUsuarios'),
    path('administrador/gestion-restaurante', gestion_restaurante, name='gestionRestaurante'),
    path('administrador/gestion-Ciudades', gestion_ciudades, name='gestionCiudades'),
    path('administrador/savecategoria', save_categoria, name="saveCategoria"),
    path('administrador/verrestaurante/<int:id>', verRes),
    path('cliente/<str:name>/menu/<int:id>/<int:idc>', menus),
    path('administrador/solicitudes', solicitudes, name="solicitudes"),
    # path('verificar', verificar, name="verificar"),
    path('login/crear.html', usuario_nuevo, name="Usernew"), # esta url muestra el formualario para crear el usuario
    path('save_usuario', guardar_user, name='save'),
    path('cliente/inicio_usuario_cliente.html/<str:name>', user, name="inicio_usuario"),
    path('cliente/categoria', cliente_cat, name="cliente_cat"),
    path('cliente/restaurante', cliente_rest, name="cliente_rest"),
    path('cliente/ciudad', cliente_ciudad, name="cliente_ciudad"),
    path('cliente/query-ciudad/<int:id>', cliente_queryCiudad, name="cliente_queryCiudad"),
    path('cliente/restaurante/menu/<int:id>', cliente_restaurante_menu),
    path('cliente/vermenu/<int:id>', vermenu),


    path('cliente/configuracion_cliente.html', configuracion),
    path('administrador/root.html', root),
    # path('administrador/Empleado.html', empleado),
    # Usuario
    path('usuario/crear', crear_usuario),
    path('usuario/actualizar/<int:id>', actualizar_usuario),
    # path('usuario/ver_usuario/<int:id>', ver_usuario),
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
    # path('guardar_user', guardar_user),
    # url(r'^guardar_user/', guardar_user),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
