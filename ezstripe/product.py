def data_cleaner(d):
    recurring = None
    metadata = None
    active = False
    if "active" in d:
        active = d['active']
    if "recurring" in d:
        recurring = d['recurring']
    if "metadata" in d:
        metadata = d['metadata']
    return recurring, metadata, active

class Product(object):
    def __init__(self, ez):
        self.ez = ez

    def retrieve(self, id, active=None):
        context = self.ez.stripe.Product.retrieve(id)
        context['price']=[]
        prices = self.ez.price.list(active=active)["data"]
        for s in prices:
            if s['product'] == id:
                context['price'].append(s)
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
        context = self.ez.stripe.Product.modify(
            d['id'],
            active=active,
            metadata=metadata,
            name=d['name'],
            description=d['description'],
        )
        # print(f"79: \t {context}")
        if "unit_amount" in d:
            context['price']=[]
            u_a=d['unit_amount']
            if isinstance(u_a, int):
                u_a=[u_a]
            prices = self.ez.price.list()["data"]
            for s in prices:
                if s['product'] == d['id']:
                    if s['unit_amount'] in u_a and s['active']:
                        # print(f"{s['unit_amount']}, EXISTS AND ACTIVE")
                        u_a.remove(s['unit_amount'])
                        # context['price'].append()
                    elif s['unit_amount'] in u_a and s['active'] == False:
                        # print(f"{s['unit_amount']}, IF EXISTS AND NOT ACTIVE")
                        self.ez.stripe.Price.modify(s['id'], active=active)
                        u_a.remove(s['unit_amount'])
                    elif s['unit_amount'] not in u_a and s['active'] == True:
                        # print(f"{s['unit_amount']}, NOT IN NEW, ARCHIVE")
                        self.ez.stripe.Price.modify(s['id'], active=False)
                    # else:
                    #     print(f"ERR!: SU:{s['unit_amount']}, DU:{u_a}")
            if len(u_a) >= 1:
                
                for n in u_a:
                    created = self.ez.price.create({
                            "active":active,
                            "unit_amount":n,
                            "recurring":recurring,
                            "product":d['id'],
                        })
                    context['price'].append(dict(created))
            return context
