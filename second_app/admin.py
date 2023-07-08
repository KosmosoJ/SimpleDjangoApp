from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass 

@admin.register(Svg)
class SvgAdmin(admin.ModelAdmin):
    pass

@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    pass

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    pass

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    pass
    
    
