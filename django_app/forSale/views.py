"""
For Django and Stripe to connect, we need to override
the Django get_context_data() to grab the Stripe
publishable key from the ../app/settings.py

In the .html file:
the data-key="{{ key }}" is where we referece the context['key']
and pass the STRIPE_PUBLISHABLE_KEY from /settings.py
    (so we can name this variable "key" whatever, just make sure it's consistent obiously)



On charge_through_stripe():

    * amount is without decimals
    * currency is also explicit

    * description will be displayed in the Stripe dashboard/json file
        so (so most likely) necessary to have it custom to the product


"""

import stripe
#we access the settings file with this import
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render

from .models import ItemsForSale


# grabbing secret key from settings.py
stripe.api_key = settings.STRIPE_SECRET_KEY


def ForSalePage(request):
    context = {
        'items': ItemsForSale.objects.all(),
        'key': settings.STRIPE_PUBLISHABLE_KEY,
        }
    return render(request, 'forSale/sale_page.html', context)


def charge_through_stripe(request):
    if request.method == 'POST':
        charged = stripe.Charge.create(
            amount= request.POST['data-amount'],
            currency='usd',
            description='Charge through Django with Stripe API',
            source=request.POST['stripeToken']
        )
        return render(request, 'forSale/charge_sucessful.html')


        # set dollar amount
def charge_10_through_stripe(request):
    if request.method == 'POST':
        charged = stripe.Charge.create(
            amount=1000,
            currency='usd',
            description='Charge through Django with Stripe API',
            source=request.POST['stripeToken']
        )
        return render(request, 'forSale/charge_sucessful.html')
