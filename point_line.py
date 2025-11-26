class Point:
    def __init__(self, x:int, y:int, z: int):
        self.x = x
        self.y = y
        self.z = z

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def length(self) -> float:
        return ((self.end.x - self.start.x) ** 2 + 
                (self.end.y - self.start.y) ** 2 + 
                (self.end.z - self.start.z) ** 2) ** 0.5
    
    def direction_cosine_x(self) -> float:
        length = self.length()
        if length == 0:
            return 0.0
        return (self.end.x - self.start.x) / length
    
    def direction_cosine_y(self) -> float:
        length = self.length()
        if length == 0:
            return 0.0
        return (self.end.y - self.start.y) / length

    def direction_cosine_z(self) -> float:
        length = self.length()
        if length == 0:
            return 0.0
        return (self.end.z - self.start.z) / length