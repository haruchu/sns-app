from django.db import models
from django.contrib.auth.models import User

class FriendShip(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followee_friendships')
    followee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower_friendships')

    class Meta:
        unique_together = ('follower', 'followee')

    def __str__(self):
        return ('フォローする人('+str(self.follower)+')⇔' +'フォローされる人('+ str(self.followee)+')')
