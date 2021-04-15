from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'
urlpatterns = [
    path('<int:user_id>/profile/', views.user_profile, name='profile'),
    path('<int:user_id>/follow/', views.follow_view, name='follow'),
    path('<int:user_id>/unfollow/', views.unfollow_view, name='unfollow'),
    path('administrator/', views.administrator, name='administrator'),
]
