from django.urls import path

from scrapper import views

urlpatterns = [
    path('get_data_clinica_santa_maria', views.get_data_clinica_santa_maria),
    path('get_data_recetas_de_cocina', views.get_data_recetas_de_cocinas),
    path('get_data_tabla_de_calorias', views.get_data_tabla_de_calorias)
]