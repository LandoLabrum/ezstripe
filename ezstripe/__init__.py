import os
import stripe
from dotenv import load_dotenv
from .product import Product
from .price import Price
from .customer import Customer
from .method import Method
from .session import Session
from .invoice import Invoice
from .subscription import Subscription

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

    @property
    def method(self):
        return Method(self)

    @property
    def session(self):
        return Session(self)

    @property
    def invoice(self):
        return Invoice(self)

    @property
    def subscription(self):
        return Subscription(self)
