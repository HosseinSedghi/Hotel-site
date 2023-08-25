from django import forms

from blog.models import Ticket


class TicketForm(forms.Form):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'contactus',
            'placeholder': 'Title'
        }),
        error_messages={
            'required': 'this field is must be fill.'
        }
    )
    text = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'textarea',
            'placeholder': 'Text',
            'row': 20
        }),
        error_messages={
            'required': 'this field is must be fill.'
        }
    )
