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
    path("<int:post_id>/reply/like/<int:reply_id>/", views.reply_like, name="reply_like"),
    path("<int:post_id>/reply/unlike/<int:reply_id>/", views.reply_unlike, name="reply_unlike"),
    path("<int:post_id>/reply/delete/<int:reply_id>/", views.reply_unlike, name="reply_delete"),
]
