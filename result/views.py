from django.shortcuts import render
from result.models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == "POST":
        if request.method == "POST":
            roll = request.POST.get('roll1')
            year = request.POST.get('year1')
            try:
                student = Student.objects.get(roll_no=roll)
            except:
                error = "yes"
                return render(request, 'search.html', {'error': error})
            else:
                if year != student.year:
                    error = "yes"
                    print(year)
                    print(student.year)
                    return render(request, 'search.html', {'error1': error})
                else:
                    file1 = student.file
                    error = "no"
                d = {'error1': error, 'roll_no': roll, 'file': file1}
                return render(request, 'result.html', d)

    else:
        print('Get Method')
    return render(request, 'search.html')

def student(request):
    error = False
    if request.method == "POST":
        roll = request.POST['roll1']
        year = request.POST['year']
        image = request.FILES['img']
        Student.objects.create(roll_no=roll, year=year, file=image)
        error = True
    d = {'error': error}
    return render(request, 'student.html', d)
