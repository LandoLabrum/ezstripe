from ezstripe import ez_stripe
ez=ez_stripe()
create=ez.session.create(
    customer_id="cus_KbYjCGCrgaDIRp",
    mode="payment",
    line_items=[{
      "price": "price_1JXfu3IodeKZRLDVHcVLbnXx",
      "quantity": 1,
    }],
    )
# retrieve=ez.session.retrieve("cs_test_a1phhn2ZxgITJ3h0Tvr6X2Y5d0hN3uKoztdouXM32Rdho5o2dfiQgL1DiS")
print(create)