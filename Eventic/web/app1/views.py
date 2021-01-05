from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .form import ContactData
from django.contrib.auth.hashers import make_password
from .models import Register, CreateEvent


def eventdetails(request):
    con = CreateEvent.objects.all()
    return render(request, 'app1/eventdetails.html' ,{'con':con})


def index1(request):
    con = CreateEvent.objects.all()
    # if request.method == "POST":
    #     Contact.objects.create(name=request.POST.get('name'), email=request.POST.get('email'),
    #                            msg=request.POST.get('message'))
    #     return redirect('/register')

    return render(request, 'app1/hompageslide01.html', {'con':con})


def sign_in(request):
    con = Register.objects.all()
    if request.method == "POST":
        lemail = request.POST.get('email')
        lpwd = request.POST.get('pwd')
        for k in con:
            if k.pwd == lpwd and k.email == lemail:
                return redirect('/eventdetails')

    return render(request, 'app1/sign_in.html')


def registration(request):
    if request.method == "POST":
        Register.objects.create(category=request.POST.get('category'),phone=request.POST.get('phone'),cms_id=request.POST.get('cms_id'),name=request.POST.get('name'), email=request.POST.get('email'),pwd=request.POST.get('pwd'))
        return redirect('/')

    return render(request, 'app1/registration.html')


def createEvent(request):
    if request.method == "POST":
        CreateEvent.objects.create(event_title=request.POST.get('event_name'), event_head=request.POST.get('event_head'), phone=request.POST.get('phone'), date=request.POST.get('date'), s_time=request.POST.get('s_time'), e_time=request.POST.get('e_time'),event_desc=request.POST.get('desc'),event_type=request.POST.get('event_type'),event_price=request.POST.get('event_price'),event_value=request.POST.get('value'))
        return redirect('/eventdetails')

    return render(request, 'app1/eventcreation.html')
