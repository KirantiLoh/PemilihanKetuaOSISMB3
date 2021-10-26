from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    gender_choice = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan')
    )
    class_choices = (
        (8, 'SHS10SCI'),
        (9, 'SHS10SOC'),
        (10, 'SHS11SCI'),
        (11, 'SHS11SOC'),
        (12, 'SHS12SCI'),
        (13, 'SHS12SOC'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=gender_choice)
    kelas = models.PositiveSmallIntegerField(choices=class_choices)
    voted = models.BooleanField(default=False)

    def __str__(self):
        return self.nama

class Teacher(models.Model):
    gender_choice = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=gender_choice)
    mengajar = models.CharField(max_length=30)
    voted = models.BooleanField(default=False)

    def __str__(self):
        return self.nama

