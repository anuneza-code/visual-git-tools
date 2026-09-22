def total_price(items, discount=0):
    """Return the total price of all items after applying a discount percentage."""
    total = 0
    for price in items:
        total = total + price
    total = total - (total * discount / 100)
    return total


prices = [10, 25, 8]
print("Total:", total_price(prices, discount=10))
print("Checkout complete.")