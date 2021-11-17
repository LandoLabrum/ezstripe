import time
from ezstripe import ez_stripe

ts = int(time.time())
ez = ez_stripe()

# create = ez.customer.create({
#     "name": f"Test @{ts}",
#     "email":"test@deepturn.com",
#     "phone":"4356719245",
#     "address": {
#         "city": "Heber City",
#         "country": "US",
#         "line1": "1800 S 3350 E",
#         "line2": "",
#         "postal_code": "84032",
#         "state": "Utah"
#     },
#     "description": f"Test @{ts}: description",
# })

# retrieve = ez.customer.retrieve(customer_id="cus_KbW3LQR3X73HCr")

# modify = ez.customer.modify(
#     data={"name": f"Test @{ts}"},
#     customer_id="cus_KbXJgnXasELhuQ"
#     )

# delete = ez.customer.delete("cus_KbW3LQR3X73HCr")

# list = ez.customer.list(email="test@deepturn.com")
# print(create)