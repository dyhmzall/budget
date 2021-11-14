from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="имя", max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="имя", max_length=128)
    price = models.DecimalField(verbose_name="цена", max_digits=8, decimal_places=2, default=0)
    description = models.TextField(verbose_name="описание продукта", blank=True)

    def __str__(self):
        return self.name


class Budget(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    month = models.CharField(verbose_name="месяц", max_length=128)
    amount = models.DecimalField(verbose_name="сумма", max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"[{self.category.name}] ({self.month}) {self.amount}"
