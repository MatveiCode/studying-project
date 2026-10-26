import pytest
from cart import Cart



@pytest.fixture
def full_cart():
    cart = Cart()
    cart.add_item("pizza", 600)
    cart.add_item("coffee", 120)
    cart.add_item("chicken", 300)
    return cart

def test_str(full_cart):
    assert full_cart.__str__() == full_cart.__str__() != []

def test_len(full_cart):
    assert len(full_cart) == 3

def test_total(full_cart):
    assert full_cart.total() == 1020

