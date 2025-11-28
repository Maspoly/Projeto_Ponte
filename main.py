from point_line import Point, Line

p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)
line = Line(p1, p2)

l = line.direction_cosine_x()
m = line.direction_cosine_y()
n = line.direction_cosine_z()


matrix = [[l**2, l * m, l * n, -(l**2), -(l * m), -(l * n),],
          [l * m, m**2, m * n, -(l * m), -(m**2), -(m * n),],
          [l * n, m * n, n**2, -(l * n), -(m * n), -(n**2),],
          [-(l**2), -(l * m), -(l * n), l**2, l * m, l * n,],
          [-(l * m), -(m**2), -(m * n), l * m, m**2, m * n,],
          [-(l * n), -(m * n), -(n**2), l * n, m * n, n**2,]]


