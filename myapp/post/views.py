from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import PostForm, ReplyForm
from .models import Post, Like, Reply
from user.helpers import get_current_user


@login_required
def create_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.user = request.user
        post = form.save()
        return redirect('/home')
    return render(request, 'home.html', {'form': form})


@login_required
def like(request, post_id):
    post = Post.objects.get(pk=post_id)
    # 0か1か
    like_num = Like.objects.filter(
        user=request.user).filter(post=post).count()
    # 該当するツイートをいいねしていた場合
    if like_num > 0:
        return redirect('/home')
    # いいねしてなかった場合はここまでくる
    post.like += 1
    post.save()
    like = Like()
    like.user = request.user
    like.post = post
    like.save()
    return redirect('/home')


@login_required
def unlike(request, post_id):
    post = Post.objects.get(pk=post_id)
    # 0か1か
    like_num = Like.objects.filter(
        user=request.user).filter(post=post).count()
    # いいねされていなかった場合
    if like_num == 0:
        return redirect('/home')
    # いいねしていた場合はここまでくる
    liking = Like.objects.get(post_id=post_id, user=request.user)
    liking.delete()
    post.like -= 1
    post.save()
    return redirect('/home')


@login_required
def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/home')


@login_required
def reply_list(request, post_id):
    main_post = Post.objects.get(pk=post_id)
    current_user = get_current_user(request)
    initial_dict = {'user': request.user, "post": main_post}
    form = ReplyForm(request.POST or None, initial=initial_dict)
    context = {
        "main_post": main_post,
        "replies": Reply.objects.filter(post=main_post),
        "form": form,
        "user": request.user,
        "current_user": current_user,
        "my_likes_ids": Like.objects.filter(
            user=request.user).values_list('post_id', flat=True),
    }
    return render(request, 'reply.html', context)

@login_required
def reply(request, post_id):
    form = ReplyForm(request.POST)
    if form.is_valid():
        form = ReplyForm(request.POST)
        reply = form.save(commit=False)
        reply.user = request.user
        reply.post = Post.objects.get(pk=post_id)
        reply = form.save()
        return redirect('post:reply_list',post_id=post_id)
    return render(request, 'reply_list.html', {'form': form})

