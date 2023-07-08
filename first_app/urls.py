from django.urls import path
from .views import * 
from django.conf.urls.static import static
from django.conf import settings

app_name = 'first_app'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('services/', service_list, name='services'),
    # path('projects/', project_list, name='projects'),
    path('project/<int:pk>', project_detail, name='project'),
    path('contacts/', about_us, name='about_us'),
    path('request/', advanced_form, name='adv_form'),
    path('news/<int:pk>', news_view, name='news'),
    
]
