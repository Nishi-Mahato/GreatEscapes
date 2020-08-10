from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from cart.forms import CartAddProductForm
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render


def home(request):
    return render(request, 'tms/home.html',
                  {'tms': home})


def register(request):
    print("entered into register view method")
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,
                          'registration/registerdone.html',
                          {'form': form})
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    print("categories: " + str(categories))
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  'tms/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'tms/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        send_mail(
            message_name,
            message,
            message_email,
            ['jcui@unomaha.edu'],
            )

        return render(request,'tms/contact.html', {'message_name':message_name})
    else:
        return render(request, 'tms/contact.html', {})
