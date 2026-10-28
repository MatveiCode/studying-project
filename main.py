import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    filename="shop.log",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)

from cart import Cart
from product import Product

pizza = Product("Pizza", 500)
coffee = Product("Coffee", 120)
steak = Product("Steak", 700)

products = [pizza, coffee, steak]
cart = Cart()
for p in products:
    cart.add_item(p.name, p.price)

cart.total()
