from math import hypot
from typing import Optional
class Point:
    """
    A point on the axis provides two-dimensional coordinotes.
    # >>> p1 = point()
    # >>> p2 = point(3, 4)
    # >>> p2.reset()
    # >>> p1.distance(p2)
    0.0
    """
    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initalize the x and y coordinates of the new point
        :param x: x-coordinates
        :param y: y-coordinates
        """
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    def reset(self):
        self.move(0, 0)
    def distance(self, other):
        return hypot(self.x-other.x, self.y-other.y)


point: Optional[Point] = None


def get_point():
    global point
    if not point:
        point = Point()
    return point

def main():
    po1 = get_point()



if __name__ == "__main__":
    main()

