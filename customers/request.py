CUSTOMERS = [
    {
        "id": 1,
        "name": "Sharon Gregory",
        "address": "123 Oak Meadow Lane"
    },
    {
        "id": 2,
        "name": "Andrew Sabet",
        "address": "1234 Ridge Farm Place"
    },
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
