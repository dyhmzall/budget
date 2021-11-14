from django.contrib import admin

from .models import Product, Category, Budget

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Budget)
