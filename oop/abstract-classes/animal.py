class Animal:
    def sleep(self):
        print("ZzzZzz")

    def animal_sound(self):
        raise NotImplementedError("Method not implemented.")

    def wake_up(self):
        self.animal_sound()
        print("I am awake!")


class Lion(Animal):
    def animal_sound(self):
        print("Roar!")
