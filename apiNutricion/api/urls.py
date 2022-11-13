from django.urls import path

from api import views

urlpatterns = [

    # Food
    path('get_food/<str:arg>', views.get_food),
    path('get_food/', views.get_food),
    path('get_food_pagination/', views.FoodListApiView.as_view() ),

    # User
    path('get_user/', views.UserListApiView.as_view() ),
    path('create_user/', views.UserCreateView.as_view()),
    path('detail_user/<pk>', views.UserDetailView.as_view()),
    path('delete_user/<pk>', views.UserDeleteView.as_view()),
    path('update_user/<pk>', views.UserUpdateView.as_view()),
    path('modified_user/<pk>', views.UserRetriveUpdateView.as_view()),
]
