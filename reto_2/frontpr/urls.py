from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('determinarpais/', views.dpais, name='determinarpais'),
    path('determinarpais/', views.procesar_archivo, name='procesar_archivo'),
    ##
    path('procesar_archivo/', views.procesar_archivo, name='procesar_archivo'),
    path('mostrar_resultado/', views.mostrar_resultado, name='mostrar_resultado'),
    path('mostrar_resultado/', views.descargar_resultado, name='descargar_resultado')
]