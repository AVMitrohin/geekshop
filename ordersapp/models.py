from django.conf import settings
from django.db import models

from mainapp.models import Product


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNL'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен в обработку'),
        (PROCEEDED, 'обрабатывается'),
        (PAID, 'оплачен'),
        (READY, 'готов'),
        (CANCEL, 'отменён'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлён', auto_now=True)
    status = models.CharField(verbose_name='статус', max_length=3, choices=ORDER_STATUS_CHOICES, default=FORMING)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Текущий заказ: {self.pk}'

    def get_total_quantity(self):
        items = self.orderitems.values_list('quantity', flat=True)
        return sum(items)

    def get_product_type_quantity(self):
        return self.orderitems.count()

    def get_total_cost(self):
        items = self.orderitems.select_related('product')
        return sum([el.quantity * el.product.price for el in items])

    def delete(self):
        for item in self.orderitems.all():
            item.product.quantity += item.quantity
            item.product.save()

        self.is_active = False
        self.save()


# class OrderItemQuerySet(models.QuerySet):
#
#     def delete(self, *args, **kwargs):
#         for object in self:
#             object.product.quantity += object.quantity
#             object.product.save()
#         super().delete(*args, **kwargs)


class OrderItem(models.Model):
    # objects = OrderItemQuerySet.as_manager()
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)

    def get_product_cost(self):
        return self.product.price * self.quantity

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.filter(pk=pk).first()

    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - OrderItem.get_item(self.pk).quantity
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super().save(*args, **kwargs)
    #
    # def delete(self):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super().delete()
