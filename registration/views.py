from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import StudentRegistrationForm
from .models import Student


def register(request):
    students = Student.objects.all().order_by('-created_at')

    selected_student = None
    student_id = request.GET.get('student')

    if student_id:
        selected_student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('registration:register')
    else:
        form = StudentRegistrationForm()

    return render(request, 'registration/register.html', {
        'form': form,
        'students': students,
        'selected_student': selected_student
    })

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)

    return render(request, 'registration/student_detail.html', {
        'student': student
    })