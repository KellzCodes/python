# Operator Overloading

![image](https://user-images.githubusercontent.com/19383145/169733715-70e9dd54-4937-4f96-8b38-dcccb2dc9e20.png)

## Addition (`__add__`)

Python’s `__add__(self, other)` method returns a new object that represents the sum of two objects. It implements the addition operator `+` in Python.

```
class Page:
  def __init__(self, words, page_number):
    self.words = words
    self.page_number = page_number

  def __add__(self, other):
    new_words = self.words + other.words
    new_page_number = max(self.page_number, other.page_number) + 1
    return Page(new_words, new_page_number)

page1 = Page("Tim is a great instructor! ", 1)
page2 = Page("This is another page", 2)
page3 = page1 + page2
print(page3.words, page3.page_number)
```

Output:

![image](https://user-images.githubusercontent.com/19383145/169739063-94ef0e94-b18d-472e-b5fe-59dd3c80469e.png)

## Subtraction (`__sub__()`)

Python’s `__sub__(self, other)` method returns a new object that represents the difference of two objects. It implements the subtraction operator `-` in Python.

```
class StoreItem:
  TAX = 0.13
  
  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.after_tax_price = 0
    self.set_after_tax_price()

  def set_after_tax_price(self):
    self.after_tax_price = self.price * (1 + self.TAX)

  def __sub__(self, discount):
    return StoreItem(self.name, self.price - discount)

bread = StoreItem("Bread", 7)
discounted_bread = bread - 2
print(discounted_bread.after_tax_price)
```

Output:

![image](https://user-images.githubusercontent.com/19383145/169740329-991faee1-8239-43a7-b573-4f6169cc0f95.png)

## Multiplication (`__mul__()`)

The Python `__mul__()` method is called to implement the arithmetic multiplication operation `*`. 

```
class Data:

    def __init__(self, value):
        self.value = value
        
    def __mul__(self, other):
        return Data(self.value * other.value)


a = Data(21)
b = Data(2)
c = a * b

print(c.value)
```

Output:

42

## Division (`__truediv__()`)

The Python `__truediv__()` method is called to implement the normal division operation `/` called true division as opposed to the floor division operation `//`.

```
class Data:

    def __init__(self, value):
        self.value = value
        
    def __truediv__(self, other):
        return Data(self.value / other.value)


a = Data(22)
b = Data(2)
c = a / b

print(c.value)
```

Output:

11.0

## Division (`__floordiv__()`)

The Python `__floordiv__()` method implements the integer division operation `//` called floor division as opposed to the true division operation `/`.

```
class Data:

    def __init__(self, value):
        self.value = value
        
    def __floordiv__(self, other):
        return Data(self.value // other.value)


a = Data(21)
b = Data(2)
c = a // b

print(c.value)
```

Output:

10

The Python `__len__` method returns a positive integer that represents the length of the object on which it is called. It implements the built-in `len()` function.

```
class Data:
    def __len__(self):
        return 42


a = Data()

print(len(a))
```

## Equality comparison (`__eq__()`)

To customize the behavior of the equality operator `x == y`, override the `__eq__()` dunder method in your class definition. Python internally calls `x.__eq__(y)` to compare two objects using `x == y`. If the `__eq__()` method is not defined, Python will use the is operator per default that checks for two arbitrary objects whether they reside on the same memory address.

```
class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age



alice = Person(18)
bob = Person(19)
carl = Person(18)

print(alice == bob)
# False

print(alice == carl)
# True
```

## Equality comparison (`__ne__()`)

To customize the behavior of the non-equality operator `x != y`, override the `__ne__()` dunder method in your class definition. Python internally calls `x.__ne__(y)` to compare two objects using `x != y`. If the `__ne__()` method is not defined, Python will use the is not operator per default that checks for two arbitrary objects whether they reside on a different memory address.

```
class Person:
    def __init__(self, age):
        self.age = age

    def __ne__(self, other):
        return self.age != other.age



alice = Person(18)
bob = Person(19)
carl = Person(18)

print(alice != bob)
# True

print(alice != carl)
# False
```

## Other Comparisons (`__gt__()`)

To customize the behavior of the greather than operator `x > y`, override the `__gt__()` dunder method in your class definition. Python internally calls `x.__gt__(y)` to obtain a return value when comparing two objects using `x > y`. The return value can be any data type because any value can automatically converted to a Boolean by using the `bool()` built-in function. If the `__gt__()` method is not defined, Python will raise a `TypeError`.

```
class Person:
    def __init__(self, age):
        self.age = age

    def __gt__(self, other):
        return self.age > other.age



alice = Person(18)
bob = Person(17)
carl = Person(18)

print(alice > bob)
# True

print(alice > carl)
# False

print(bob > alice)
# False
```

## Other Comparisons (`__lt__()`)

To customize the behavior of the less than operator `x < y`, override the `__lt__()` dunder method in your class definition. Python internally calls `x.__lt__(y)` to obtain a return value when comparing two objects using `x < y`. The return value can be any data type because any value can automatically converted to a Boolean by using the `bool()` built-in function. If the `__lt__()` method is not defined, Python will raise a `TypeError`.

```
class Person:
    def __init__(self, age):
        self.age = age

    def __lt__(self, other):
        return self.age < other.age



alice = Person(18)
bob = Person(17)
carl = Person(18)

print(alice < bob)
# False

print(alice < carl)
# False

print(bob < alice)
# True
```

## `__str__()`

The Python `__str__` method returns a string representation of the object on which it is called. For example, if you call `print(x)` an object `x`, Python internally calls `x.__str__()` to determine the string representation of object `x`. This method is also used to implement the built-in `str()` function.

```
class Data:
        
    def __str__(self):
        return 'This is a string'


a = Data()

print(str(a))
# This is a string
```

## `__repr__()`

The Python `__repr__` method returns a string representation of the object on which it is called. It implements the built-in `repr()` function. If you call `print(x)` an object `x`, Python internally calls `x.__str__()` to determine the string representation of object `x`. If this isn’t implemented, Python calls `x.__repr__()`.

```
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def __repr__(self):
        return '123'

    
porsche = Car('black', 'porsche')
tesla = Car('silver', 'tesla')

print(str(porsche))
print(str(tesla))
```

Output:

![image](https://user-images.githubusercontent.com/19383145/169744686-e714fdd2-00d0-4ebd-8ef6-f9f5c44bd16b.png)
