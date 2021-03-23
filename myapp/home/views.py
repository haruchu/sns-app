from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from post.forms import PostForm
from post.models import Post, Like

class HomeView(generic.FormView):
    template_name = "home.html"
    form_class = PostForm
    login_url = '/'

    def get_context_data(self, **kwargs):
        initial_dict = {'user': self.request.user}
        form_class = PostForm(self.request.POST or None, initial=initial_dict)
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["form"] = form_class
        context["posts"] = Post.objects.all()
        # ユーザーはリクエストユーザーであるツイートをリスト化
        context['my_likes_ids'] = Like.objects.filter(
            user=self.request.user).values_list('post_id', flat=True)
        return context
    def get_success_url(self):
        return reverse('user:profile', kwargs={'pk': self.user.id})
