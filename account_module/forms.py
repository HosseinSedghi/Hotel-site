from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(),
        error_messages={
            'required': 'username field is xxx required'
        }
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        error_messages = {
            'required': 'password field is xxx required'
        }
    )
