from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.create_post, name='post'),
    path("<int:post_id>/like/", views.like, name="like"),
    path("<int:post_id>/unlike/", views.unlike, name="unlike"),
]
