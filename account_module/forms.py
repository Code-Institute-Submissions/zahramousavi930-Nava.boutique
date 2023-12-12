from django import forms
from django.core import validators



class RegisterForm(forms.Form):
    name=forms.CharField(
        label='name',
        widget=forms.TextInput(),
        validators=[
            validators.MaxLengthValidator(50)
    ]
    )

    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )


    phone_number = forms.CharField(
        label='phone_number',
        widget=forms.TextInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )




class LoginForm(forms.Form):

    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )

    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='new password ',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
