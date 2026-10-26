class Cart:
    def __init__(self):
        self.cart_items = []

    def add_item(self, name, price):
        self.cart_items.append([name, price])

    def __str__(self):
        return self.cart_items

    def __len__(self):
        return len(self.cart_items)

    def total(self):
        total = 0
        for item in self.cart_items:
            total += item[1]
        return total