from django.core import validators
from django import forms
from .models import Student, ProEvent


class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','departments','employer','date','package','ref_no']
        #adding bootstrap classes to form inputs
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'departments' : forms.Select(attrs={'class':'form-control'}),
            'employer': forms.TextInput(attrs={'class':'form-control'}),
            'date' : forms.DateInput(format='%m/%d/%Y',attrs={'class':'form-control'}),
            'package': forms.NumberInput(attrs={'class':'form-control'}),
            'ref_no': forms.NumberInput(attrs={'class':'form-control'}),
        }

class AddProEvent(forms.ModelForm):
    class Meta:
        model = ProEvent
        fields = ['activity','dept','pname','pcontact','participants','fromdate','todate']
