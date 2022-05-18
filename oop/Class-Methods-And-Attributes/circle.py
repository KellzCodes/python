class Circle:
  pi = 3.14

  @classmethod
  def area(cls, radius):
    return cls.pi * (radius ** 2)

  @classmethod
  def perimeter(cls, radius):
    return 2 * cls.pi * radius

  @classmethod
  def get_area_and_perimeter(cls, radius):
    return cls.area(radius), cls.perimeter(radius)

print(Circle.area(2))
