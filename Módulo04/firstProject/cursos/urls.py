from django.urls import path, include
from . import views

urlpatterns = [
    path('cursos/2023/', views.lista_cursos, name = 'cursos2023'),
    path('cursos/2024/', views.lista_cursos_2024, name = 'cursos2024'),
]