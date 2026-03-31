from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from .models import MyAppStudent


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


@login_required(login_url='login')
def profile(request):
    student, created = MyAppStudent.objects.update_or_create(
        roll_no=str(request.user.id),
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


def api_list(request):
    return render(request, 'api/api_list.html')