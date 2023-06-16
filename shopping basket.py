class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}, color: {self.description}, size: {self.dimensions}"


class User:
    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} {self.surname}, phone number : {self.phone_number}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        tmp = ""
        for item, cnt in self.products.items():
            tmp += f"{str(item)}: {cnt} pcs.\n"

        return f"User:{buyer}\nItems:\n{tmp}"

    def get_total(self):
        total = 0
        for item, count in self.products.items():
            total += item.price * count
        return total


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

buyer = User("Ivan", "Ivanov", "02628162")

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
cart.get_total()
print(cart)
print(f"Total cost of the order: {cart.get_total()}")
