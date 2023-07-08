from django import forms
from django.core.validators import RegexValidator

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True
    required=False
    


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result



class Request(forms.Form):
    first_name = forms.CharField(min_length=2, max_length=30, required=False, label='Имя', empty_value='Не указано')
    last_name = forms.CharField(min_length=2, max_length=30, required=False, label='Фамилия', empty_value='Не указано')
    email = forms.EmailField(min_length=2, required=True, label='Эл. почта*')
    
    phone_regex = RegexValidator(regex=r'^\+?7?\d{10}$', message='Введите номер телефона')
    phone_number = forms.CharField(validators=[phone_regex], min_length=10, max_length=12,  label='Номер телефона*', required=True, error_messages={'required':'Необходимо ввести номер телефона'})
    message = forms.CharField(required=False, widget=forms.Textarea, label='Оставьте сообщение...', empty_value='Не указано')
    
choices = [
    ('','Выберите категорию'),
    (1,'Строительство'),
    (2,'Ремонт'),
    (3,'Охрана'),
    (4,'Корпуса/Упаковка'),
    (5, 'Охота/Рыбалка'),
    (6,'Путешествия'),
    (7,'Решения для аудио/Видео'),
    (8,'Кухня'),
    (9,'Для бизнеса'),
    (10,'Другое...')
]
    
checkbox_choices = [
    (1,'Нужна сборка'),
    (2,'Нужна покраска'),
    (3,'Нужна жесткая упаковка')
]
    
class AdvancedRequest(forms.Form):
    first_name = forms.CharField(min_length=2, max_length=30, required=True, label='Имя*', label_suffix=' ', empty_value='Не указано')
    last_name = forms.CharField(min_length=2, max_length=30, required=True, label='Фамилия*', label_suffix=' ', empty_value='Не указано')
    email = forms.EmailField(min_length=2, required=True, label_suffix=' ', label='Эл. почта*')
    phone_regex = RegexValidator(regex=r'^\+?7?\d{10}$', message='Введите номер телефона')
    phone_number = forms.CharField(validators=[phone_regex], min_length=10, max_length=12, label_suffix=' ',  label='Номер телефона*', required=True, error_messages={'required':'Необходимо ввести номер телефона'})
    message = forms.CharField(required=False, widget=forms.Textarea, label='Оставьте сообщение...', empty_value='Не указано')
    category = forms.ChoiceField(choices=choices, label='Категория*', label_suffix=' ', required=True)
    file = MultipleFileField(label='Загрузка файла', label_suffix=' ', required=False)
    
    
class NewsForm(forms.Form):
        
    first_name = forms.CharField(min_length=2, max_length=30, required=True, label='Имя *', label_suffix=' ', empty_value='Не указано')
    last_name = forms.CharField(min_length=2, max_length=30, required=True, label='Фамилия *', label_suffix=' ', empty_value='Не указано')
    email = forms.EmailField(min_length=2, required=True, label_suffix=' ', label='Эл. почта *')
    phone_regex = RegexValidator(regex=r'^\+?7?\d{10}$', message='Введите номер телефона')
    phone_number = forms.CharField(validators=[phone_regex], min_length=10, max_length=12, label_suffix=' ',  label='Телефон *', required=True, error_messages={'required':'Необходимо ввести номер телефона'})
    category = forms.ChoiceField(choices=choices, label='Категория *', label_suffix=' ', required=True)
    name = forms.CharField(min_length=2, max_length=50, required=True, label='Название товара *', label_suffix=' ')
    material = forms.CharField(min_length=2, max_length=100, required=True, label='Материал товара *', label_suffix=' ')
    size = forms.CharField(min_length=2, max_length=100, required=True, label='Габаритные размеры *', label_suffix=' ')
    quantity = forms.IntegerField(min_value=0,required=True, label='Количество *', label_suffix=' ')
    conditions = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=checkbox_choices, label='Условия', label_suffix=' ', error_messages={'conditions':'Условия - Необходимо выбрать условие'})
    message = forms.CharField(required=False, widget=forms.Textarea, label='Ваше предложение', empty_value='Не указано')
    
    file = MultipleFileField(label='Если есть, здесь Вы можете отправить нам эксизы/чертежи/3D модели', label_suffix=' ', required=False)
    
    
    
