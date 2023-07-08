from django import forms
from django.core.validators import RegexValidator

class Contacts(forms.Form):
    name = forms.CharField(min_length=2, max_length=30, required=True, label_suffix=' ', label='Имя *')
    surname = forms.CharField(min_length=2, max_length=40, label_suffix=' ', required=True, label='Фамилия *')
    email = forms.EmailField(required=True, label_suffix=' ', label='Email *')
    
    phone_regex = RegexValidator(regex=r'^\+?7?\d{10}$', message='Введите номер телефона')
    phone_number = forms.CharField(validators=[phone_regex], min_length=10, max_length=12, label_suffix=' ',  label='Телефон *', required=True, error_messages={'required':'Необходимо ввести номер телефона'})
    
    specialisation = forms.CharField(min_length=2, max_length=30, label_suffix=' ', required=False, label='Ваша специальность', empty_value='Не указано')
    theme = forms.CharField(min_length=2, max_length=100, label_suffix=' ',  required=True, label='Тема письма *')
    message = forms.CharField(required=True, label_suffix=' ', widget=forms.Textarea, label='Напишите Ваше сообщение здесь... *')
    
    
class Signup(forms.Form):
    email = forms.EmailField(required=True, label_suffix=' ', label='Email *')