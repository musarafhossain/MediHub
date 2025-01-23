from django.db import models
from django.utils.timezone import now

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others'),
)

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, default='Male', max_length=10)
    age = models.IntegerField(default=0)
    mobile = models.IntegerField(null=True)
    address = models.TextField(null=True)
    added_time = models.DateField(auto_now_add=True, null=True)

class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    detail = models.TextField(null=True)
    medicine_detail = models.TextField(null=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2, default=0.0)
    next_visit = models.IntegerField(default=0)
    visit_date = models.DateField(default=now, null=True)
    note = models.TextField(null=True)
    