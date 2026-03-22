from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.models import User



def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


@login_required(login_url='login')
def profile(request):
    # One record for the demo, enhanced to show the logged-in user
    student, created = Student.objects.update_or_create(
        roll_no=request.user.id,
        defaults={
            'name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
            'branch': 'Information Technology'
        }
    )
    context = {'student': student}
    return render(request, 'profile.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('myapp:home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'auth/signup.html', {'form': form})




def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    

def create_admin(request):
    username = 'zero'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, '04myexperimentswithai@gmail.com', 'zero')
        return HttpResponse("Superuser created!")

    return HttpResponse("Already exists")