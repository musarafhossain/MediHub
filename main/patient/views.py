from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import CustomAuthenticationForm, CustomPasswordChangeForm, QuickPatientForm, PatientForm
from django.contrib import messages
from .models import Patient

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    return render(request, 'doctor/home.html', {
        'page_title': 'Home',
    })

#Doctor Dashboard
def doctor_dashbaord(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    return render(request, 'doctor/dashboard.html', {
        'page_title': 'Dashboard',
    })

#Quick add patient
def doctor_quick_add_patient(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    if request.method=='POST':
        fm = QuickPatientForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Patient added successfully")
        else:
            messages.warning(request, "Something went wrong!!")
    else:
        fm = QuickPatientForm()
    return render(request, 'doctor/quick-add-patient.html', {
        'page_title': 'Quick Add Patient',
        'form': fm
    })

#View all patient
def all_patients(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    data = Patient.objects.all().order_by('-id')
    return render(request, 'doctor/all-patients.html', {
        'data': data,
        'page_title': 'All Patients',
    })

#Add patient
def add_patients(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    if request.method=='POST':
        fm = PatientForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Patient added successfully")
        else:
            messages.warning(request, "Something went wrong!!")
    else:
        fm = PatientForm()
    return render(request, 'doctor/quick-add-patient.html', {
        'page_title': 'Add Patient',
        'form': fm
    })

#Delete patient
def delete_patients(request, id):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    if id is not None:
        patient = Patient.objects.get(id=id)
        patient.delete()
    return redirect('all-patients')

#Doctor Login
def doctor_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        fm = CustomAuthenticationForm(request, request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home') 
    else:
        fm = CustomAuthenticationForm()
    return render(request, 'doctor/login.html', {
        'page_title': 'Doctor Login',
        'form': fm,
    })

#Doctor Logout
def doctor_logout(request):
    logout(request)
    return redirect('doctor_login') 

#Reset Password
def doctor_change_password(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    if request.method == 'POST':
        fm = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request, "Password has been changed.")
    else:
        fm = CustomPasswordChangeForm(user=request.user)
    return render(request, 'doctor/change-password.html', {
        'page_title': 'Change Password',
        'form': fm,
    })