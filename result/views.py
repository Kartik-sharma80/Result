from django.shortcuts import render
from result.models import *
# Create your views here.
def index(request):
    return render(request, '404.html')

def result(request):
    if request.method == "POST":
        if request.method == "POST":
            year = request.POST.get('year1')

            sem = request.POST.get('sem')
            roll = request.POST.get('roll1')
            dob = request.POST.get('dob')

            try:
                student = Student.objects.get(roll_no=roll.upper())
            except:
                error = "yes"
                return render(request, 'search.html', {'error': error})
            else:
                if year != student.year:
                    error = "yes"
                    return render(request, 'search.html', {'error1': error})
                else:
                    if sem != student.semester:
                        error = "yes"
                        return render(request, 'search.html', {'error2': error})
                    else:
                        if str(dob) != str(student.dob):
                            error = "yes"
                            return render(request, 'search.html', {'error3': error})
                        else:
                            error = "no"
                            total = student.sub1_marks + student.sub2_marks + student.sub3_marks + student.sub4_marks + student.sub5_marks + student.sub6_marks + student.sub7_marks
                            pert = total//7
                            d = {'error3': error, 'student': student, 'total':total, 'pert': pert}
                            return render(request, 'result.html', d)
    else:
        print('Get Method')
    return render(request, 'search.html')

def result_by_name(request):
    if request.method == "POST":
        name = request.POST.get('name')
        fname = request.POST.get('fname')
        dob = request.POST.get('dob')
        sem = request.POST.get('sem')
        qs = Student.objects.all()
        try:
            student = qs.get(name=name, semester=sem, dob=dob, father_name=fname)
        except:
            error = "yes"
            return render(request, 'search_name.html', {'error': error})
        else:
            if fname.upper() != student.father_name:
                error = "yes"
                return render(request, 'search_name.html', {'error1': error})
            else:
                if str(dob) != str(student.dob):
                    error = "yes"
                    return render(request, 'search_name.html', {'error2': error})
                else:
                    if sem != student.semester:
                        error = "yes"
                        return render(request, 'search_name.html', {'error3': error})
                    else:
                        error = "no"
                        total = student.sub1_marks+student.sub2_marks+student.sub3_marks+student.sub4_marks+student.sub5_marks+student.sub6_marks+student.sub7_marks
                        pert = total//7
                        d = {'error3': error, 'name': name, 'total': total, 'pert': pert, 'student': student}
                        return render(request, 'result1.html', d)
    else:
        print('Get Method')
    return render(request, 'search_name.html')


def handle_404(request, exception):
    return render(request, '404.html')
