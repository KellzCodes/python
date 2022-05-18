class Student:
  grade_bump = 2.0
  
  def __init__(self, name, grades=[]):
    self.name = name
    self.grades = grades

  def average(self):
    return sum(self.grades) / len(self.grades)
  
  @classmethod
  def average_from_grades_plus_bump(cls, grades):
    average = cls.average_from_grades(grades)
    return min(average + grade_bump, 100)
  
  @staticmethod
  def average_from_grades(grades):
    return sum(grades) / len(grades)
