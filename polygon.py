from drawing_board import DrawingBoard
from collections import Set
import random

class RandomPolygon:
    """
    Randomly creates a polygon with the specified number of sides
    """

    def __init__(self, board: DrawingBoard, n_sides: int):
        self.Board = board
        self._points = []
        for i in range(n_sides):  # 1200 x 800 canvas
            self._points.append((random.randint(0, 1200), random.randint(0, 800)))

    def distance(self, p1, p2):
        """
        Computes euclindean distance between two points
          Example: (0, 0) -> (5, 0) = 5 | (1, 0) -> (1, 4) = 4 | (0, 0) -> (3, 4) = 5
        :param p1: point 1
        :param p2: point 2
        :return: distance
        """
        return (((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)) ** 0.5

    def get_nearest_neighbor(self, this, rest: Set):
        """
        Returns the point of those remaining that is closest to this point
          Example: point = (0, 0), rest = {(1, 1), (2, 2)} -> (1, 1)
        :return: point
        """

        nearest = None
        dist = 10000000
        for i in rest:
            d = self.distance(this, i)
            if d < dist:
                nearest = i
                dist = d
        return nearest

    def draw(self):
        """
        Draws the segments of the polygon
        :return: none
        """

        # how to render w/o lines crossing over?

        print("Drawing polygon...")
        self.Board.SHOULD_ANIMATE = True  # set indicator at start
        this_point = self._points[0]
        other = set(self._points)
        other.remove(this_point)
        for i in range(len(self._points)):

            if i == len(self._points) - 1:  # final point - close polygon
                next_point = self._points[0]
            else:  # draw segment from this point to next point
                next_point = self.get_nearest_neighbor(this_point, other)
                other.remove(next_point)
            print("[outer loop {0}] this: {1} | next: {2}".format(i, this_point, next_point))

            fraction = 75
            start = this_point
            for j in range(1, fraction+1):
                end_x = this_point[0] + (next_point[0] - this_point[0]) * j / fraction
                end_y = this_point[1] + (next_point[1] - this_point[1]) * j / fraction
                # print("[inner loop {0}] start: {1} | end: ({2}, {3})".format(j, start, end_x, end_y))
                self.Board.Canvas.create_line(start[0], start[1], end_x, end_y, width=3, fill='black')
                self.Board.Window.update()  # redraw
                start = (end_x, end_y)

            radius = 2
            self.Board.Canvas.create_oval(this_point[0] - radius, this_point[1] - radius,
                                          this_point[0] + radius, this_point[1] + radius,
                                          fill="Red", outline="Red", width=radius)
            this_point = next_point