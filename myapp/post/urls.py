from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.CreatePost.as_view(), name='post'),
    path("<int:post_id>/like/", views.like, name="like"),
    path("<int:post_id>/unlike/", views.unlike, name="unlike"),
]
