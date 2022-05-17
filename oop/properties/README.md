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
