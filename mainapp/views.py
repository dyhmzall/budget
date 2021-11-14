from django.shortcuts import render
from django.http import JsonResponse
import datetime

from .models import Product, Category, Budget


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
        'category_id': category_id,
        'message': 'успешно добавлено!'
    }

    current_category = Category.objects.get(id=category_id)

    now = datetime.datetime.now()

    product = Product()
    product.name = name
    product.price = price
    product.category = current_category
    product.month = now.strftime('%m.%Y')
    product.save()

    return JsonResponse(data)


def budget(request):
    months = Budget.objects.all().values('month').distinct()

    content = {
        'months': months
    }

    return render(request, "mainapp/budget.html", content)


def month(request, month=None):
    budget = Budget.objects.filter(month=month)

    products = Product.objects.filter(month=month)

    expenses = {}

    for product in products:

        if not product.category.id in expenses:
            expenses[product.category.id] = 0

        expenses[product.category.id] += product.price

    # return JsonResponse(expenses)

    categories = []

    for category in budget:
        spend = expenses[category.category.id] if category.category.id in expenses else 0

        categories.append({
            'name': category.category.name,
            'amount': category.amount,
            'spend': spend,
            'total': category.amount - spend
        })

    content = {
        'budget': categories,
        'amount': sum(list(map(lambda x: x['amount'], categories))),
        'spend': sum(list(map(lambda x: x['spend'], categories))),
        'total': sum(list(map(lambda x: x['total'], categories))),
        'products': products
    }

    return render(request, "mainapp/month.html", content)
