from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="Home"),
    path('vote', views.vote_view, name="Vote"),
    path('success', views.success_view, name="Success"),
    path('error', views.error_view, name="Error"),
    path('error/<int:id>', views.error_view, name="Error"),
]
