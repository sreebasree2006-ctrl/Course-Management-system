from django import forms 
from .models import Student,Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','age','email','city']
        model = Course
        fields =['course','duration','fees']

class RegisterForm(UserCreationForm):
   class Meta:
       model=User
       fields=['username','email']
       
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course', 'duration', 'fees', 'trainer', 'description', 'active']