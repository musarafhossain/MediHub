from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','name','gender','age','mobile','next_visit','address','detail', 'medicine_detail','note', 'amount')
    search_fields = ('name',)