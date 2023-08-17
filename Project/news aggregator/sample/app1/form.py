from django import forms
from app1.models import userdet

class userform(forms.ModelForm):
    class Meta:
        model = userdet
        fields = "__all__"

"""
class EmpForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = "__all__"
"""