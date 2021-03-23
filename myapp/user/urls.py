from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'
urlpatterns = [
    path('<int:pk>/profile', views.ProfileView.as_view(), name='profile'),
    path('<int:pk>/follow', views.follow_view, name='follow'),
    path('<int:pk>/unfollow', views.unfollow_view, name='unfollow'),
]
