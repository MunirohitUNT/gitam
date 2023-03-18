from django.shortcuts import render, redirect
from django.http import HttpResponse
from admissions.models import Student
from admissions.forms import StudentModelForm
from admissions.forms import VendorForm
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ImageForm
from django.contrib.auth.hashers import make_password

hashed_password = make_password('password123')


# Create your views here.
@login_required
def homepage(request):
    return render(request, 'index.html')


def logoutUser(request):
    return render(request, 'logout.html')


@login_required
def addAdmission(request):
    form = StudentModelForm
    studentform = {'form': form}

    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)
    # values = {"name": "Santosh", "age": 26, "address": "denton"}
    return render(request, 'addadmission.html', studentform);


@login_required
def admissionsReport(request):
    # get all the records from the table
    result = Student.objects.all();  # SELECT * FROM students
    # store it in dictionary students
    students = {'allstudents': result}
    return render(request, 'admissionReport.html', students);


@login_required
@permission_required('admissions.delete_student')
def deleteStudent(request, id):
    s = Student.objects.get(id=id)  # select * from admissions_student where id=idvalue
    s.delete()
    return admissionsReport(request)


@login_required
@permission_required('admissions.change_student')
def updateStudent(request, id):
    s = Student.objects.get(id=id)  # select * from admissions_student where id=idvalue
    form = StudentModelForm(instance=s)
    dict = {'form': form}

    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
        return homepage(request)
    return render(request, 'updateadmission.html', dict);


@login_required
def addVendor(request):
    form = VendorForm
    vform = {'form': form}

    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['bloodGroup'])
            print(form.cleaned_data['age'])
            print(form.cleaned_data['contact'])
        return homepage(request)
    # values = {"name": "Santosh", "age": 26, "address": "denton"}
    return render(request, 'addvendor.html', vform);


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})
