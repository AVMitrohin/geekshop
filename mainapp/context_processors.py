from basketapp.models import Basket


def basket(request):
    print(f'context processors works')

    if request.user.is_authenticated:
        basket = request.user.basket.all()

        return {
            'basket': basket,
        }
    else:
        return {
            'basket': []
        }
