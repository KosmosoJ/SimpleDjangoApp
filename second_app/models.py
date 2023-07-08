from django.db import models
from datetime import datetime
# Create your models here.

def logo_image_path(instance:'Service', filename):
    date_time = datetime.now().strftime("%Y_%m_%d,%H:%M:%S")
    saved_filename = instance.title + '-' + date_time + '.jpg'.replace(' ', '_')
    return f'service/{instance.title}/logo/{saved_filename}'

def service_image_path(instance:'Service', filename):
    date_time = datetime.now().strftime("%Y_%m_%d,%H:%M:%S")
    saved_filename = instance.title + '-' + date_time + '.jpg'.replace(' ', '_')
    return f'service/{instance.title.replace(" ", "_")}/image/{saved_filename}'

class Svg(models.Model):
    class Meta:
        verbose_name = 'Иконка'
        verbose_name_plural = 'Иконки'
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название')
    logo = models.FileField(upload_to='svgs/', verbose_name='иконка')
    
    def __str__(self) -> str:
        return self.title


    
class Service(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
    
    title = models.CharField(max_length=100, null=False, blank=True, default='Услуга', verbose_name='Название услуги')
    second_title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Название в верху')
    logo = models.ForeignKey(Svg, on_delete=models.PROTECT, verbose_name='Иконка')
    description = models.TextField(null=False, blank=True, default='Описание', verbose_name='Описание услуги')
    image = models.ImageField(upload_to=service_image_path, null=True, blank=True, default='media/images/default.png', verbose_name='Изображение услуги')
    
    
    def __str__(self) -> str:
        return self.title
    
    
class Advantage(models.Model):
    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        
    logo = models.ForeignKey(Svg, on_delete= models.PROTECT, verbose_name='Икона')    
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Заголовок')
    descr = models.TextField(max_length=200, null=False, blank=True, verbose_name='Описание')
    
    def __str__(self) -> str:
        return self.title
    
    
class Faq(models.Model):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        
    question = models.CharField(max_length=100, null=False, blank=True, default='Вопрос', verbose_name='Вопрос')
    answer = models.TextField(max_length=1000, null=False, blank=True, default='Ответ', verbose_name='Ответ')
    
    def __str__(self) -> str:
        return self.question
        
        
class SocialMedia(models.Model):
    class Meta:
        verbose_name = 'Соцсеть'
        verbose_name_plural = 'Соцсети'
        
    title = models.CharField(max_length=100, null=False, blank=True, verbose_name='Название')
    url = models.URLField(null=False, blank=True, verbose_name='Ссылка')
    
    def __str__(self) -> str:
        return self.title