from django import template

register = template.Library()


@register.filter
def basket_total_cost(user):
    if user.is_anonymous:
        return 0
    else:
        items = user.basket.all()
        total_cost = sum(list(map(lambda x: x.product_cost, items)))
        return total_cost
