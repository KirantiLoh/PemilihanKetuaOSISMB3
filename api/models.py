from django.utils.timezone import now
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Candidate(models.Model):
    image = CloudinaryField('image')
    ketua = models.CharField(max_length=100)
    wakil = models.CharField(max_length=100)
    visi = models.TextField()
    misi = models.TextField()
    total_vote = models.PositiveIntegerField(default=0)
    date_added = models.DateField(default=now)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"Ketos : {self.ketua} & Waketos : {self.wakil}"