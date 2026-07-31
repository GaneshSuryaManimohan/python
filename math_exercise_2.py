# Area of a circle = pi * r²

import math

radius = float(input("Please enter radius of the circle: "))

area = math.pi * pow(radius, 2)

print(f"Area of the circle is: {round(area,2)}cm^2")
