class Menu:
    def __init__(self, items):
        # Note that since the MenuItem has a __gt__ dunder method overridden,
        # the sorting will by default sort the items by name.
        self.items = sorted(items)

    def __str__(self):
        s = f"*** Menu ({len(self)} items) ***\n"
        for item in self.items:
            s += f"- {item.name}: ${item.price} ({item.calories} calories)\n"
        return s

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        return Menu(self.items + other.items)


class MenuItem:
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def __eq__(self, other):
        return (self.name, self.price, self.calories) == (other.name, other.price, other.calories)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.name > other.name


items1 = [
    MenuItem("Apple", 1, 50),
    MenuItem("Filet Mignon", 10, 500),
    MenuItem("Cake", 5, 350),
    MenuItem("Zucchini", 3, 15),
    MenuItem("Wine", 30, 250),
]
menu1 = Menu(items1)
print(menu1)

items2 = [
    MenuItem("Orange", 1, 50),
    MenuItem("Pasta", 8, 300),
    MenuItem("Beef", 10, 500),
]
menu2 = Menu(items2)
print(menu2)

print(menu1 + menu2)
