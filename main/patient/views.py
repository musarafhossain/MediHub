from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'doctor/home.html')

#Doctor Login
def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            redirect('/')
    return render(request, 'doctor/login.html', {
        'page_title': 'Doctor Login'
    })

#Reset Password
def doctor_reset_password(request):
    return render(request, 'doctor/reset_password.html')