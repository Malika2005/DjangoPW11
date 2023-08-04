from django.shortcuts import render, get_object_or_404, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.surname = request.POST['surname']
        student.age = request.POST['age']
        student.course = request.POST['course']
        student.instrument = request.POST['instrument']
        student.performance = request.POST['performance']
        paid_for_studies = request.POST.get('paid_for_studies', False)
        student.paid_for_studies = paid_for_studies == 'True'
        student.save()
        return redirect('student_list')
    return render(request, 'student_edit.html', {'student': student})

# Create your views here.
