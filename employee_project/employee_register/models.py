from django.db import models

# Create your models here.

STATES = (
    ('', 'Choose...'),
    ('NY', 'New York'),
    ('CA', 'California'),
    ('TX', 'Texas')
)

class Employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.BigIntegerField()
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipCode = models.BigIntegerField()
    state = models.CharField(max_length=100, choices=STATES, default='1')