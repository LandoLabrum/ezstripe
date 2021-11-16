from stripe.error import InvalidRequestError


class Method(object):
    def __init__(self, ez):
        self.ez = ez

    def create(self, customer_id=None, card=None):
        billing_details={"address":self.ez.customer.retrieve(customer_id)["address"]}
        
        method = self.ez.stripe.PaymentMethod.create(
            type="card",
            card=card,
            billing_details=billing_details
        )['id']
        context=self.ez.stripe.PaymentMethod.attach(
            method,
            customer=customer_id
        )
        # context = self.ez.stripe.SetupIntent.create(
        #     customer=customer_id,
        #     payment_method=method
        # )
        return context

    def retrieve(self, method_id=None):
        context = {}
        try:
            context = self.ez.stripe.PaymentMethod.retrieve(method_id)
        except InvalidRequestError as e:
            context = e
        return context

    def modify(self, d):
        context = self.ez.stripe.PaymentMethod.modify(
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
        context = self.ez.stripe.PaymentMethod.delete(id)
        return context

    def list(self, customer_id=None):
        context = self.ez.stripe.Customer.list_payment_methods(
            customer_id,
            type="card",
        ).to_dict()['data']
        return context
