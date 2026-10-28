class Product:
    currency = "₽"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = value

    @property
    def price_with_vat(self):
        return self._price + (self.price / 5)

    def __str__(self):
        return f"{self.name} - {self.price}{self.currency}"

    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    @staticmethod
    def is_valid_name( name):
        return 0 < len(name) <= 50

    @classmethod
    def from_string(cls, text):
        name, price = text.split(";")
        return cls(name, int(price))

    def return_info(self):
        return f"{self.name};{self.price}"


if __name__ == "__main__":
    pizza_peperoni = Product("пицца", 650)
    pizza_peperoni_2 = Product("пицца", 650)
    print(pizza_peperoni)
    print(repr(pizza_peperoni))
    print(pizza_peperoni == pizza_peperoni_2)
    print(Product.is_valid_name("Пицца"))  # True
    print(Product.is_valid_name(""))  # False
    print(Product.is_valid_name("а" * 51))  # False — 51 символ
    print(Product.is_valid_name("а" * 50))  # True — ровно 50, граница

    soup = Product.from_string("Суп;300")
    print(soup)  # Суп - 300₽
    print(repr(soup))  # Product('Суп', 300)
