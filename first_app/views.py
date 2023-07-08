from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from .models import *
from .form import Request, AdvancedRequest, choices, NewsForm, checkbox_choices
from datetime import datetime
import os 

from .utils import send_email
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail, EmailMessage
from django.conf import settings



# Create your views here.    





# def base(request):
#     categories = Category.objects.all().prefetch_related('services').all()
#     return render(request, 'base.html', context={'categories':categories})




def homepage(request, message=None):
    """ Рендер главной страницы 
    
        При успешной валидации данных в форме - будет отправлять письмо на эл. почту
        Иначе, ничего не происходит 
        
    """
    context = {}
            
    if request.method == 'GET':
        form = Request()
        try:
            if request.session['message']:                
                context['success_message'] = request.session['message']
                del request.session['message']
                request.session.modifed = True
        except:
            pass
            
        services = Service.objects.exclude(title='Вакуумная формовка').all()
        vacuum = Service.objects.filter(title='Вакуумная формовка')
        images = Image.objects.all()
        context['images'] = images
        context['vacuum'] = vacuum
        context['services'] = services
        context['form'] = form     
        persons = Person.objects.all()
        carousel_items = HomepageCarouselItem.objects.all()
        context['persons'] = persons
        context['carousel'] = carousel_items
        
        return render(request, 'homepage.html', context=context)
    
    if request.method == 'POST':
        form = Request(request.POST)

        if form.is_valid():    
            first_name = form.cleaned_data['first_name'] 
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
                
            email_content = f'Заявка от пользователя:\nИмя: {first_name}\nФамилия: {last_name}\nЭл.почта: {email}\nНомер телефона: {phone_number}\nСообщение: {message}\nОт {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}\n\n'
            
            send_email(subject='Краткая форма', email_content=email_content, files=[])
            
            success_message = 'Заявка отправлена, спасибо'
            request.session['message'] = success_message
    
            return redirect('first_app:homepage')
        else:
            success_message = 'Пожалуйста, проверьте правильность ввода данных.'
            request.session['message'] = success_message
            
            return redirect('first_app:homepage')
                    
def news_view(request, pk):
    if request.method == 'GET':
        news = News.objects.filter(pk=pk).first()
        context = {}
        
        try:
            if request.session['adv_message']:                
                context['adv_success_message'] = request.session['adv_message']
                del request.session['adv_message']
                request.session.modifed = True
        except:
            pass    
        
        form = NewsForm()
        context['form'] = form
        context['news'] = news
        return render(request,'news.html', context=context)
    
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            
            first_name = form.cleaned_data['first_name'] 
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            category = form.cleaned_data['category']
            name = form.cleaned_data['name']
            material = form.cleaned_data['material']
            size = form.cleaned_data['size']
            quantity = form.cleaned_data['quantity']
            conditions = form.cleaned_data['conditions']
            message = form.cleaned_data['message']
            
            file = request.FILES.getlist('file')
            
            uploaded = []
            
            try:
                if len(file) > 0:
                    fs = FileSystemStorage()
                    for f in file:
                        filename = fs.save(f.name.replace(' ','_'), f)
                        uploaded.append(fs.url(filename))
            except Exception as ex:
                pass
            condition_list = []
            if conditions:
                for condition in conditions:
                    for checkbox in checkbox_choices:
                        if str(checkbox[0]) == condition:
                            condition_list.append(checkbox[1])
            else:
                condition_list = 'Не указано'
                
            email_content = f"""Клиент {first_name} {last_name}
Номер телефона: {phone_number}
Email: {email}\n
Категория: {category}
Название товара: {name}
Материал: {material}
Габариты: {size}
Количество: {quantity}
Условия: {condition_list}\n
Сообщение: {message}\n
От {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}"""
            
            send_email('Новостная форма', email_content=email_content, files=uploaded)
            
            
            success_message = 'Заявка отправлена, спасибо'
            request.session['adv_message'] = success_message
            return redirect('first_app:news', pk)
        else:            
            request.session['adv_message'] = form.errors
            
            return redirect('first_app:news', pk)
        
    
    
    
def advanced_form(request):
    context = {}
    if request.method == 'GET':
        adv_form = AdvancedRequest()
        
        try:
            if request.session['adv_message']:                
                context['adv_success_message'] = request.session['adv_message']
                del request.session['adv_message']
                request.session.modifed = True
        except:
            pass
        
        images = Image.objects.all()
        context['images'] = images
        context['form'] = adv_form
        return render(request,'request.html', context=context)
    
    if request.method == 'POST':
        adv_form = AdvancedRequest(request.POST, request.FILES)
        
        if adv_form.is_valid():
            name = adv_form.cleaned_data['first_name']
            last_name = adv_form.cleaned_data['last_name']
            phone_number = adv_form.cleaned_data['phone_number']
            email = adv_form.cleaned_data['email']
            message = adv_form.cleaned_data['message']
            category = adv_form.cleaned_data['category']
            file = request.FILES.getlist('file')
            
            uploaded = []
            try:
                if len(file) > 0:
                    fs = FileSystemStorage()
                    for f in file:
                        filename = fs.save(f.name.replace(' ','_'), f)
                        uploaded.append(fs.url(filename))
            except Exception as ex:
                pass
            
            
            for choice in choices:
                if str(choice[0]) == category:
                    category = choice[1]
                    
            email_content = f'Клиент {name} {last_name}\nНомер телефона: {phone_number}\nEmail: {email}\nКатегория: {category}\nСообщение: {message}\nОт {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}'
            
            # email_message = EmailMessage(
            #     subject='Расширенная форма',
            #     body=email_content,
            #     from_email='settings.EMAIL_HOST_USER',
            #     to=['xiwob79606@aramask.com'],
            # )
            
            # BASE_DIR = settings.BASE_DIR
            
            # if uploaded:
            #     for f in uploaded:
            #         path = f'{BASE_DIR}/{f}'
            #         email_message.attach_file(path)
            #         os.remove(path)
            
            # email_message.send(fail_silently=False)
            
            send_email('Расширенная форма', email_content=email_content, files=uploaded)
            
            
            success_message = 'Заявка отправлена, спасибо'
            request.session['adv_message'] = success_message

            return redirect('first_app:adv_form')

            
    
def service_list(request):
    if request.method == 'GET':
        service_list = Service.objects.all()
        
        return render(request, 'service_list.html', context={'service_list':service_list})
    

    
def about_us(request):
    if request.method == 'GET':
        return render(request, 'about_us.html')
    
def your_ideas(request):
    if request.method == 'GET':
        return render(request, 'your_ideas.html')
    
def project_detail(request, pk):
    if request.method == 'GET':
        project = Project.objects.filter(pk=pk).first()
        return render(request, 'project_detail.html', {'project':project})
    

    