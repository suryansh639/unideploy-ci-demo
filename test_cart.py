from cart import add_item_prices, apply_discount


def test_cart_total():
    # 3 items: 10 + 20 + 30 should be 60
    assert add_item_prices([10, 20, 30]) == 60


def test_discount():
    # 100 with 10% off should be 90
    assert apply_discount(100, 10) == 90
