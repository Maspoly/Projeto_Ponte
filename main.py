from point_line import Point, Line

p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)
line = Line(p1, p2)

print(f"Line Length: {line.length()}")
print(f"Direction Cosine X: {line.direction_cosine_x()}")
print(f"Direction Cosine Y: {line.direction_cosine_y()}")
print(f"Direction Cosine Z: {line.direction_cosine_z()}")


