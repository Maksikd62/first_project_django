from django import forms
from users.models import User

class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"  # all Book model fields
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name.isalpha():
            raise forms.ValidationError("First name must contain only letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must contain only letters.")
        return last_name
    
    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        if self.instance and self.instance.user_name == user_name:
            return user_name
        if User.objects.filter(user_name=user_name).exists():
            raise forms.ValidationError("User with this username already exists. Please choose another one.")
        return user_name

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone.isdigit():
            raise forms.ValidationError("Phone must contain only digits.")
        return phone