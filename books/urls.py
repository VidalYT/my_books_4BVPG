from django.urls import path
from . import views

# Añadimos las conexiones de las urls generadas a partir de la seleccion.
urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:id>/', views.detail, name='detail_book'),
    path('edit/<int:id>/', views.edit, name='edit_book'),
    path('delete/<int:id>/', views.delete, name='delete_book'),
]s