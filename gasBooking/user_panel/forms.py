from django import forms
from core.models import Booking, Complaint

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = []  # No fields needed, as cylinder assignment is automatic

class ComplaintForm(forms.ModelForm):
    issue_type = forms.ChoiceField(choices=Complaint.ISSUE_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    class Meta:
        model = Complaint
        fields = ['issue_type', 'description']