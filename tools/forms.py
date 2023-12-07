from django import forms

class CalculatorForm(forms.Form):
    num_1 = forms.IntegerField(
        label='Number 1',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Numer 1'}
        )
    )
    num_2 = forms.IntegerField(
        label='Number 2',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Number 2'}
        )
    )