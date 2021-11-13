from django.conf import settings
from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse

from .models import Product, Category


def main(request):
    categories = Category.objects.all()

    content = {
        'title': 'Бюджет',
        'categories': categories
    }

    return render(request, "mainapp/empty.html", content)


def bay(request):
    name = request.POST.get('name', '')
    price = request.POST.get('price', 0)
    category_id = request.POST.get('category_id', 0)

    data = {
        'name': name,
        'price': price,
        'category_id': category_id
    }

    current_category = Category.objects.get(id=category_id)

    product = Product()
    product.name = name
    product.price = price
    product.category = current_category
    product.save()

    return JsonResponse(data)
