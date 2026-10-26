import pytest
from product import Product


def test_product():
    p = Product("пицца", 500)
    assert str(p) == "пицца - 500₽"
    assert repr(p) == "Product('пицца', 650)"
    p2 = Product("пицца", 500)
    assert p == p2
    with pytest.raises(ValueError):
        p.price = -200

def test_for_vat():
    p = Product("пицца", 500)
    assert p.price_with_vat() == 600

def test_negative_price_in_init():
    with pytest.raises(ValueError):
        Product("пицца", -200)

def test_valid_name():
    assert Product.is_valid_name("пицца") == True

@pytest.mark.parametrize("name, expected", [
    ("пицца", True),
    ("", False),
    ("a" * 50, True),
    ("a" * 51, False),
])

def test_is_valid_name(name, expected):
    assert Product.is_valid_name(name) == expected

def test_from_string():
    soup = Product.from_string("soup;300")
    assert soup.name == "soup"