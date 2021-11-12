from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name="Login"),
    path('logout', views.logout_view, name="Logout"),
    path('set-voted-to-false', views.set_voted_to_false, name='Set Voted To False'),
    path('set-student-voted-to-true', views.set_student_voted_to_true, name='Set Student Voted To True'),
    path('set-teacher-voted-to-true', views.set_teacher_voted_to_true, name='Set Teacher Voted To True'),
]
