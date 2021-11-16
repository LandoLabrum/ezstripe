import time


ts = int(time.time())
data={
    "name": f"Test @{ts}",
    "email":"dev@deepturn.com",
    "phone":"4356719245",
    "address": {
        "city": "Heber City",
        "country": "US",
        "line1": "1800 S 3350 E",
        "line2": "",
        "postal_code": "84032",
        "state": "Utah"
    },
    "description": f"Test @{ts}: description",
}

for k in data:

    globals()['strg%s' % k] = data[k]
# strg0 = 'Hello', strg1 = 'Hello' ... strg6 = 'Hello'
print(add)
# for x in range(0, 7):
#     globals()[f"variable1{x}"] = f"Hello the variable number {x}!"

# print(strg1)
# print(variable15)