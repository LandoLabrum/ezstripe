class Customer(object):
    def __init__(self, ez):
        self.ez = ez

    def create(self, d):
        context = self.ez.stripe.Customer.create(
            address=d['address'],
            description=d['description'],
            email=d['email'],
            metadata=['metadata'],
            name=['name'],
            payment_method=['payment_method'],
            phone=['phone']
        )
        return context

    def retrieve(self, id):
        context = self.ez.stripe.Customer.retrieve(id)
        return context
    
    def modify(self, d):
        context = self.ez.stripe.Customer.modify(
            d['id'],
            address=d['address'],
            description=d['description'],
            email=d['email'],
            metadata=d['metadata'],
            name=d['name'],
            phone=d['phone'],
        ) 
        return context

    def delete(self, id):
        context = self.ez.stripe.Customer.delete(id)
        return context

    def list(self, limit=None, email=None):
        if email != None:
            context = self.ez.stripe.Customer.list(limit=limit, email=email)
        else:
            context = self.ez.stripe.Customer.list(limit=limit)
        return context