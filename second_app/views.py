from django.shortcuts import render, redirect
from .models import * 
from .form import *

# Create your views here.
def form_processing(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            
            return redirect('second_app:homepage')

def homepage(request):
    if request.method == "GET":
        context = {}
        advs = Advantage.objects.all()
        services = Service.objects.all()
        faq = Faq.objects.all()
        context['faq'] = faq
        context['services'] = services
        context['advs'] = advs
        return render(request, 'second_homepage.html', context=context)
    
def contacts_view(request):
    if request.method == "GET":
        context = {}
        form = Contacts()
        context['form'] = form
        return render(request,'contacts.html', context=context)
    if request.method == 'POST':
        form = Contacts(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone_number']
            specialisation = form.cleaned_data['specialisation']
            theme = form.cleaned_data['theme']
            message = form.cleaned_data['message']
            
            # print(f"""{name}\n
            #       {surname}\n
            #       {email}\n
            #       {phone}\n
            #       {specialisation}\n
            #       {theme}\n
            #       {message}\n""")
            return redirect('second_app:homepage')