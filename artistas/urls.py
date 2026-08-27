from django.urls import path
from . import views


urlpatterns = [
    path('artistas/', views.lista_artistas),
    path('artistas/<int:pk>/', views.detalle_artista),
    path('eventos/', views.lista_eventos),
    path('eventos/<int:pk>/', views.detalle_evento),
]