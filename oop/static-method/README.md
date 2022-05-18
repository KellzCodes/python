# static method

![image](https://user-images.githubusercontent.com/19383145/169162769-32a7ceed-f0b0-467f-8701-72b1ff1b4963.png)

```
class Student:
  def __init__(self, name, grades=[]):
    self.name = name
    self.grades = grades

  @staticmethod
  def average_from_grades(grades):
    return sum(grades) / len(grades)

s1 = Student("Tim", [80, 75, 65, 100])
s2 = Student("Clement", [60, 50, 65, 60])

average = Student.average_from_grades(s2.grades)
print(average)
```

Output:

![image](https://user-images.githubusercontent.com/19383145/169164663-ef8c9b61-8171-413e-9742-e8e01bd14d42.png)

Class attributes are also called static attributes
