import os
import stripe
from dotenv import load_dotenv


def data_cleaner(d):
    recurring = None
    metadata = {}
    active = False
    if "active" in d:
        active = d['active']
    if "recurring" in d:
        recurring = d['recurring']
    if "metadata" in d:
        metadata = d['metadata']
    return recurring, metadata, active


class ez_stripe(object):
    def __init__(self):
        load_dotenv()
        stripe.api_key = os.getenv('STRIPE_PUBLIC_KEY')
        self.stripe = stripe
        self.outer_var = 1

    @property
    def price(self):
        return self.Price(self)

    class Price(object):
        def __init__(self, ez):
            self.ez = ez

        def retrieve(self, id):
            context = self.ez.stripe.Price.retrieve(id)
            return context

        def list(self, limit=None):
            if limit != None:
                context = self.ez.stripe.Price.list(limit=limit)
            else:
                context = self.ez.stripe.Price.list()
            return context

    @property
    def product(self):
        return self.Product(self)

    class Product(object):
        def __init__(self, ez):
            self.ez = ez

        def retrieve(self, id):
            context = self.ez.stripe.Product.retrieve(id)
            return context

        def list(self, limit=None):
            if limit != None:
                context = self.ez.stripe.Product.list(limit=limit)
            else:
                context = self.ez.stripe.Product.list()
            return context

        def create(self, d):
            recurring, metadata, active = data_cleaner(d)
            if isinstance(d['unit_amount'], int):
                context = self.ez.stripe.Price.create(
                    active=active,
                    unit_amount=d['unit_amount'],
                    currency="usd",
                    recurring=recurring,

                    product_data={
                        "name": d['name'],
                        "metadata": metadata
                    },
                )
            elif isinstance(d['unit_amount'], list):
                context = []
                product = None
                for u_a in d['unit_amount']:
                    if product == None:
                        nu_product = self.ez.stripe.Price.create(
                            active=active,
                            unit_amount=u_a,
                            currency="usd",
                            recurring=recurring,
                            product_data={
                                "name": d['name'],
                                "metadata": metadata
                            },
                        )
                        context.append(dict(nu_product))
                        product = nu_product['product']
                    else:
                        nu_product = self.ez.stripe.Price.create(
                            active=active,
                            unit_amount=u_a,
                            currency="usd",
                            recurring=recurring,
                            product=product
                        )
                        context.append(dict(nu_product))
            return context

        def modify(self, d):
            context={}
            recurring, metadata, active = data_cleaner(d)
            # context = self.ez.stripe.Product.modify(
            #     d['id'],
            #     active=active,
            #     metadata=metadata,
            #     name=d['name'],
            #     description=d['description'],
            # )



            if "unit_amount" in d:
                if isinstance(d['unit_amount'], int):
                    d['unit_amount']=[d['unit_amount']]
                prices = self.ez.price.list()["data"]
                for s in prices:
                    if s['product'] == d['id']:
                        if s['unit_amount'] in d['unit_amount'] and s['active']:
                            print("IF EXISTS AND ACTIVE")
                        elif s['unit_amount'] in d['unit_amount'] and s['active'] == False:
                            print("IF EXISTS AND NOT ACTIVE")
                            self.ez.stripe.Price.modify(s['id'], active=active)
                        elif s['unit_amount'] not in d['unit_amount'] and s['active'] == True:
                            print("IF NOT EXISTS")
                            self.ez.stripe.Price.modify(s['id'], active=False)
                        else:
                            print(f"ERR!: SU:{s['unit_amount']}, DU:{d['unit_amount']}")
                    
                # IF EXISTS AND ACTIVE
                    # DONT TOUCH
                # IF EXISTS AND NOT ACTIVE
                    #  MAKE ACTIVE
                # IF NOT EXISTS
                    # CREATE
                # REMOVE ANY THAT NOT IN QUERY









            # if "unit_amount" in d:
            #     prices = self.ez.price.list()["data"]
            #     for i in prices:
            #         if i['product'] == d['id']:
            #             if isinstance(d['unit_amount'], int) and i['unit_amount'] != d['unit_amount']:
            #                 context['price'] = self.ez.stripe.Price.create(
            #                     active=active,
            #                     unit_amount=d['unit_amount'],
            #                     currency="usd",
            #                     recurring=recurring,
            #                     product=d['id'])
            #                 stripe.Price.modify(i['id'], active=False)
            #             elif isinstance(d['unit_amount'], list):
            #                 context['price'] = []
            #                 if i['unit_amount'] not in d['unit_amount']:
            #                     self.ez.stripe.Price.modify(
            #                         i['id'], active=False)
            #                 else:
            #                     d['unit_amount'].remove(i['unit_amount'])
            #             for u_a in d['unit_amount']:
            #                 new = self.ez.stripe.Price.create(
            #                     active=active,
            #                     unit_amount=i['unit_amount'],
            #                     currency="usd",
            #                     recurring=recurring,
            #                     product=d['id'])
            #                 context['price'].append(new)
            return context

        def delete(self, id):
            context = self.ez.stripe.Product.delete(id)
            return context
