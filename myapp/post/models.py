from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Post(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, default="")
    text = models.CharField(max_length=200)
    like = models.PositiveIntegerField(default=0)

    def __str__(self):
        return (str(self.text)+'(' + str(self.user)+')')


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='like_user')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post")

    def __str__(self):
        return (str(self.user) + '　→ ' + str(self.post) + '　にいいね')


class Reply(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="main_post")
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, default="")
    text = models.CharField(max_length=200)
    like = models.PositiveIntegerField(default=0)


    def __str__(self):
        return (str(self.text)+'(' + str(self.user)+')')
