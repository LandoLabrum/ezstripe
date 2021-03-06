

class Invoice(object):
    """
    https://stripe.com/docs/api/invoices/
    """

    def __init__(self, ez):
        self.ez = ez

    def create(self, customer_id=None, data=None):
        auto_advance, collection_method, description, metadata, subscription = invoice_cleaner(
            data)
        context = self.ez.stripe.Invoice.create(
            customer=customer_id,
            auto_advance=auto_advance,
            collection_method=collection_method,
            description=description,
            metadata=metadata,
            subscription=subscription,
        )
        return context

    def retrieve(self, invoice_id):
        context = self.ez.stripe.Invoice.retrieve(
            invoice_id,
        )

        return context

    def modify(self, invoice_id=None, data=None):
        invoice = self.retrieve(invoice_id)
        for i in invoice:
            if i not in data:
                globals()[i] = invoice[i]
            else:
                globals()[i] = data[i]
        context = self.ez.stripe.Invoice.modify(
            invoice_id,
            auto_advance=auto_advance,
            collection_method=collection_method,
            description=description,
            metadata=metadata,
            subscription=subscription,
        )
        return context

    def delete(self, invoice_id=None):
        context = self.ez.stripe.Invoice.delete(
            invoice_id,
        )
        return context

    def finalize(self, invoice_id=None):
        context = self.ez.stripe.Invoice.finalize_invoice(
            invoice_id,
        )
        return context

    def pay(self, invoice_id=None, forgive=None, off_session=None, paid_out_of_band=None, payment_method=None, source=None):
        context = self.ez.stripe.Invoice.pay(
            invoice_id,
            forgive=forgive,
            off_session=off_session,
            paid_out_of_band=paid_out_of_band,
            payment_method=payment_method,
            source=source,
        )
        return context
