from django.shortcuts import redirect, render
from . import urls
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import *
# Create your views here.
def index(request):
    voting = Voting.objects.all()
    return render(request, 'index.html', {'voting': voting})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,email=email,password=password,)
        user.save
        return redirect('/')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def vote(request,pk):
    user = request.user
    vote = Voting.objects.get(id=pk)
    if request.method == 'POST':
        try:
            voter = Voters.objects.get(user=user, voted_for=vote)
            messages.info(request, f"you have already voted for {vote}")
            return redirect('/')  
        except Voters.DoesNotExist:
            Voters.objects.create(user=user, voted_for=vote)
            vote.count += 1
            vote.save()
            messages.success(request, "vote added successfully")
            return redirect('/')
        except TypeError:
            messages.info(request, "you must log in first")
            return redirect('/')