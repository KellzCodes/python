class Animal:
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height


class Mammal(Animal):
    def __init__(self, age, weight, height, sex):
        super().__init__(age, weight, height)
        self.sex = sex


class Reptile(Animal):
    def __init__(self, age, weight, height, legs):
        super().__init__(age, weight, height)
        self.legs = legs


class Monkey(Mammal):
    fingers = 5

    def __init__(self, age, weight, height, sex, color):
        super().__init__(age, weight, height, sex)
        self.color = color


class Lizard(Reptile):
    tail = True

    def __init__(self, age, weight, height, legs, color):
        super().__init__(age, weight, height, legs)
        self.color = color
