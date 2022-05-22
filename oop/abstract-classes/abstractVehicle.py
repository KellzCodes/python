class AbstractVehicle:
    def get_max_speed(self):
        raise NotImplementedError

    def get_make(self):
        raise NotImplementedError

    def get_wheel_count(self):
        raise NotImplementedError

    def display(self):
        print(f"Make = {self.get_make()}, Wheel Count = {self.get_wheel_count()}, Top Speed = {self.get_max_speed()}")


class Car(AbstractVehicle):
    def __init__(self, make):
        self.make = make

    def get_wheel_count(self):
        return 4

    def get_make(self):
        return self.make


class Motorcycle(AbstractVehicle):
    def __init__(self, make):
        self.make = make

    def get_wheel_count(self):
        return 2

    def get_make(self):
        return self.make


class Tesla(Car):
    def __init__(self, model):
        super().__init__("Tesla")
        self.model = model

    def get_max_speed(self):
        if self.model == "Plaid":
            return 250
        return 200


class Yamaha(Motorcycle):
    def __init__(self):
        super().__init__("Yamaha")

    def get_max_speed(self):
        return 150


vehicles = [Tesla("Plaid"), Yamaha(), Tesla("S")]
for vehicle in vehicles:
    vehicle.display()
