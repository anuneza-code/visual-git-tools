def total_price(items):
    total = 0
    for price in items:
        total = total + price
    return total


prices = [10, 25, 8]
print("Total:", total_price(prices))