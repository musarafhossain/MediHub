#Django Imports
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.db.models import Count, Sum

#Local Imports
from .forms import CustomAuthenticationForm, CustomPasswordChangeForm, QuickPatientForm, PatientForm
from .models import Patient

#Python Imports
from datetime import date, timedelta
import calendar

# Home view
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
    return render(request, 'doctor/add-patient.html', {
        'page_title': 'Quick Add Patient',
        'form': fm,
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
    return render(request, 'doctor/add-patient.html', {
        'page_title': 'Add Patient',
        'form': fm,
    })

#Update patient
def update_patients(request, id):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    if id is not None:
        patient = Patient.objects.get(id=id)
        if request.method=='POST':
            fm = PatientForm(request.POST, instance=patient)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Patient updated successfully")
            else:
                messages.warning(request, "Something went wrong!!")
            redirect('update-patients', id)
        else:
            fm = PatientForm(instance=patient)
        return render(request, 'doctor/add-patient.html', {
            'page_title': 'Update Patient',
            'form': fm,
        })

#Delete patient
def delete_patients(request, id):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    if id is not None:
        patient = Patient.objects.get(id=id)
        patient.delete()
    return redirect('all-patients')

#Toatl Patient Reports View
def reports(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    
    # Get all Year
    years = Patient.objects.values('visit_date__year').annotate(total=Count('id'))
    selectedYear = date.today().year
    if request.GET.get('year'):
        selectedYear = int(request.GET.get('year'))
    else:
        if years:
            year_values = [year['visit_date__year'] for year in years]
            selectedYear = date.today().year if date.today().year in year_values else year_values[0]

    # Get all Month
    months = Patient.objects.filter(visit_date__year=selectedYear).values('visit_date__month').annotate(total=Count('id'))
    monthName = [{
        'name': calendar.month_name[month['visit_date__month']],
        'number': month['visit_date__month'] 
    } for month in months]

    if request.GET.get('month'):
        selectedMonth = int(request.GET.get('month'))
    else:
        selectedMonth = date.today().month

    dailyChartLabels, dailyChartValues = [], []
    monthChartLabels, monthChartValues = [], []
    yearChartLabels, yearChartValues = [], []
    # Chart By Month
    if request.GET.get('chart_type')=='monthly':
        mPatients = Patient.objects.filter(visit_date__year=selectedYear).values('visit_date__month').annotate(total=Count('id'))
        for data in mPatients:
            monthChartLabels.append(calendar.month_name[data['visit_date__month']])
            monthChartValues.append(data['total'])
    # Chart By Year
    elif request.GET.get('chart_type')=='yearly':
        yPatients = Patient.objects.filter().values('visit_date__year').annotate(total=Count('id'))
        for data in yPatients:
            yearChartLabels.append(data['visit_date__year'])
            yearChartValues.append(data['total'])
    # Chart By Date
    else:
        dPatients = Patient.objects.filter(visit_date__year=selectedYear, visit_date__month=selectedMonth).values('visit_date').annotate(total=Count('id'))
        for data in dPatients:
            dailyChartLabels.append(data['visit_date'].strftime('%d-%m-%y'))
            dailyChartValues.append(data['total'])

    return render(request, 'doctor/reports.html', {
        'page_title': 'Total Patient Reports',
        'dailyChart': {
            'dailyChartLabels': dailyChartLabels,
            'dailyChartValues': dailyChartValues,
        },
        'monthlyChart': {
            'monthlyChartLabels': monthChartLabels,
            'monthlyChartValues': monthChartValues,
        },
        'yearlyChart': {
            'yearlyChartLabels': yearChartLabels,
            'yearlyChartValues': yearChartValues,
        },
        'years': years,
        'months': monthName,
        'curr_year': selectedYear,
        'curr_month': calendar.month_name[selectedMonth],
    })

#Collection Reports View
def collection_reports(request):
    if not request.user.is_authenticated:
        return redirect('doctor_login')
    
    # Get all Year
    years = Patient.objects.values('visit_date__year').annotate(total=Count('id'))
    selectedYear = date.today().year
    if request.GET.get('year'):
        selectedYear = int(request.GET.get('year'))
    else:
        if years:
            year_values = [year['visit_date__year'] for year in years]
            selectedYear = date.today().year if date.today().year in year_values else year_values[0]

    # Get all Month
    months = Patient.objects.filter(visit_date__year=selectedYear).values('visit_date__month').annotate(total=Count('id'))
    monthName = [{
        'name': calendar.month_name[month['visit_date__month']],
        'number': month['visit_date__month'] 
    } for month in months]

    if request.GET.get('month'):
        selectedMonth = int(request.GET.get('month'))
    else:
        selectedMonth = date.today().month

    dailyChartLabels, dailyChartValues = [], []
    monthChartLabels, monthChartValues = [], []
    yearChartLabels, yearChartValues = [], []
    # Chart By Month
    if request.GET.get('chart_type')=='monthly':
        mPatients = Patient.objects.filter(visit_date__year=selectedYear).values('visit_date__month').annotate(total=Sum('amount'))
        for data in mPatients:
            monthChartLabels.append(calendar.month_name[data['visit_date__month']])
            monthChartValues.append(float(data['total']))
    # Chart By Year
    elif request.GET.get('chart_type')=='yearly':
        yPatients = Patient.objects.filter().values('visit_date__year').annotate(total=Sum('amount'))
        for data in yPatients:
            yearChartLabels.append(data['visit_date__year'])
            yearChartValues.append(float(data['total']))
    # Chart By Date
    else:
        dPatients = Patient.objects.filter(visit_date__year=selectedYear, visit_date__month=selectedMonth).values('visit_date').annotate(total=Sum('amount'))
        for data in dPatients:
            dailyChartLabels.append(data['visit_date'].strftime('%d-%m-%y'))
            dailyChartValues.append(float(data['total']))

    return render(request, 'doctor/collection-reports.html', {
        'page_title': 'Collection Reports',
        'dailyChart': {
            'dailyChartLabels': dailyChartLabels,
            'dailyChartValues': dailyChartValues,
        },
        'monthlyChart': {
            'monthlyChartLabels': monthChartLabels,
            'monthlyChartValues': monthChartValues,
        },
        'yearlyChart': {
            'yearlyChartLabels': yearChartLabels,
            'yearlyChartValues': yearChartValues,
        },
        'years': years,
        'months': monthName,
        'curr_year': selectedYear,
        'curr_month': calendar.month_name[selectedMonth],
    })

#Send Email Notification for debug
def n_patients(request):
    # Fetch patients with a past visit date
    patients = Patient.objects.filter(visit_date__lt=date.today())
    count = 0

    for patient in patients:
        next_visit_date = patient.visit_date + timedelta(days=patient.next_visit)
        notification_date = next_visit_date - timedelta(days=1)
        if notification_date == date.today():
            # Prepare email content
            subject = 'Doctor Next Visit'
            context = {
                'next_visit': next_visit_date,
                'name': patient.name,
            }
            email_body = render_to_string('email/email-template.html', context)

            # Send email
            email = EmailMessage(
                subject=subject,
                body=email_body,
                from_email=settings.EMAIL_HOST_USER,
                to=[patient.email],
            )
            email.content_subtype = "html"  # Specify HTML content

            try:
                email.send()
                count += 1  # Increment count only if email sent successfully
            except Exception as e:
                # Log the error (optional, depending on your logging setup)
                print(f"Failed to send email to {patient.email}: {e}")

    # Render the count in the template
    return render(request, 'email/n_patients.html', {
        'count': count,
    })

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
    return render(request, 'auth/login.html', {
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
    return render(request, 'auth/change-password.html', {
        'page_title': 'Change Password',
        'form': fm,
    })
