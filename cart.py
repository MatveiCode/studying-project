import logging

logger = logging.getLogger(__name__)


class Cart:
    def __init__(self):
        self.cart_items = []

    def add_item(self, name, price):
        self.cart_items.append([name, price])
        logger.info("в корзину добавлен(о): %s, с ценой: %s", name, price)

    def __len__(self):
        return len(self.cart_items)

    def total(self):
        total = 0
        for item in self.cart_items:
            total += item[1]
        logger.debug("общая цена корзины - %s", total)
        return total
