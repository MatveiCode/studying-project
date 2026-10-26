class Product:
    currency = "₽"
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}{self.currency}"

    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

if __name__ == "__main__":
    pizza_peperoni = Product("пицца", 650)
    pizza_peperoni_2 = Product("пицца", 650)
    print(pizza_peperoni)
    print(repr(pizza_peperoni))
    print(pizza_peperoni == pizza_peperoni_2)