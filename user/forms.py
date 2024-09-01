from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['firstname','lastname','username', 'email', 'password']

    def save(self, commit=True):
        print("Save method called")
        print("Cleaned data:", self.cleaned_data)


        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        