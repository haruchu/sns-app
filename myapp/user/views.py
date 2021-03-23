from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import FriendShip
from post.models import Post, Like
from .helpers import get_current_user


@login_required
def user_profile(request, user_id):
    follower = User.objects.get(username=request.user)
    followee = User.objects.get(id=user_id)
    user = User.objects.get(id=user_id)
    context = {
        "current_user": get_current_user(request),
        "user": user,
        "followee": FriendShip.objects.filter(
            followee=followee).count(),
        "follower": FriendShip.objects.filter(
            follower=followee).count(),
        # 相手をフォローしている人
        "followees": FriendShip.objects.filter(followee=followee),
        # 相手がフォローしている人
        "followers": FriendShip.objects.filter(follower=followee),
    }
    if user_id is not user.username:
        result = FriendShip.objects.filter(
            follower=follower).filter(followee=followee)
        context['connected'] = True if result else False
    return render(request, 'profile.html', context)


@login_required
def follow_view(request, user_id):
    follower = User.objects.get(username=request.user)
    followee = User.objects.get(id=user_id)
    created = FriendShip.objects.get_or_create(
        follower=follower, followee=followee)
    if (created):
        messages.success(request, '{}をフォローしました'.format(followee.username))
    else:
        messages.warning(
            request, 'すでに{}をフォローしています'.format(followee.username))
    return redirect('user:profile', user_id=followee.id)


@login_required
def unfollow_view(request, user_id):
    follower = User.objects.get(username=request.user)
    followee = User.objects.get(id=user_id)
    unfollow = FriendShip.objects.get(follower=follower, followee=followee)
    unfollow.delete()
    messages.success(
        request, '{}のフォローを外しました'.format(followee.username))
    return redirect('user:profile', user_id=followee.id)
