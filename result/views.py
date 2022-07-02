from django.shortcuts import render
from result.models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')
def search(request):
    if request.method == "POST":
        roll = request.POST.get('roll1')
        student = Student.objects.get(roll_no= roll)
        file1 = student.file
        context = {
            'roll_no': roll,
            'file': file1
        }
        return render(request, 'result.html', context)
    else:
        print("GET Method")
    return render(request, 'search.html')

def score(request):
    return render(request, 'result.html')

def student(request):
    if request.method == "POST":
        roll = request.POST.get('roll1')
        file = request.FILES['file']
        Student.objects.create(roll_no=roll, file=file)

        return render(request, 'student.html')
    else:
        print("Get method")
    return render(request, 'student.html')
