from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mostrar_resultado/<int:puntaje_riesgo>/', views.mostrar_resultado, name='mostrar_resultado'),
    #path('mostrar_resultado/', views.mostrar_resultado, name='mostrar_resultado'),
    #path('mostrar_resultado/', views.descargar_resultado, name='descargar_resultado')
]