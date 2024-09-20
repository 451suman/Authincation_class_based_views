
from django.urls import path

from auth_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("signup/", views.SignupView.as_view(),name="signup"),
    path(
        "change-password/",
        auth_views.PasswordChangeView.as_view(template_name="change-password.html"),
    ),
]
