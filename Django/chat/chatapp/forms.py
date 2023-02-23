from django import forms

class CheckInForm(forms.Form):
    check_in = forms.DateTimeField()

class CheckOutForm(forms.Form):
    check_out = forms.DateTimeField()