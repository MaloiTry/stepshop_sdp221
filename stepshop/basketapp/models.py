from django.db import models
from mainapp.models import Product
from stepshop import settings


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='пользователь',
        on_delete=models.CASCADE,
        related_name='basket',
    )

    product = models.ForeignKey(
        Product,
        verbose_name='продукт',
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )

    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.user.username} - {self.product.name} ({self.quantity} шт.)'

    @property
    def product_cost(self):
        return self.product.price * self.quantity    \


    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity

    @property
    def total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.product_cost, _items)))
        return _total_cost

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
