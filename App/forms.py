from django import forms
from django.forms import SelectDateWidget

from App.models import CourseModel,StudentModel

class CourseForm(forms.ModelForm):
    date=forms.DateField(widget=forms.DateField)
    time=forms.TimeField(widget=forms.TimeInput)
    class Meta:
        model=CourseModel
        fields='__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
