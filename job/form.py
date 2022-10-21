from django import forms
from .models import Apply 


class ApplyForm(forms.ModelForm):
    class meta:
        model = Apply
        fields =['name','email','website','cv','coverletter']