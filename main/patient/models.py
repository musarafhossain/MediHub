from django.db import models

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others'),
)

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(choices=GENDER_CHOICES, default='Male', max_length=10)
    age = models.IntegerField(default=0)
    mobile = models.IntegerField(null=True)
    next_visit = models.IntegerField(default=0)
    address = models.TextField(null=True)
    detail = models.TextField(null=True)
    medicine_detail = models.TextField(null=True)
    note = models.TextField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    added_time = models.DateTimeField(auto_now_add=True, null=True)