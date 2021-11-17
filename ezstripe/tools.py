def product_cleaner(d):
    recurring = None
    metadata = None
    active = False
    if "active" in d:
        active = d['active']
    if "recurring" in d:
        recurring = d['recurring']
    if "metadata" in d:
        metadata = d['metadata']
    return recurring, metadata, active

def invoice_cleaner(data):
    auto_advance = None
    if "auto_advance" in data:
        auto_advance = data["auto_advance"]
    collection_method = None
    if "collection_method" in data:
        collection_method = data["collection_method"]
    description = None
    if "description" in data:
        description = data["description"]
    metadata = None
    if "metadata" in data:
        metadata = data["metadata"]
    subscription = None
    if "subscription" in data:
        subscription = data["subscription"]
    return auto_advance, collection_method, description, metadata, subscription

def subscription_item_cleaner(price_id):
    if isinstance(price_id, list):
        items=[]
        for i in price_id:
            items.append({"price": i})
    else:
        items=[{"price": price_id}]
    return items