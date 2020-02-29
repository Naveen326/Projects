from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Question,Answer
from django.contrib.auth.models import User


class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=(
            'user',
            'title',
            'slug',
            'question',
        )


class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=(
            'user',
            'answer',
        )

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
        'username',
        'password1',
        'password2',
        ]

    def save(self,commit=True):
        user= super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user
