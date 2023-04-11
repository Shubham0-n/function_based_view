from django import forms
from .models import Student
from phonenumber_field.formfields import PhoneNumberField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class StudentForms(forms.ModelForm):
    phone_number = PhoneNumberField()

    class Meta:
        model = Student
        fields = "__all__"
