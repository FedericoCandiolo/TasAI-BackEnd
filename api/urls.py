from django.urls import path, include
from rest_framework import routers
from . import views
from django.contrib.auth.views import LoginView, LogoutView

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'plan', views.PlanViewSet)
router.register(r'propiedad', views.PropiedadViewSet)
router.register(r'tasacion', views.TasacionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('home/', views.home_page),
    path('hello/', views.hello_page),

]
