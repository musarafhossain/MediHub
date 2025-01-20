from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('email/', views.n_patients, name='email'),
    path('doctor/dashboard/', views.doctor_dashbaord, name='doctor_dashboard'),
    path('doctor/quick-add-patient/', views.doctor_quick_add_patient, name='quick-add-patient'),
    path('patients/', views.all_patients, name='all-patients'),
    path('patients/add', views.add_patients, name='add-patients'),
    path('patients/delete/<int:id>', views.delete_patients, name='delete-patients'),
    path('patients/update/<int:id>', views.update_patients, name='update-patients'),
    path('reports/', views.reports, name='reports'),
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('doctor/logout/', views.doctor_logout, name='doctor_logout'),
    path('doctor/reset-password/', views.doctor_change_password, name='doctor_change_password'),
]