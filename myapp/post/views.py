from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post, Like

class CreatePost(generic.FormView):
    success_url = reverse_lazy('/home')
    form_class = PostForm

    def form_valid(self, form):
        form_class = PostForm(self.request.POST)
        post = form_class.save(commit=False)
        post.user = self.request.user
        post = form.save()
        return redirect('/home')

    def form_invalid(self, form):
        return render(self.request, 'home.html', {'form': form})

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
