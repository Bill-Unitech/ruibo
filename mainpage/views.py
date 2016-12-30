from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from .forms import MessageForm
from .models import Message
from django.shortcuts import render

# -*- coding: utf-8 -*-

# Create your views here.
@csrf_protect
def index(request):
    if request.method == "POST":
        send_mail(
            "Greetings, here is a message from a client sent by Ruibo.com",
            "name: "+ request.POST.get("name")+';\n'+
            "mail: " + request.POST.get("email") + ';\n' +
            "message: " + request.POST.get("message") + '.\n' +
            "/n tech support - Unitech - Bill ",
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com', 'rainbowsite0711@126.com'],
            fail_silently=False,
        )
    theform = MessageForm()
    c = {
        'the_form': theform,

    }
    return render(request, './index.html', c)

@csrf_protect
def contact_page(request):

    theform = MessageForm()
    c = {
        'the_form': theform,

    }
    return render(request, './contact_page_2.html', c)

@csrf_protect
def show_cars_1(request):
    if request.method == "POST":
        send_mail(
            'testing django emailing',
            'this message is from: '+ request.POST.get("name")+';\n'+
            "this message is sent by: " + request.POST.get("email") + ';\n' +
            "this message says: " + request.POST.get("message") + '.\n',
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com'],
            fail_silently=False,
        )
    theform = MessageForm()
    c = {
        'the_form': theform,
    }
    print (request)

    return render(request, './show_cars/show_cars_1.html', c)

@csrf_protect
def show_cars_2(request):
    if request.method == "POST":
        send_mail(
            'testing django emailing',
            'this message is from: '+ request.POST.get("name")+';\n'+
            "this message is sent by: " + request.POST.get("email") + ';\n' +
            "this message says: " + request.POST.get("message") + '.\n',
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com'],
            fail_silently=False,
        )
    theform = MessageForm()
    c = {
        'the_form': theform,
    }
    return render(request, './show_cars/show_cars_2.html', c)

@csrf_protect
def show_cars_3(request):
    if request.method == "POST":
        send_mail(
            'testing django emailing',
            'this message is from: '+ request.POST.get("name")+';\n'+
            "this message is sent by: " + request.POST.get("email") + ';\n' +
            "this message says: " + request.POST.get("message") + '.\n',
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com'],
            fail_silently=False,
        )
    theform = MessageForm()
    c = {
        'the_form': theform,
    }
    return render(request, './show_cars/show_cars_3.html', c)

@csrf_protect
def show_cars_4(request):
    if request.method == "POST":
        send_mail(
            'testing django emailing',
            'this message is from: '+ request.POST.get("name")+';\n'+
            "this message is sent by: " + request.POST.get("email") + ';\n' +
            "this message says: " + request.POST.get("message") + '.\n',
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com'],
            fail_silently=False,
        )
    theform = MessageForm()
    c = {
        'the_form': theform,
    }
    return render(request, './show_cars/show_cars_4.html', c)

@csrf_protect
def show_cars_5(request):
    if request.method == "POST":
        send_mail(
            'testing django emailing',
            'this message is from: '+ request.POST.get("name")+';\n'+
            "this message is sent by: " + request.POST.get("email") + ';\n' +
            "this message says: " + request.POST.get("message") + '.\n',
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com'],
            fail_silently=False,
        )
    theform = MessageForm()
    c = {
        'the_form': theform,
    }
    return render(request, './show_cars/show_cars_5.html', c)

@csrf_protect
def show_cars_6(request):
    if request.method == "POST":
        send_mail(
            'testing django emailing',
            'this message is from: '+ request.POST.get("name")+';\n'+
            "this message is sent by: " + request.POST.get("email") + ';\n' +
            "this message says: " + request.POST.get("message") + '.\n',
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com'],
            fail_silently=False,
        )
    theform = MessageForm()
    c = {
        'the_form': theform,
    }
    return render(request, './show_cars/show_cars_6.html', c)

@csrf_protect
def show_cars_7(request):
    if request.method == "POST":
        send_mail(
            'testing django emailing',
            'this message is from: '+ request.POST.get("name")+';\n'+
            "this message is sent by: " + request.POST.get("email") + ';\n' +
            "this message says: " + request.POST.get("message") + '.\n',
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com'],
            fail_silently=False,
        )
    theform = MessageForm()
    c = {
        'the_form': theform,
    }
    return render(request, './show_cars/show_cars_7.html', c)

@csrf_protect
def show_cars_8(request):
    if request.method == "POST":
        send_mail(
            'testing django emailing',
            'this message is from: '+ request.POST.get("name")+';\n'+
            "this message is sent by: " + request.POST.get("email") + ';\n' +
            "this message says: " + request.POST.get("message") + '.\n',
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com'],
            fail_silently=False,
        )
    theform = MessageForm()
    c = {
        'the_form': theform,
    }
    return render(request, './show_cars/show_cars_8.html', c)

@csrf_protect
def show_cars_9(request):
    if request.method == "POST":
        send_mail(
            'testing django emailing',
            'this message is from: '+ request.POST.get("name")+';\n'+
            "this message is sent by: " + request.POST.get("email") + ';\n' +
            "this message says: " + request.POST.get("message") + '.\n',
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com'],
            fail_silently=False,
        )
    theform = MessageForm()
    c = {
        'the_form': theform,
    }
    return render(request, './show_cars/show_cars_9.html', c)

@csrf_protect
def show_cars_10(request):
    if request.method == "POST":
        send_mail(
            'testing django emailing',
            'this message is from: '+ request.POST.get("name")+';\n'+
            "this message is sent by: " + request.POST.get("email") + ';\n' +
            "this message says: " + request.POST.get("message") + '.\n',
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com'],
            fail_silently=False,
        )
    theform = MessageForm()
    c = {
        'the_form': theform,
    }
    return render(request, './show_cars/show_cars_10.html', c)

@csrf_protect
def show_cars_11(request):
    if request.method == "POST":
        send_mail(
            'testing django emailing',
            'this message is from: '+ request.POST.get("name")+';\n'+
            "this message is sent by: " + request.POST.get("email") + ';\n' +
            "this message says: " + request.POST.get("message") + '.\n',
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com'],
            fail_silently=False,
        )
    theform = MessageForm()
    c = {
        'the_form': theform,
    }
    return render(request, './show_cars/show_cars_11.html', c)

@csrf_protect
def show_cars_12(request):
    if request.method == "POST":
        send_mail(
            'testing django emailing',
            'this message is from: '+ request.POST.get("name")+';\n'+
            "this message is sent by: " + request.POST.get("email") + ';\n' +
            "this message says: " + request.POST.get("message") + '.\n',
            settings.EMAIL_HOST_USER,
            ['314046334@qq.com'],
            fail_silently=False,
        )
    theform = MessageForm()
    c = {
        'the_form': theform,
    }
    return render(request, './show_cars/show_cars_12.html', c)

