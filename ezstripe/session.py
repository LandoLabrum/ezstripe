from stripe.error import InvalidRequestError


class Session(object):
    def __init__(self, ez):
        self.ez = ez

    def create(self, customer_id=None, mode="setup", line_items=None):
        """
        mode: ("payment", "setup", "subscription")
           line_items=[
            {
            "price": price_id,
            "quantity": quantity,
            },
        ]
        """
        
        context = self.ez.stripe.checkout.Session.create(
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
            payment_method_types=["card"],
            customer=customer_id,
            line_items=line_items,
            mode=mode,
        )
        return context

    # def retrieve(self, method_id=None):
    #     context={}
    #     try:
    #         context = self.ez.stripe.Session.retrieve(method_id)
    #     except InvalidRequestError as e:
    #         context = e
    #     return context

    # def modify(self, d):
    #     context = self.ez.stripe.Session.modify(
    #         d['id'],
    #         address=d['address'],
    #         description=d['description'],
    #         email=d['email'],
    #         metadata=d['metadata'],
    #         name=d['name'],
    #         phone=d['phone'],
    #     )
    #     return context

    # def delete(self, id):
    #     context = self.ez.stripe.Session.delete(id)
    #     return context

    # def list(self, customer_id=None):
    #     context=self.ez.stripe.Customer.list_payment_methods(
    #         customer_id,
    #         type="card",
    #     ).to_dict()['data']
    #     return context
