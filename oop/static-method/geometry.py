import math

class Geometry:
    @staticmethod
    def perimeter_of_square(side_length):
        return 4 * side_length

    @staticmethod
    def area_of_square(side_length):
        return side_length ** 2

    @staticmethod
    def perimeter_of_circle(radius):
        return 2 * math.pi * radius

    @staticmethod
    def area_of_circle(radius):
        return math.pi * (radius ** 2)


print("Perimeter of square with side of length 7:", Geometry.perimeter_of_square(7))
print("Area of square with side of length 7:", Geometry.area_of_square(7))

print("Perimeter of circle with radius of length 3:", Geometry.perimeter_of_circle(3))
print("Perimeter of circle with radius of length 3:", Geometry.area_of_circle(3))
