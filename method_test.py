from ezstripe import ez_stripe
create = ez_stripe().method.create(
    customer_id="cus_KZaRYovQ1JN6vL",
    card={"number": "4242424242424242",
     "exp_month": 12,
     "exp_year": 2022,
     "cvc": "314",
     }
)
print(create)

# list=ez_stripe().method.list(customer_id="cus_KZaRYovQ1JN6vL")
# print(list)

# retrieve = ez_stripe().method.retrieve(method_id="pm_1JwG81IodeKZRLDVKUg6MiO4")
# print(retrieve)
