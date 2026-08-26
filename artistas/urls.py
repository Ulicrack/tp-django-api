from django.urls import path
from . import views


urlpatterns = [
    path('artistas/', views.lista_artistas),
    path('artistas/<int:pk>/', views.detalle_artista),
]