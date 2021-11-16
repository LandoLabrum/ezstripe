from ezstripe import ez_stripe

create=ez_stripe().session.create(
    customer_id="cus_KZaRYovQ1JN6vL",
    mode="payment",
    line_items=[{
      "price": "price_1JXfu3IodeKZRLDVHcVLbnXx",
      "quantity": 2,
    }],
    )
print(create)