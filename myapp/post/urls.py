from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.create_post, name='post'),
    path("<int:post_id>/like/", views.like, name="like"),
    path("<int:post_id>/unlike/", views.unlike, name="unlike"),
    path("<int:post_id>/delete/", views.delete, name="delete"),
    path("<int:post_id>/reply_list/", views.reply_list, name="reply_list"),
    path("<int:post_id>/reply/", views.reply, name="reply"),
]
