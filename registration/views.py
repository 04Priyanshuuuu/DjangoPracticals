from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentRegistrationForm


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('registration:register')
    else:
        form = StudentRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
