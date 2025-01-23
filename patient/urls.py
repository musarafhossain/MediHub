from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    # Doctor Dashboard
    path('doctor/dashboard/', views.doctor_dashbaord, name='doctor_dashboard'),
    # View all patients
    path('patients/', views.all_patients, name='all-patients'),
    # Add patient [Quick, Normal]
    path('doctor/quick-add-patient/', views.doctor_quick_add_patient, name='quick-add-patient'),
    path('patients/add', views.add_patients, name='add-patients'),
    # Update patient
    path('patients/update/<int:id>', views.update_patients, name='update-patients'),
    # Delete patient
    path('patients/delete/<int:id>', views.delete_patients, name='delete-patients'),
    # Reports [Daily, Monthly, Yearly]
    path('reports/', views.reports, name='reports'),
    # Collection Reports [Daily, Monthly, Yearly]
    path('collection-report/', views.collection_reports, name='collection_reports'),
    # Authentication [Login, Logout, Reset Password]
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('doctor/logout/', views.doctor_logout, name='doctor_logout'),
    path('doctor/reset-password/', views.doctor_change_password, name='doctor_change_password'),
    # Email
    path('email/', views.n_patients, name='email'),
]