from django.contrib import admin
from .models import Candidate
from django.shortcuts import render
from django.urls import path
from django.contrib.auth.models import Group
from datetime import datetime
from account.models import Student, Teacher

# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    list_display= ('ketua', 'wakil', 'total_vote')
    list_filter = ('date_added',)
    search_fields = ('ketua', 'wakil')

    def graph_view(self, request):
        candidates = Candidate.objects.filter(date_added__day = datetime.now().day)
        students = Student.objects.all().count()
        teachers = Teacher.objects.all().count()
        total_vote = students + teachers
        return render(request, 'admin/graph.html', {'candidates':candidates, 'total':total_vote})

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('result', self.graph_view),
        ]
        return urls + my_urls

admin.site.register(Candidate, CandidateAdmin)
admin.site.unregister(Group)