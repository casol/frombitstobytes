from django import forms


class ContactForm(forms.Form):
    """
    Base contact form class.
    """
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(required=True, max_length=100, label='Email')
    subject = forms.CharField(required=True, max_length=200, label='Subject')
    message = forms.CharField(required=True, widget=forms.Textarea, label='Message')

