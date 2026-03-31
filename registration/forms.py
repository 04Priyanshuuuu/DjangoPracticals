from django import forms
from .models import RegistrationStudent


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationStudent
        fields = ['name', 'email', 'age', 'course']
        widgets = {
    'name': forms.TextInput(attrs={'class': 'w-full border p-2 rounded-lg'}),
    'email': forms.EmailInput(attrs={'class': 'w-full border p-2 rounded-lg'}),
    'age': forms.NumberInput(attrs={'class': 'w-full border p-2 rounded-lg'}),
    'course': forms.TextInput(attrs={'class': 'w-full border p-2 rounded-lg'}),
}

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 16:
            raise forms.ValidationError('Age must be at least 16.')
        return age
