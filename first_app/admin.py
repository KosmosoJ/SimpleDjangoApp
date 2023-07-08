from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import * 
# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ['preview']
    
    def preview(self, obj):
        preview_template = '<img src="{0}" title="{1}">'
        preview_str = ''
        all_images = obj.images.all()
        image_list = []
        for i_image in all_images:
            preview_str += preview_template.format(i_image.image.url, i_image) + ','
        return mark_safe(f'{preview_str}')
    
    preview.short_description = 'Изображение'

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['preview']
    
    
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}">')
    
    preview.short_description = 'Изображение'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ['preview']
    
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.person_image.url}">')

    preview.short_description = 'Изображение'
    
    
@admin.register(HomepageCarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    readonly_fields = ['preview']
    
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}">')

    preview.short_description = 'Изображение'

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass