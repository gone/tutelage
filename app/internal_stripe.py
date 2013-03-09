import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API

def create_customer(user, token_id):
    customer = stripe.Customer.create(
        card=token_id,
        description=user.email,
    )
    return customer

def purchase_lesson(user, lesson):
    customer_id = user.customer.customer_id
    amount = int(lesson.price) * 100 #convert to cents
    #TODO: save the receipt
    stripe.Charge.create(
        amount=amount,
        currency="usd",
        customer=customer_id,
    )


def bill_pledge(pledge):
    customer_id = pledge.user.customer.customer_id
    amount = int(pledge.amount) * 100 #convert to cents
    #TODO: save the receipt
    stripe.Charge.create(
        amount=amount,
        currency="usd",
        customer=customer_id,
    )
