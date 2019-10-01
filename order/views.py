from django.shortcuts import render
from django.views.decorators.http import require_POST

from cart.cart import Cart
from .models import buyerdata
def OrderPage(request):
    cart = Cart(request)
    return render(request,'order/orderr.html', {'cart' : cart})

@require_POST
def createpost(request):
    if request.method == 'POST':
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('address'):
            post = buyerdata()
            post.first_name = request.POST.get('first_name')
            post.last_name = request.POST.get('last_name')
            post.address = request.POST.get('address')
            post.save()

            return render(request, 'order/response.html')
        else:
            return render(request, 'order/error.html')
    else:
        return render(request, 'order/orderr.html')