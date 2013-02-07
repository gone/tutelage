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

def bill_pledge(pledge):
    customer_id = pledge.user.customer.customer_id
    amount = int(pledge.amount) * 100 #convert to cents
    stripe.Charge.create(
        amount=amount,
        currency="usd",
        customer=customer_id,
    )
