import math

from nodes.leaf_node import Arc, LeafNode
from nodes.point import Point
from decimal import *


class Event:
    @property
    def x(self):
        return 0

    @property
    def y(self):
        return 0

    def __lt__(self, other):
        if self.y == other.y and self.x == other.x:
            return isinstance(self, SiteEvent)

        if self.y == other.y:
            return self.x < other.x

        # Switch y axis
        return self.y > other.y

    def __eq__(self, other):
        if other is None:
            return None
        return self.y == other.y and self.x == other.x

    def __ne__(self, other):
        return not self.__eq__(other)


class SiteEvent(Event):
    def __init__(self, point: Point):
        """
        Site event
        :param point:
        """
        self.point = point

    @property
    def x(self):
        return self.point.x

    @property
    def y(self):
        return self.point.y

    def __repr__(self):
        return f"SiteEvent(x={self.point.x}, y={self.point.y}, pl={self.point.player})"


class CircleEvent(Event):
    def __init__(self, center: Point, radius: float, arc_node: LeafNode, point_triple=None, arc_triple=None):
        """
        Circle event.

        :param y: Lowest point on the circle
        :param arc_node: Pointer to the node in the beach line tree that holds the arc that will disappear
        :param point_triple: The tuple of points that caused the event
        """
        self.center = center
        self.radius = radius
        self.arc_pointer = arc_node
        self.is_valid = True
        self.point_triple = point_triple
        self.arc_triple = arc_triple

    def __repr__(self):
        return f"CircleEvent({self.point_triple}, {round(self.center.y - self.radius, 3)})"

    @property
    def x(self):
        return self.center.x

    @property
    def y(self):
        return self.center.y - self.radius

    def get_triangle(self):
        return (
            (self.point_triple[0].x, self.point_triple[0].y),
            (self.point_triple[1].x, self.point_triple[1].y),
            (self.point_triple[2].x, self.point_triple[2].y),
        )

    def remove(self, verbose=False):
        if verbose:
            print(f"Circle event for {self.y} removed.")
        self.is_valid = False

    @staticmethod
    def create_circle_event(left_node: LeafNode, middle_node: LeafNode, right_node: LeafNode, sweep_line,
                            verbose=False) -> "CircleEvent":
        """
        Checks if the breakpoints converge, and inserts circle event if required.
        :param sweep_line: Y-coordinate of the sweep line
        :param left_node: The node that represents the arc on the left
        :param middle_node: The node that represents the arc on the middle
        :param right_node: The node that represents the arc on the right
        :param verbose: Flag for printing debugging information
        :return: The circle event or None if no circle event needs to be inserted
        """

        # Check if any of the nodes is None
        if left_node is None or right_node is None or middle_node is None:
            return None

        # Get arcs from the nodes
        left_arc: Arc = left_node.get_value()
        middle_arc: Arc = middle_node.get_value()
        right_arc: Arc = right_node.get_value()

        # Get the points from the arcs
        a, b, c = left_arc.origin, middle_arc.origin, right_arc.origin

        # Check if we can create a circle event
        if CircleEvent.create_circle(a, b, c):

            # Create the circle
            x, y, radius = CircleEvent.create_circle(a, b, c)

            # Check if the bottom of the circle is below the sweep line
            if y - radius < sweep_line:

                # Create the circle event
                return CircleEvent(center=Point(x, y), radius=radius, arc_node=middle_node, point_triple=(a, b, c),
                                   arc_triple=(left_arc, middle_arc, right_arc))

        return None

    @staticmethod
    def create_circle(a, b, c):

        a, b, c = sorted((a, b, c), key=lambda item: item.x)

        # Algorithm from O'Rourke 2ed p. 189
        A = Decimal(b.x - a.x)
        B = Decimal(b.y - a.y)
        C = Decimal(c.x - a.x)
        D = Decimal(c.y - a.y)
        E = Decimal((b.x - a.x) * (a.x + b.x) + (b.y - a.y) * (a.y + b.y))
        F = Decimal((c.x - a.x) * (a.x + c.x) + (c.y - a.y) * (a.y + c.y))
        G = Decimal(2 * ((b.x - a.x) * (c.y - b.y) - (b.y - a.y) * (c.x - b.x)))

        if G == 0:
            # Points are all on one line (collinear), so no circle can be made
            return False

        # Center and radius of the circle
        x = (D * E - B * F) / G
        y = (A * F - C * E) / G
        radius = Decimal(math.sqrt(math.pow(Decimal(a.x) - x, 2) + math.pow(Decimal(a.y) - y, 2)))

        return float(x), float(y), float(radius)
