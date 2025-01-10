from django import forms
from users.models import User

class CreateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"  # всі поля моделі User
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ініціалізуємо всі поля порожнім значенням
        for field_name, field in self.fields.items():
            if field_name != 'avatar':  # Робимо виключення для поля avatar
                field.required = True
                field.initial = ""  # Поля будуть пустими за замовчуванням
            else:
                field.required = False

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
        if User.objects.filter(user_name=user_name).exists():
            raise forms.ValidationError("User with this username already exists. Please choose another one.")
        return user_name

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone.isdigit():
            raise forms.ValidationError("Phone must contain only digits.")
        return phone
