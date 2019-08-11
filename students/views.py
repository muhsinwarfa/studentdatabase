from django.shortcuts import render, redirect
from .models import Student
from .Forms import StudentForm

# Create your views here.
def index(request):
#get all students
    students = Student.objects.all()
    context = {
        'students': students
    }
# pass the context object to be rendered in the index file
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        # populate the form with the input details
        student = StudentForm(request.POST)
        if student.is_valid():
            student.save()
            return redirect('index')
    else:
        # display a new form again
        student = StudentForm()

    context = {
        'student': student
    }

    return render(request, 'new.html', context)


def delete_record(request,id):
    # get the object from the student db
    record = Student.objects.get(id=id)
    record.delete()
    return redirect('index')

def update_record(request,id):
    instance = Student.objects.get(id=id)
    # populate the form with the data obtained above
    form = StudentForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'update.html', {'form': form})

def view_record(request,id):
    student = Student.objects.get(id=id)
    return render(request, 'view.html', {'student': student})




