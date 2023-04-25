"""
A straight line is one that has the same slope x/y between all coordinates.

There will always be at least 2 coordinates provided

- get first coordinate difference and store the slope
- comparing slope is rise / run. to compare two slopes
   (y1 - y0) / (x1 - x0) == (y2 - y1) / (x2 - x1) or to avoid ZeroDivision
   (y1 - y0) * (x - x1) == (y - y1) * (x1 - x0)
"""


def check_straight_line(coordinates: list) -> bool:
    x0, y0 = coordinates[0][0], coordinates[0][1]
    x1, y1 = coordinates[1][0], coordinates[1][1]

    for x, y in coordinates[2:]:
        if (y1 - y0) * (x - x1) != (y - y1) * (x1 - x0):
            return False
    return True

