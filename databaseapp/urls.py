from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.contrib import admin

urlpatterns = [

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.home_view, name='home'),                # Home page (e.g., shows posts from DB)
    path('register/', views.register_view, name='register'),  # Register a new user (saves to DB)
    path('login/', views.login_view, name='login'),           # Log in (checks DB for user)
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Log out
]
