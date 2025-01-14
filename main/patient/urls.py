from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor/dashboard/', views.doctor_dashbaord, name='doctor_dashboard'),
    path('doctor/quick-add-patient/', views.doctor_quick_add_patient, name='quick-add-patient'),
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('doctor/logout/', views.doctor_logout, name='doctor_logout'),
    path('doctor/reset-password/', views.doctor_change_password, name='doctor_change_password'),
]