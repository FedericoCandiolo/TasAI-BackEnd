from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('home/', views.home_page),
    path('hello/', views.hello_page)

]
