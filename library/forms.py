from django import forms
from django.utils import timezone
from datetime import timedelta


class ReminderForm(forms.Form):
    email = forms.EmailField(label='Enter email', required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)
    datetime = forms.DateTimeField(label='Enter time', required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('Email cannot be empty.')
        return email

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text or not text.strip():
            raise forms.ValidationError('Text cannot be empty.')
        return text

    def clean_datetime(self):
        datetime = self.cleaned_data['datetime']
        max_datetime = timezone.now() + timedelta(days=2)

        if datetime < timezone.now():
            raise forms.ValidationError("Datetime can't be in the past.")
        elif datetime > max_datetime:
            raise forms.ValidationError("Datetime can't be more than 2 days in the future.")
        return datetime
