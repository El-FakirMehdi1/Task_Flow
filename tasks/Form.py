from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    Completed = forms.BooleanField(required=False, label='Task Done?')
    due_date = forms.DateField(
        required=False,
        label='Due date',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Task
        fields = [
        'title',
        'description',
        'category',
        'priority',
        'due_date',
        'Completed',
    ]

class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]