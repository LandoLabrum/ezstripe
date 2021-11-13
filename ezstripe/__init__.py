import os
import stripe
from dotenv import load_dotenv


# class ez_stripe:
#     def __init__(self):
#         load_dotenv()
#         stripe.api_key = os.getenv('STRIPE_PUBLIC_KEY')
#         self.stripe = stripe
#         self.context = {}

#     class product:
#         def __init__(self):
#             ## instantiating the 'list' class
#             self = self

#         def list(self, limit=None):
#             # if limit == None:
#             #     self.context=self.stripe.Product.list(limit=limit)
#             #     return self.context
#             # self.context=self.stripe.Product.list()
#             return self.context


class ez_stripe(object):
    def __init__(self):
        load_dotenv()
        stripe.api_key = os.getenv('STRIPE_PUBLIC_KEY')
        self.stripe = stripe
        self.outer_var = 1

    @property
    def product(self):
        return self.Product(self)

    class Product(object):
        def __init__(self, ez):
            self.ez = ez

        def list(self, limit=None):
            if limit != None:
                context = self.ez.stripe.Product.list(limit=limit)
            else:
                context = self.ez.stripe.Product.list()
            return context
        def create(self, data):
            d=data
            recurring=None
            metadata=None
            if 
            if "recurring" in d:
                recurring=d['recurring']
            if "metadata" in d:
                metadata=d['metadata']
            context = self.ez.stripe.Price.create(
                unit_amount=d['unit_amount'],
                currency="usd",
                recurring=recurring,
                metadata=metadata,
                product_data={
                    "name":d['name']
                },
            )
            return context
