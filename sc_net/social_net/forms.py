from .models import Person, Announcement
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

class AnnouncementCreateForm(forms.Form):
    person = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class':'form-control form-control-lg'
            }
        )
    )
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg'
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control form-control-lg'
            }
        )
    )
    image = forms.JSONField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control form-control-lg'
            }
        )
    )

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=255,
        label='Юзернейм пользователя.',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg'
            }
        )
    )
    password1 = forms.CharField(
        max_length=255,
        label='Пароль.',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg'
            }
        )
    )
    password2 = forms.CharField(
        max_length=255,
        label='Подтверждение пароля.',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg'
            }
        )
    )

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError('password does not match')
        return self.cleaned_data['password1']

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).count():
            raise ValidationError('User with that username already exists.')
        return self.cleaned_data['username']

    def save(self, commit=True):
        user = super().save()
        Person.objects.create(
            username = self.cleaned_data['username'],
            user = user
        )


# class CreateUserForm(forms.Form):
#     username = forms.CharField(
#         max_length=255,
#         widget=forms.TextInput(
#             attrs={
#                 'class':'form-control form-control-lg'
#             }
#         )
#     )
#     name = forms.CharField(
#         max_length=255,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control form-control-lg'
#             }
#         )
#     )
#     age = forms.DecimalField(
#         max_digits=5,
#         widget=forms.IntegerField(
#             attrs={
#                 'class':'form-control form-control-lg'
#             }
#         )
#     )
#     about = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 'class':'form-control form-control-lg'
#             }
#         )
#     )
#     image = forms.JSONField(
#         widget=forms.CharField(
#             attrs={
#                 'class':'form-control form-control-lg'
#             }
#         )
#     )
#     friends = forms.JSONField(
#         widget=forms.CharField(
#             attrs={
#                 'class':'form-control form-control-lg'
#             }
#         )
#     )
#
#     def clean_username(self):
#         if Person.objects.filter(username=self.cleaned_data['username']).count():
#             raise ValidationError("a user with that username already exists")
#         return self.cleaned_data['username']


