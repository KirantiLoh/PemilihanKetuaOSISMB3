from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name="Login"),
    path('logout', views.logout_view, name="Logout"),
]
