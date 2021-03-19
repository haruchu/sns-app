from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

class UserSignupView(generic.FormView):
    form_class = UserCreationForm
    template_name = 'signup.html'

    def form_valid(self, form):
        return render(self.request, 'signup.html', {'form': form})


class UserConfirmView(generic.FormView):
    form_class = UserCreationForm

    def form_valid(self, form):
        return render(self.request, 'confirm.html', {'form': form})

    def form_invalid(self, form):
        return render(self.request, 'signup.html', {'form': form})


class UserCreateView(generic.FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        # 認証
        user = form.save()
        # ログイン
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, 'signup/sinup.html', {'form': form})
