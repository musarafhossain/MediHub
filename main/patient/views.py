from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'doctor/home.html')

#Doctor Login
def doctor_login(request):
    return render(request, 'doctor/login.html', {
        'page_title': 'Doctor Login'
    })

#Reset Password
def doctor_reset_password(request):
    return render(request, 'doctor/reset_password.html')