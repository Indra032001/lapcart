from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import cartForm
from .models import Laptop


@login_required(login_url="/auth/login/")
def show_view(request):
    template_name = "lapcartAPP/show.html"
    product = Laptop.objects.all()
    context = {'product': product}
    return render(request, template_name, context)


def add_view(request):
    if request.method == "GET":
        template_name = "lapcartAPP/add.html"
        form = cartForm()
        context = {'form': form}
        return render(request, template_name, context)
    elif request.method == "POST":
        filled_form = cartForm(request.POST, request.FILES)
        if filled_form.is_valid():
            filled_form.save()
            return redirect("/cart/show/")


def update_view(request, i):
    if request.method == "GET":
        template_name = "lapcartAPP/add.html"
        product = Laptop.objects.get(id=i)
        form = cartForm(instance=product)
        context = {'form': form}
        return render(request, template_name, context)
    elif request.method == "POST":
        product = Laptop.objects.get(id=i)
        filled_form = cartForm(request.POST, instance=product)
        if filled_form.is_valid():
            filled_form.save()
            return redirect("/cart/show/")


def delete_view(request, i):
    product = Laptop.objects.get(id=i)
    product.delete()
    return redirect("/cart/show/")
