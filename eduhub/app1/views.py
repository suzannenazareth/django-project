from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Student, StudentDetails

@login_required(login_url='login')
def HomePage(request):
    students = Student.objects.filter(is_active=True)
    return render(request, 'home.html', {'students': students})

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            messages.error(request, "Your password and confirm password do not match!")
            return redirect('signup')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    else:
        return render (request,'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'login.html')

def AddPage(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept = request.POST.get('dept')
        student = Student.objects.create(roll_no=roll_no, first_name=first_name, last_name=last_name, dept=dept)
        
        return redirect('home')
    return render(request, 'add.html')

def ViewPage(request):
    students = Student.objects.all()
    return render(request, 'view.html', {'students': students})

def get_records_view(request, roll_no):
    student = Student.objects.get(roll_no=roll_no)
    student_details = StudentDetails.objects.filter(student=student)
    return render(request, 'records.html', {'student': student, 'student_details': student_details})




def DeletePage(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        try:
            student_to_delete = Student.objects.get(roll_no=roll_no)
            student_to_delete.delete()
            return redirect('delete')
        except Student.DoesNotExist:
            error_message = "Student with provided roll number does not exist."
            students = Student.objects.all()
            return render(request, 'delete.html', {'error_message': error_message, 'students': students})
    else:
        students = Student.objects.all()
        return render(request, 'delete.html', {'students': students})

def update_student_details(request, roll_no):
    student = Student.objects.get(roll_no=roll_no)
    
    if request.method == 'POST':
        semester = request.POST.get('semester')
        semester_cleared = request.POST.get('semester_cleared')
        extracurricular = request.POST.get('extracurricular')
        cocurricular = request.POST.get('cocurricular')
        attendance_percentage = request.POST.get('attendance_percentage')
        cgpi = request.POST.get('cgpi')
        sgpi = request.POST.get('sgpi')
        
        student_details = StudentDetails.objects.create(
            student=student,
            semester=semester,
            semester_cleared=semester_cleared,
            extracurricular=extracurricular,
            cocurricular=cocurricular,
            attendance_percentage=attendance_percentage,
            cgpi=cgpi,
            sgpi=sgpi
        )
        
        return redirect('view')  
    
    return render(request, 'update.html', {'student': student})
    
    return render(request, 'update.html', {'student': student})





def LogoutPage(request):
    logout(request)
    return redirect('login')


