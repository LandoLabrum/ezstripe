import os
import stripe
from dotenv import load_dotenv
from .product import Product
from .price import Price
from .customer import Customer 

class ez_stripe(object):
    def __init__(self):
        load_dotenv()
        stripe.api_key = os.getenv('STRIPE_PUBLIC_KEY')
        self.stripe = stripe
        self.outer_var = 1

    @property
    def price(self):
        return Price(self)

    @property
    def product(self):
        return Product(self)

    @property
    def customer(self):
        return Customer(self)