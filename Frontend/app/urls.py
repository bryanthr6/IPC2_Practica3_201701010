from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('carga/', views.cargar_archivo, name='carga'),
    path('estadisticas/', views.ver_grafica, name='estadisticas'),
    path('pdf/', views.datos_estudiante, name='pdf'),
    path('procesados/', views.ver_procesados, name='ver_procesados'),  # Nueva URL para ver procesados
]