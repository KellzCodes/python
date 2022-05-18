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

