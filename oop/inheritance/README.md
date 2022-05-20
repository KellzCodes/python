# inheritance

![image](https://user-images.githubusercontent.com/19383145/169172849-b841584e-2072-42a8-843a-489a80a3dbcd.png)

```
class Animal:
    def __init__(self, species):
        self.species = species


class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def speak(self):
        print(f"{self.species} named {self.name}: Woof!")


class Cat(Animal):
    def __init__(self, age):
        super().__init__("Cat")
        self.age = age

    def speak(self):
        print(f"{self.age} year old {self.species}: Miao!")


animals = [Dog("Rex"), Cat(13), Dog("Rose")]
for animal in animals:
    animal.speak()
```

Output:

![image](https://user-images.githubusercontent.com/19383145/169173033-d4b4d801-1d12-4844-a165-d4fdf43a1f61.png)

## What is inheritance?

Inheritance allows you to have one class inherit or use the functionality from another class. 

Inheritance allows you to have related classes, reuse functionality, such that it's easier to debug in the future, easier to modify or change, and it allows you to not have to duplicate code throughout your program. 

## Polymorphism

Polymorphism means we can treat objects differently based on the contect that we're using them in. 

A single object may have multiple characteristics, but exhibit different behavior based on how we're treating it in our program. 

## Inheritance Syntax

```
class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def say_hello(self):
    print(f"Hi, my name is {self.first_name} {self.last_name}")

class Employee(Person):
  def test(self):
    print("test")
```

## Parent / Child Classes

Below, the `Employee` class is the child class. The class that inherits from something is called the child class, subclass, or drive class. 

`Employee` inherits from class `Person`. The class we inherit from is known as the superclass, base class, or parent class.

`Employee` has access to everything inside of its superclass. 

```
class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def say_hello(self):
    print(f"Hi, my name is {self.first_name} {self.last_name}")

class Employee(Person):
  def test(self):
    print("test")

e = Employee("Kelli", "Davis")
e.say_hello()
```

Output:

![image](https://user-images.githubusercontent.com/19383145/169411578-204b47bf-5cdd-45ad-9825-af42a656957b.png)

`Person` does not have access to anything inside `Employee` because `Person` not inherit anything from `Employee`.

Let's add the line `e = Person("Kelli", "Davis")` then run `e.test()`. We get an error because `Person` does not have an attribute called `test`

```
class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def say_hello(self):
    print(f"Hi, my name is {self.first_name} {self.last_name}")

class Employee(Person):
  def test(self):
    print("test")

e = Person("Kelli", "Davis")
e.test()
```

Output: 

![image](https://user-images.githubusercontent.com/19383145/169412205-b2f33f54-dbe0-4757-b333-64611181dc25.png)

## Method Overriding

Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes. When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.

![image](https://user-images.githubusercontent.com/19383145/169422921-5187a9e9-da55-458c-b8a4-bc3b86c7d1d9.png)

Using `super()` will implicitly pass the `self` keyword to the method that's on the super class

```
class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def say_hello(self):
    print(f"Hi, my name is {self.first_name} {self.last_name}")

class Employee(Person):
  def say_hello(self):
    super().say_hello()

e = Employee("Kelli", "Davis")
e.say_hello()
```

Output:

![image](https://user-images.githubusercontent.com/19383145/169423970-72a60ed5-b5a1-452e-aef2-0e8a740abae7.png)

### Overriding the constructor (`__init__()`)

This is how you override the constructor. 

```
class Employee(Person):
  def __init__(self, first_name, last_name, salary):
    super().__init__(first_name, last_name)
    self.salary = salary
```

This is how overriding the the constructor works in a program. 

```
class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def say_hello(self):
    print(f"Hi, my name is {self.first_name} {self.last_name}")

class Employee(Person):
  def __init__(self, first_name, last_name, salary):
    super().__init__(first_name, last_name)
    self.salary = salary
    
  def say_hello(self):
    super().say_hello()
    print(f"My salary is {self.salary}")

e = Employee("Kelli", "Davis", 50000)
e.say_hello()
```

Output:

![image](https://user-images.githubusercontent.com/19383145/169424800-da30e380-35b2-40b1-ba01-4949f4af125e.png)

## Multilevel Inheritance

We can also inherit from a child class. This is called multilevel inheritance. It can be of any depth in Python.

In multilevel inheritance, features of the parent class and the child class are inherited into the new child class.

![image](https://user-images.githubusercontent.com/19383145/169426846-793d96c0-60e0-4389-8a78-4198ba3d9063.png)

Below, the `Employee` class is derived from the `Person` class, and the `Manager` class is derived from the `Employee` class

```
class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def say_hello(self):
    print(f"Hi, my name is {self.first_name} {self.last_name}")

class Employee(Person):
  def __init__(self, first_name, last_name, salary):
    super().__init__(first_name, last_name)
    self.salary = salary
    
  def say_hello(self):
    super().say_hello()
    print(f"My salary is {self.salary}")

class Manager(Employee):
  def __init__(self, first_name, last_name, salary, department):
    super().__init__(first_name, last_name, salary)
    self.department = department
```

## `isinstance()`

`isistance()` allows us to check if a specific object is a type

```
class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def say_hello(self):
    print(f"Hi, my name is {self.first_name} {self.last_name}")

class Employee(Person):
  def __init__(self, first_name, last_name, salary):
    super().__init__(first_name, last_name)
    self.salary = salary
    
  def say_hello(self):
    super().say_hello()
    print(f"My salary is {self.salary}")

class Manager(Employee):
  def __init__(self, first_name, last_name, salary, department):
    super().__init__(first_name, last_name, salary)
    self.department = department

m = Manager("Kelli", "Davis", 50000, "Sports")
print(isinstance(m, Person))
```

Output: 

True

## Multiple Inheritance

A class can be derived from more than one base class in Python, similar to C++. This is called multiple inheritance.

In multiple inheritance, the features of all the base classes are inherited into the derived class. The syntax for multiple inheritance is similar to single inheritance.

#### Example

```
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
```

Here, the `MultiDerived` class is derived from `Base1` and `Base2` classes.

![image](https://user-images.githubusercontent.com/19383145/169436530-ba67ac45-87c3-4acd-9c30-88a9777ad219.png)

The `MultiDerived` class inherits from both `Base1` and `Base2` classes.

## Duck Typing

Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.

```
class Duck:
  def swim(self):
    print("Swimming duck")

  def fly(self):
    print("Flying duck")

class Whale:
  def swim(self):
    print("Swimming whale")

animals = [Duck(), Duck(), Whale()]

for animal in animals:
  animal.swim()
  animal.fly()
```

Output: 

![image](https://user-images.githubusercontent.com/19383145/169442216-4a3d37da-6fe3-488e-884f-253eba4cd9b1.png)

The above program crashed because `Whale` does not have a method called `fly()`. 

You can't do this in a lot of other programming languages. You can't even run this code. In Python, you can run the code. Everything ran fine until it crashed. 
