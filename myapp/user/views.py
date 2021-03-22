from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FriendShip
from post.models import Post, Like
from .helpers import get_current_user


class ProfileView(generic.DetailView):
    model = User
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        follower = User.objects.get(username=self.request.user)
        followee = User.objects.get(id=self.kwargs['pk'])
        context = super(ProfileView, self).get_context_data(**kwargs)
        user_id = self.kwargs['pk']
        context['user_id'] = user_id
        context['current_user'] = get_current_user(self.request)
        context['followee'] = FriendShip.objects.filter(
            followee=followee).count()
        context['follower'] = FriendShip.objects.filter(
            follower=followee).count()
        # 相手をフォローしている人
        context['followees'] = FriendShip.objects.filter(followee=followee)
        # 相手がフォローしている人
        context['followers'] = FriendShip.objects.filter(follower=followee)
        if user_id is not context['current_user'].username:
            result = FriendShip.objects.filter(
                follower=follower).filter(followee=followee)
            context['connected'] = True if result else False
        return context


def follow_view(request, *args, **kwargs):
    follower = User.objects.get(username=request.user)
    followee = User.objects.get(id=kwargs['pk'])
    created = FriendShip.objects.get_or_create(
        follower=follower, followee=followee)
    if (created):
        messages.success(request, '{}をフォローしました'.format(followee.username))
    else:
        messages.warning(
            request, 'あなたはすでに{}をフォローしています'.format(followee.username))
    return redirect('user:profile', pk=followee.id)


def unfollow_view(request, *args, **kwargs):
    follower = User.objects.get(username=request.user)
    followee = User.objects.get(id=kwargs['pk'])
    if follower == followee:
        messages.warning(request, '自分自身のフォローを外せません')
    else:
        unfollow = FriendShip.objects.get(follower=follower, followee=followee)
        unfollow.delete()
        messages.success(
            request, 'あなたは{}のフォローを外しました'.format(followee.username))
    return redirect('user:profile', pk=followee.id)
