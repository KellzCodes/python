# Class Methods And Attributes

A class is just a blueprint that objects are modeled after; yet, it can actually possess attributes and methods that are specific to itself and only itself, but not any instance of itself.

![image](https://user-images.githubusercontent.com/19383145/168952643-e20192df-5f95-48da-a198-099dfbbb8589.png)

```
class Instructor:
    instructors = []

    def __init__(self, name):
        self.name = name
        Instructor.instructors.append(self)


tim = Instructor("Tim")
clement = Instructor("Clement")

print(f"There are {len(Instructor.instructors)} instructors")
for instructor in Instructor.instructors:
    print(f"{instructor.name} is an instructor!")
```

Output:

![image](https://user-images.githubusercontent.com/19383145/169154843-7477d6d5-4428-427a-a7b6-740bef3c8439.png)

## Instance Attribute vs Class Attribute

Instance attributes store data associated with each instance of a class while class attributes store data associated with the class itself

In Python, class attributes are attributes associated with a class, not an instance of a class. Class attributes can be accessed by using the class name or from any instance of the class.

Below, `number_of_cars` is a class attribute

```
class Car:
  number_of_cars = 0

  def __init__(self, make, model):
    self.make = make
    self.model = model

print(Car.number_of_cars)
```

Output:

0

### you can update the `__init__()` method to add the class attribute to each instance which will make an instance attribute

```
class Car:
  number_of_cars = 0

  def __init__(self, make, model):
    self.make = make
    self.model = model
    self.number_of_cars = 1

c1 = Car("Ford", "Edge")
c2 = Car("Mazda", "3")

print(c1.number_of_cars)
print(c2.number_of_cars)
```

Output:

![image](https://user-images.githubusercontent.com/19383145/169156542-3238c21a-5a6e-434e-8d50-8b5ddf7c463f.png)

### modify the class attribute by using the class name and update it every time we create a new instance

```
class Car:
  number_of_cars = 0

  def __init__(self, make, model):
    self.make = make
    self.model = model
    Car.number_of_cars += 1

c1 = Car("Ford", "Edge")
c2 = Car("Mazda", "3")

print(c1.number_of_cars)
print(c2.number_of_cars)
print(Car.number_of_cars)
```

Output: 

![image](https://user-images.githubusercontent.com/19383145/169157239-e46cf3ef-342f-4acb-8e79-c2c4475878dd.png)

## Instance Method vs Class Method

An instance method can access and modify both class ans instance attributes while a class method can only access and modify class attributes.

Class methods are used when you only need access to class attributes or class methods while instance methods are used when you need access to instance attributes or instance methods.

Class methods accept a mandatory `cls` parameter and are denoted using the `@classmethod` decorator, while instance attributes accept a mandatory `self` parameter.

```
class Car:
  number_of_cars = 0
  wheels = 4

  def __init__(self, make, model):
    self.make = make
    self.model = model
    Car.number_of_cars += 1

  @classmethod
  def update_number_of_cars(cls, cars):
    cls.number_of_cars = cars
    print("run update")

c1 = Car("Ford", "Edge")
c2 = Car("Mazda", "3")

Car.update_number_of_cars(10)

print(c1.number_of_cars)
print(c2.number_of_cars)
print(Car.number_of_cars)
```

Output: 

![image](https://user-images.githubusercontent.com/19383145/169158665-a93a9440-b2eb-4701-8a27-1130714ae417.png)

#### We can also run class methods on instances

```
class Car:
  number_of_cars = 0
  wheels = 4

  def __init__(self, make, model):
    self.make = make
    self.model = model
    Car.number_of_cars += 1

  @classmethod
  def update_number_of_cars(cls):
    cls.number_of_cars = 5
    print("run update")

c1 = Car("Ford", "Edge")
c2 = Car("Mazda", "3")

c2.update_number_of_cars()

print(c1.number_of_cars)
print(c2.number_of_cars)
print(Car.number_of_cars)
```

Output: 

![image](https://user-images.githubusercontent.com/19383145/169159257-a9846e3d-55e3-4450-969e-a4c46493bb17.png)
