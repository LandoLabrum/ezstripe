import json

class Customer(object):
    def __init__(self, ez):
        self.ez = ez

    def create(self, data):
        all=self.list(email=data['email'])
        if all == '[]':
            metadata = None
            if "metadata" in data:
                metadata = data['metadata']
            context = self.ez.stripe.Customer.create(
                name=data['name'],
                email=data['email'],
                phone=data['phone'],
                address=data['address'],
                description=data['description'],
                metadata=metadata,
            )
            return context
        else:
            context={"error":{"code":409,"msg":"Customer with this email exists"}}
            return context

    def retrieve(self, customer_id=None, email=None):
        if email == None:
            context = self.ez.stripe.Customer.retrieve(customer_id)
        else:
            context = self.list(email=email)
        return context

    def modify(self, customer_id=None, data=None):
        customer = self.retrieve(customer_id=customer_id)
        for i in customer:
            if i not in data:
                globals()[i]=customer[i]
            else:
                globals()[i]=data[i]
        context = self.ez.stripe.Customer.modify(
            customer_id,
            address=address,
            balance=balance,
            currency=currency,
            default_source=default_source,
            description=description,
            discount=discount,
            email=email,
            invoice_prefix=invoice_prefix,
            invoice_settings=invoice_settings,
            metadata=metadata,
            next_invoice_sequence=next_invoice_sequence,
            phone=phone,
            preferred_locales=preferred_locales,
            shipping=shipping,
        )
        return context

    def delete(self, id):
        context = self.ez.stripe.Customer.delete(id)
        return context

    def list(self, limit=None, email=None):
        if email != None:
            context = json.dumps(self.ez.stripe.Customer.list(
                limit=limit, email=email)["data"])
        else:
            context = json.dumps(self.ez.stripe.Customer.list(limit=limit)['data'])
        return context

