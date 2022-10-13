from django.urls import path

from api import views

urlpatterns = [

    # Food
    path('get_food/<str:arg>', views.get_food),
    path('get_food/', views.get_food),

]
