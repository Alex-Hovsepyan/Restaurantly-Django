from django import forms
from .models import Reservation, ContactMessage, Subscribe

class ReservationModelForm(forms.ModelForm):

    class Meta:

        model = Reservation
        fields = ['user_name', 'user_email', 'user_phone', 'user_date', 'user_time', 'user_count', 'user_message']

class ContactMessageModelForm(forms.ModelForm):

    class Meta:

        model = ContactMessage
        fields = ['user_name', 'user_email', 'user_subject', 'user_message']

class SubscribeModelForm(forms.ModelForm):

    class Meta:

        model = Subscribe
        fields = ['user_email']