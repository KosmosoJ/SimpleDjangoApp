from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import * 

app_name = 'second_app'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('contacts/', contacts_view, name='contacts'),
    path('form/', form_processing, name='form_processing')
]
