from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


def signup_view(request):
    reg_form = UserCreationForm()
    if request.method == 'POST':
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('/auth/login/')
    template_name = 'authAPP/signup.html'
    context = {'reg_form': reg_form}
    return render(request, template_name, context)


def login_view(request):
    if request.method == "POST":
        u = request.POST["un"]
        p = request.POST["pw"]
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('/cart/show/')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credintial')

    template_name = 'authAPP/login.html'
    context = {}
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('/auth/login/')
