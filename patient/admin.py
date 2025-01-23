from django.contrib import admin
from .models import Patient, Visit

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','name','gender','age','mobile', 'address')
    search_fields = ('name',)

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id','patient', 'next_visit', 'detail', 'medicine_detail','note', 'amount')
    search_fields = ('patient',)