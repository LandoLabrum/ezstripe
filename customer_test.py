from ezstripe import ez_stripe

## CUSTOMER LIST
## With email
# print(ez_stripe().customer.list(email="test@test.com"))
## W/o
# print(ez_stripe().customer.list())





## CUSTOMER LIST
# print(ez_stripe().customer.list({
    # "active": True,
#     "name": "test-product-2",
#     "unit_amount": 1000,
#     "metadata": {"type": "store"}
#     }))