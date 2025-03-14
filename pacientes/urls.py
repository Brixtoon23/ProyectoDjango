from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet

router = DefaultRouter()
router.register(r'', PacienteViewSet)  # Se quita el prefijo 'pacientes' aquí

urlpatterns = [
    path('', include(router.urls)),  # Se mantiene limpio para evitar duplicaciones
]
