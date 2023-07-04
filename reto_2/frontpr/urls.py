from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mostrar_resultado/<int:puntaje_riesgo>/<str:umbral_riesgo>/', views.mostrar_resultado, name='mostrar_resultado'),
]