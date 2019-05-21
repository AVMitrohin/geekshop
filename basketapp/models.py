from django.db import models
from django.conf import settings
from mainapp.models import Product


# class BasketQuerySet(models.QuerySet):
#     pass
#
#     def delete(self, *args, **kwargs):
#         for object in self:
#             object.product.quantity += object.quantity
#             object.product.save()
#
#         super().delete(*args, **kwargs)


class Basket(models.Model):
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
    # objects = BasketQuerySet.as_manager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=1)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    @property
    def product_cost(self):
        "return cost of all products this type"
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        "return total quantity for user"
        items = Basket.objects.filter(user=self.user)
        total_quantity = sum(list(map(lambda x: x.quantity, items)))
        return total_quantity

    @property
    def total_cost(self):
        "return total cost for user"
        items = Basket.objects.filter(user=self.user)
        total_cost = sum(list(map(lambda x: x.product_cost, items)))
        return total_cost

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - Basket.get_item(self.pk).quantity
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username + ' ' + self.product.name

    # def delete(self):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super().delete()
