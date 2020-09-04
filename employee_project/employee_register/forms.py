from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'firstName':'First Name',
            'lastName':'Last Name',
            'email':'Email',
            'phoneNumber':'Phone Number',
            'address':'Address',
            'address2':'Address2',
            'city':'City',
            'zipCode':'Zip Code',
            'state':'State',
        }