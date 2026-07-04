"""A tiny shopping-cart total calculator (demo app)."""


def add_item_prices(prices):
    """Return the total price of all items in the cart."""
    total = 0
    for price in prices:
        total = total + price
    return total


def apply_discount(total, percent):
    """Apply a percentage discount to the total."""
    return total * (1 - percent / 100)
