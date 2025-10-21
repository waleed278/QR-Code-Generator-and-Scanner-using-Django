from django import forms
from django.core.validators import MaxLengthValidator,MinLengthValidator,RegexValidator
from django.core.exceptions import ValidationError

def max_img_size(image):
    
    if image.size>2048*1024:
        raise ValidationError("Image size should not exceed 4 MB.")


class ScannerForm(forms.Form):
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
    image = forms.ImageField(
        validators=[max_img_size],
        widget=forms.ClearableFileInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Image size cannot exceed 4 MB'
            }
        )
    )