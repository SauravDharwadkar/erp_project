from django.core import validators
from django import forms
from .models import Student, ProEvent

class DateInput(forms.DateInput):
    input_type = 'date'

class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','departments','employer','date','package','ref_no']
        #adding bootstrap classes to form inputs
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'departments' : forms.Select(attrs={'class':'form-control'}),
            'employer': forms.TextInput(attrs={'class':'form-control'}),
            'date' : DateInput(attrs={'class':'form-control'}),
            'package': forms.NumberInput(attrs={'class':'form-control'}),
            'ref_no': forms.NumberInput(attrs={'class':'form-control'}),
        }

class AddProEvent(forms.ModelForm):
    class Meta:
        model = ProEvent
        fields = ['no','activity_name','department_name','resourse_person_name','resourse_person_contact','no_of_participants','event_from_date','event_to_date']
        #adding bootstrap classes to form inputs
        widgets = {
            'no': forms.TextInput(attrs={'class':'form-control'}),
            'activity_name': forms.TextInput(attrs={'class':'form-control'}),
            'department_name': forms.Select(attrs={'class':'form-control'}),
            'resourse_person_name': forms.TextInput(attrs={'class':'form-control'}),
            'resourse_person_contact': forms.TextInput(attrs={'class':'form-control'}),
            'no_of_participants': forms.TextInput(attrs={'class':'form-control'}),
            'event_from_date': DateInput(attrs={'class':'form-control'}),
            'event_to_date': DateInput(attrs={'class':'form-control'}) 
        }
