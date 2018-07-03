from django.urls import path
from .views import ListaMedico, IngresarOrden

urlpatterns = [
    path('medicos/', ListaMedico.as_view(), name="ListaMedicos"),
    path('generar/<int:id_medico>/', IngresarOrden.as_view(), name="IngresarOrden"),
]