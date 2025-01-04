from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'doctor/home.html')

#Doctor Login
def doctor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'doctor/login.html', {
        'page_title': 'Doctor Login'
    })

#Doctor Logout
def doctor_logout(request):
    logout(request)
    return redirect('doctor_login') 


#Reset Password
def doctor_reset_password(request):
    return render(request, 'doctor/reset_password.html')