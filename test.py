from ezstripe import ez_stripe

# print(ez_stripe().product.list(limit=1))

## ONE TIME PRODUCT/PRICE CREATE
# print(ez_stripe().product.create({
    # "active": True,
#     "name": "test-product-2",
#     "unit_amount": 1000,
#     "metadata": {"type": "store"}
#     }))

## RECURRING PRODUCT/PRICE CREATE
# print(ez_stripe().product.create({
    # "active": True,
#     "name": "test-product-3",
#     "unit_amount": 1000,
#     "recurring": {
#         "interval": "month",
#         "interval_count": 12,
#         "usage_type": "licensed"
#     }
# }))

## MULTIPLE PRODUCT/PRICE CREATE
# print(ez_stripe().product.create({
#     "active": True,
#     "name": "multi price 2",
#     "unit_amount": [1000, 2000],
# }))

## MODIFY PRODUCT/PRICE 
ez_stripe().product.modify({
    "active": True,
    "id":"prod_JqojgnVP7jDFop",
    "name": "test nov13 1am",
    "description": "new name DESCRIPTION",
    "unit_amount": [140000,2000]
    })

## RETRIEVE PRODUCT/PRICE
# print(ez_stripe().product.retrieve(
#     "prod_JqojgnVP7jDFop"
#     ))