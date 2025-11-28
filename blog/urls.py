from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articulos/', views.articulos, name="articulos"),
    path('info/<int:id>/', views.info, name="info"),
    path('categoria/<int:id>/', views.filtro_categoria, name="filtro_categoria"),
    path('etiqueta/<int:id>/', views.filtro_etiqueta, name='filtro_etiqueta'),
]