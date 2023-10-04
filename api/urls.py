from api.views import *
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'plan', views.PlanViewSet)
router.register(r'propiedad', views.PropiedadViewSet)
router.register(r'tasacion', views.TasacionViewSet)

urlpatterns = [
    # path('api/', include(router.urls)),
    # Registro/Login/Pass
    path('cambiar-contraseña/', CambiarContraseña.as_view(), name='cambiar_contraseña'),
    path('registro/', RegistroUsuario.as_view(), name='registro_usuario'),
    path('inicio-sesion/', IniciarSesion.as_view(), name='inicio_sesion'),
    # Propiedades
    path('propiedad/<int:propiedad_id>/', GetOnePropiedad.as_view(), name='propiedad-detalle'),
    path('propiedades-de-usuario/<int:user_id>/', GetAllPropiedades.as_view(), name='propiedades-de-usuario'),
    path('guardar-propiedad/', GuardarPropiedad.as_view(), name='crear-propiedad'),
    # Tasaciones
    path('tasaciones-de-usuario/<int:user_id>/', TasacionesDeUsuario.as_view(), name='tasaciones-de-usuario'),
    path('tasacion-propiedad-existente/<int:propiedad_id>/', TasacionConPropiedadExistente.as_view(),
         name='tasacion-propiedad-existente'),
    path('tasacion-propiedad-nueva/', TasacionConPropiedadNueva.as_view(),
         name='tasacion-propiedad-nueva'),
    # Cambio de Plan
    path('cambio-de-plan/<int:user_id>/', ActualizarPlan.as_view(), name='cambio-de-plan'),
    path('esta-guardado-propiedad/<int:id_propiedad>/', EstaGuardadoPropiedad.as_view(),
         name='esta-guardado-propiedad'),
    path('esta-guardado-tasacion/<int:id_tasacion>/', EstaGuardadoTasacion.as_view(), name='esta-guardado-tasacion'),

]
