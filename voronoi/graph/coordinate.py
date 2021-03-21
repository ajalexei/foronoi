from decimal import Decimal


class Coordinate:
    def __repr__(self):
        return f"Coordinate({round(self.x, 3)}, {round(self.y, 3)})"


class DecimalCoordinate(Coordinate):
    def __init__(self, x=None, y=None):
        """
        A point in 2D space.
        :param x: (float) The x-coordinate
        :param y: (float) The y-coordinate
        """
        self._x: Decimal = Decimal(str(x)) if x is not None else None
        self._y: Decimal = Decimal(str(y)) if y is not None else None

    def __sub__(self, other):
        return DecimalCoordinate(x=self.x - other.x, y=self.y - other.y)

    def __repr__(self):
        return f"Coord({self.x:.2f}, {self.y:.2f})"

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = Decimal(str(value))

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = Decimal(str(value))

    def as_floats(self):
        return FloatCoordinate(self.x, self.y)

    def as_float_tuple(self):
        return float(self.x), float(self.y)


class FloatCoordinate(Coordinate):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
