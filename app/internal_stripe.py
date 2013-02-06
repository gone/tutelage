import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API

def create_customer(user, token_id):
    import pdb
    pdb.set_trace()
    customer = stripe.Customer.create(
        card=token_id,
        description=user.email,
    )
    return customer
