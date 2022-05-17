# properties 

```
class Instructor:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name.capitalize()

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise Exception("Name must be a string!")

        if len(value) == 0:
            raise Exception("Name cannot be empty!")

        self._name = value


tim = Instructor("tim")
print("Capitalized name:", tim.name)

tim.name = "timothy"
print("Capitalized name:", tim.name)

tim.name = 13  # this should raise an exception!
```

output:

![image](https://user-images.githubusercontent.com/19383145/168705243-6327a82a-9118-409e-9da3-beeaf0626bed.png)

## What is a property?

Properties are special attributes that make it so we can enforce specific behavior when we are accessing or trying to modify an attribute.

## The issues with attributes

The problem with attributes is that they can be modified from outside of the class to anything even if it doesn't make sense

## Private Attributes

In Python, since there is no access modifiers (private, public or protected keywords) to denote an attribute as private you prefix it with a `_`. The attribute can still be accessed and modified like all other attributes but the `_` prefix denotes that it should not be, this is a Python convention.

```
class Person:
  def __init__(self, name):
    self.name = name
    self._salary = 0
```

## Getters and Setters

### Legacy Property

Python’s `property()` is the Pythonic way to avoid formal getter and setter methods in your code. This function allows you to turn class attributes into properties or managed attributes. Since `property()` is a built-in function, you can use it without importing anything.

```
class Person:
  def __init__(self, name):
    self.name = name
    self._salary = 0

  def set_salary(self, salary):
    if salary < 0:
      raise ValueError("Hey, this is invalid!")
    self._salary = salary

  def get_salary(self):
    return round(self._salary)

  salary = property(get_salary, set_salary)

p = Person("KD")
p.salary = 101.1111
print(p.salary)
```

Output:

101

### New Property

`@property` decorator is what you put over your getter. You must name your getter after the attribute you are defining

`@attribute.setter` decorator is what you put over your setter. You must name your setter after the attribute you are defining

```
class Person:
  def __init__(self, name):
    self.name = name
    self._salary = 0

  @property
  def salary(self):
    return round(self._salary)

  @salary.setter
  def salary(self, salary):
    if salary < 0:
      raise ValueError("Hey, this is invalid!")
    self._salary = salary

p = Person("KD")
p.salary = -1
print(p.salary)
```

output:

![image](https://user-images.githubusercontent.com/19383145/168720760-d49ab75d-7e43-487f-a78c-edf82fc9f2c3.png)


## Property Example

```
class Time:
  def __init__(self, second):
    self._second = second

  @property
  def second(self):
    return self._second

  @second.setter
  def second(self, second):
    if second < 0 or second > 60:
      raise ValueError("Invalid!")
    self._second = second

t = Time(54)
t.second = 61
print(t.second)
```

output

![image](https://user-images.githubusercontent.com/19383145/168721478-d96941b6-617f-4037-b494-82190e8cdbe1.png)
