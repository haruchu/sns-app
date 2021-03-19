from django.urls import path
from . import views

app_name = 'signup'
urlpatterns = [
    path('', views.UserSignupView.as_view(), name="signup"),
    path('confirm/', views.UserConfirmView.as_view(), name="confirm"),
    path('create/', views.UserCreateView.as_view(), name="create"),
]
