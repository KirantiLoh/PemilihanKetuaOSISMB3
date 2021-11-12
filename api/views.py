from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from account.models import Student, Teacher
from datetime import datetime, timedelta
from api.models import Candidate
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

# Create your views here.
def home_view(request):
    candidates = Candidate.objects.filter(date_added__day = datetime.now().day)
    if len(candidates) < 1:
        candidates = None
    profile = None
    if request.user.is_authenticated:
        try:
            profile = Student.objects.get(user=request.user)
        except ObjectDoesNotExist:
            profile = Teacher.objects.get(user = request.user)
    return render(request, "home.html", {"candidates" : candidates, "profile":profile})

@login_required(login_url="Login")
def vote_view(request):
    try:
        profile = Student.objects.get(user=request.user)
    except ObjectDoesNotExist:
        profile = Teacher.objects.get(user=request.user)
    if profile.voted:
        return redirect("Error", id=2)
    cur_date =  timezone.now().date()
    candidates = Candidate.objects.filter(date_added__day = cur_date.day)
    if len(candidates) < 1:
        candidates = None
    if request.method == 'POST':
        datas = request.POST
        choice = ''
        for data in datas:
            if data.startswith('k'):
                choice = int(data[1:])
        choice = int(choice)
        try:
            candidate = Candidate.objects.get(id=choice)
            candidate_date = candidate.date_added
            diff = cur_date - candidate_date
            if diff.days > 1:
                return redirect("Error", id = 4)
            candidate.total_vote += 1
            candidate.save()
            profile.voted = True
            profile.save()
            return redirect("Success")
        except ObjectDoesNotExist:
            return redirect('Error', 0)
    return render(request, "vote.html", {'candidates':candidates, "profile":profile})

def success_view(request):
    return render(request, "success.html")

def error_view(request, id):
    messages = [
        "You haven't voted",
        "You have voted before, if you haven't, please contact the admin",
        "Your account doesn't exist, re check your username and password or contact the admin...",
        "The candidate you chose isn't for this election, please vote again",
        "You're not admin, you cannot access this page",
        "You have tampered with the voting fuction, your last vote isn't valid, please vote again",
    ]
    return render(request, "error.html", {'message':messages[id-1]})