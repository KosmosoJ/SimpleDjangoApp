from django.db import models
from datetime import datetime


def service_image_path(instance:'Service', filename):
    date_time = datetime.now().strftime("%Y_%m_%d,%H:%M:%S")
    saved_filename = instance.title + '-' + date_time + '.jpg'
    return f'service/{instance.title}/{saved_filename}'

def person_image_path(instance:'Person', filename):
    date_time = datetime.now().strftime("%Y_%m_%d,%H:%M:%S")
    saved_filename = instance.name + '-' + date_time + '.jpg'
    return f'persons/{instance.name}/{saved_filename}'

def carouselitem_image_path(instance:'HomepageCarouselItem', filename):
    date_time = datetime.now().strftime("%Y_%m_%d,%H:%M:%S")
    saved_filename = instance.title + '-' + date_time + '.jpg'
    return f'carousel/{instance.title}/{saved_filename}'

class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    
    title = models.CharField(max_length=100, null=False, blank=True, verbose_name='Заголовок новости')
    description = models.TextField(max_length=500, null=False, blank=True, verbose_name='Описание новости')
    
    def __str__(self) -> str:
        return self.title

class Image(models.Model):
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
    
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    
    def __str__(self) -> str:
        return f'Изображение №{self.pk}'
    

class Person(models.Model):
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        
    name=models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя работника(фио)')
    place = models.CharField(max_length=100, null=False, blank=False, verbose_name='Должность')
    person_image = models.ImageField(upload_to=person_image_path, default='persons/default/default.png') # type: ignore
    
    def __str__(self) -> str:
        return f'{self.name} - {self.place}'

    
class HomepageCarouselItem(models.Model):
    class Meta:
        verbose_name = 'Карусель'
        verbose_name_plural = 'Карусели'
    
    title = models.CharField(max_length=100, null=False, blank=True, default='Главная надпись на каруселе',verbose_name='Главная надпись на каруселе')
    description = models.CharField(max_length=100, null=False, blank=True, default='Краткое описание карусели', verbose_name='Краткое описание карусели')
    image = models.ImageField(upload_to=carouselitem_image_path, default='carousel/default/default.png', verbose_name='Изображение') # type: ignore
    news = models.ForeignKey(News, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Новость')
    
    def __str__(self) -> str:
        return self.title
    
class Service(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название услуги')
    short_descr = models.CharField(max_length=100, default='Empty', null=False, blank=False, verbose_name='Краткое описание услуги')
    descr = models.TextField(null=False, blank=False,default='Empty', verbose_name='Описание услуги')
    # images = models.ManyToManyField(Image, default=None, verbose_name='Изображение проекта')
    
    def __str__(self) -> str:
        return self.title
        
    
class Project(models.Model):
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
    
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название проекта')
    full_descr = models.TextField(null=True, blank=True, default=None, verbose_name='Полное описание проекта')
    short_descr = models.CharField(max_length=100, default='Empty', null=False, blank=False, verbose_name='Краткое описание проекта')
    descr = models.TextField(null=False, blank=False, default='Empty',verbose_name='Описание проекта')
    images = models.ManyToManyField(Image, default=None, verbose_name='Изображение проекта')
    service = models.ForeignKey(Service, null=True, on_delete=models.PROTECT, verbose_name='Услуга', related_name = 'projects')
    
    def __str__(self) -> str:
        return self.title