from django import forms

class SymptomForm(forms.Form):
    symptoms = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter symptoms (e.g., fever, headache, cough)'
            }
        ),
        help_text='Please enter your symptoms separated by commas'
    )
