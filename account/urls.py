from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name="Login"),
    path('logout', views.logout_view, name="Logout"),
    path('set-voted-to-false', views.set_voted_to_false, name='Set Voted To False')
]
