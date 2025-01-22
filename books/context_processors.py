from .cart import get_cart_count

def cart_count_processor(request):
    cart_count = get_cart_count(request.session)
    return {"cart_count": cart_count}
