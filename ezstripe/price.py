class Price(object):
    def __init__(self, ez):
        self.ez = ez

    def retrieve(self, id):
        context = self.ez.stripe.Price.retrieve(id)
        return context

    def list(self, limit=None, active=None):
        context = self.ez.stripe.Price.list(limit=limit, active=active)
        return context
    
    def create(self, d):
        context=self.ez.stripe.Price.create(
            active=d['active'],
            unit_amount=d['unit_amount'],
            currency="usd",
            recurring=d['recurring'],
            product=d['product'],
        )
        return context