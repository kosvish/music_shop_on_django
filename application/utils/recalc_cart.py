from django.db import models


# Функция которая принимает корзину как объект дабы её пересчитать

def recalc_cart(cart):
    # Агрегация всех товаров, подсчитав их сумму и id
    cart_data = cart.products.aggregate(models.Sum('final_price'), models.Count('id'))
    # Смотрю поменялась ли сумма , если да, то присвоил её в final_price
    if cart_data.get('final_price__sum'):
        cart.final_price = cart_data['final_price__sum']
    else:
        cart.final_price = 0
    cart.total_products = cart_data['id__count']
    cart.save()


