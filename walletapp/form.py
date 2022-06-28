from cProfile import label
from dataclasses import fields
from django import forms
from .models import expences

class DateInput(forms.DateInput):
    input_type='date'

class ExpForm(forms.ModelForm):
    
    class Meta:
        model=expences
        fields='__all__'

        widgets={
        'date':DateInput(),
                
        }
        labels={
                'expence':"Expences",
                'pay':"Amount",
                'date':"Date",
        }

        