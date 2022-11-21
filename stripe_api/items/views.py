import os
import stripe

from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Item

stripe.api_key = os.getenv('STRIPE_KEY')


def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item_price = item.price
    item_description = item.description

    context = {
        'item': item,
        'item_price': item_price,
        'item_description': item_description,
    }

    return render(request, 'items/items_detail.html', context)


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)