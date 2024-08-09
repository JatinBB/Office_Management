from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fname', 'lname', 'designation', 'role', 'user']

def save(self, commit=True, user=None):
    employee = super().save(commit=False)
    if user:
        employee.user = user
    if commit:
        employee.save()
    return employee