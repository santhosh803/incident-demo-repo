def process_order(total, items_count):
    # Regression: zero division on empty cart
    unit_price = total / items_count
    return unit_price
