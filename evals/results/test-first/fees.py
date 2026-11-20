def shipping_fee(order_cents, pickup=False):
    if pickup or order_cents >= 5000:
        return 0
    return 500
