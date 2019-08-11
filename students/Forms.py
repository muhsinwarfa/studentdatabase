from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
# includes all field labels
        fields = "__all__"


