from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    # Doctor Dashboard
    path('doctor/dashboard/', views.doctor_dashbaord, name='doctor_dashboard'),
    
    #Patient Details
    path('patients/', views.all_patients, name='all-patients'),                                 # View all patients
    path('doctor/quick-add-patient/', views.quick_add_patient, name='quick-add-patient'),       # Quick Add patient
    path('patients/add', views.add_patients, name='add-patients'),                              # Add patient
    path('patients/update/<int:id>', views.update_patients, name='update-patients'),            # Update patient
    path('patients/delete/<int:id>', views.delete_patients, name='delete-patients'),            # Delete patient
    
    # Visit Details [of patient]
    path('patients/all-visit/<int:patient_id>', views.all_visit, name='all-visit'),             # View all visit
    path('patients/add-visit/<int:patient_id>', views.add_visit, name='add-visit'),             # Add visit
    path('patients/update-visit/<int:visit_id>', views.update_visit, name='update-visit'),      # Update visit
    path('patients/delete-visit/<int:visit_id>', views.delete_visit, name='delete-visit'),      # Delete visit
    
    # Reports 
    path('reports/', views.reports, name='reports'),                                            # Patient Reports [Daily, Monthly, Yearly]
    path('collection-report/', views.collection_reports, name='collection_reports'),            # Collection Reports [Daily, Monthly, Yearly]
    
    # Authentication [Login, Logout, Reset Password, Profile, Edit Profile]
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('doctor/logout/', views.doctor_logout, name='doctor_logout'),
    path('doctor/reset-password/', views.doctor_change_password, name='doctor_change_password'),
    path('doctor/profile/', views.profile_view, name='doctor_profile'),
    path('doctor/edit-profile/', views.edit_profile, name='doctor_edit_profile'),
    
    # Email
    path('email/', views.n_patients, name='email'),
]