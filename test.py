from ezstripe import ez_stripe

# print(ez_stripe().product.list(limit=1))

# ONE TIME CREATE
# print(ez_stripe().product.create({
#     "name": "test-product-2",
#     "unit_amount": 1000,
#     "metadata": {"type": "store"}
#     }))

# RECURRING CREATE
# print(ez_stripe().product.create({
#     "name": "test-product-3",
#     "unit_amount": 1000,
#     "recurring": {
#         "interval": "month",
#         "interval_count": 12,
#         "usage_type": "licensed"
#     }
# }))
