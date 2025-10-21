from django import forms
from django.core.validators import MaxLengthValidator,MinLengthValidator,RegexValidator
from django.core.exceptions import ValidationError



class GenerateForm(forms.Form):
    phone_number = forms.CharField(
        max_length=13,
        validators=[
            
            MaxLengthValidator(13),
            MinLengthValidator(11),
            RegexValidator(
    regex=r'^(?:\+92|0)?3[0-9]{9}$',
    message="Enter a valid  phone number (e.g., +923001234567 or 03001234567)."
)
        ],
        widget=forms.NumberInput(attrs={
            'class':'form-control', 'placeholder':'Enter Phone number like : 3422337511'
        })
    )

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if int(amount)<1:
            raise ValidationError("Please Enter Correct Amount")
        return amount

    amount = forms.CharField(
        validators=[MinLengthValidator(1),MaxLengthValidator(6)],
        widget=forms.NumberInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Enter you amount'
            }
        )
    )