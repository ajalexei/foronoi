from voronoi import DecimalCoordinate
from voronoi.algorithm import Algorithm
from voronoi.graph import Polygon
from voronoi.graph.bounding_box import BoundingBox


# -----------------
# Helper functions
# -----------------

def _triangle(x, y):
    return Polygon([
        (0, y),
        (x, y),
        (x / 2, 0)
    ])


def _execute(polygon, points, sizes):
    v = Algorithm(polygon)
    v.create_diagram(points=points, vis_steps=False, verbose=False, vis_result=False)
    calculated = [p.cell_size(2) for p in v.points]
    assert sizes == calculated, calculated


# -----------
# Test cases
# -----------

def test_single_point_triangle():
    # Polygon
    polygon = _triangle(100, 100)

    # Points
    points = [
        (50, 50),
    ]

    # Expected sizes
    sizes = [5000]

    # Execute test
    _execute(polygon, points, sizes)


def test_grid():
    # Polygon
    polygon = BoundingBox(-5, 30, -5, 30)

    # Points
    points = []
    for i in range(25, 0, -5):
        for j in range(0, 25, 5):
            points.append((j, i))

    # Expected sizes
    sizes = [56.25, 37.5, 37.5, 37.5, 93.75, 37.5, 25.0, 25.0, 25.0, 62.5, 37.5, 25.0, 25.0, 25.0, 62.5, 37.5, 25.0,
             25.0, 25.0, 62.5, 93.75, 62.5, 62.5, 62.5, 156.25]

    # Execute test
    _execute(polygon, points, sizes)


def test_diamond():
    # Polygon
    polygon = BoundingBox(0, 10, 0, 10)

    # Points
    points = [
        (5, 7.5),
        (2.5, 5),
        (7.5, 5),
        (5, 2.5),
    ]

    # Expected sizes
    sizes = [25.0, 25.0, 25.0, 25.0, ]

    # Execute test
    _execute(polygon, points, sizes)


def test_martijn():
    # Polygon
    polygon = BoundingBox(-1, 26, -1, 26)

    # Points
    points = [
        (2.241, 3.594),
        (3.568, 3.968),
        (6.401, 16.214),
        (2.925, 18.298),
    ]

    # Expected sizes
    sizes = [42.86, 209.3, 380.84, 96.0]

    # Execute test
    _execute(polygon, points, sizes)


def test_roel():
    # Polygon
    polygon = BoundingBox(0, 30, 0, 30)

    # Points
    points = [
        (8.333, 8.333),
        (8.333, 26),
        (16.667, 8.333),
        (26, 17.667)
    ]

    # Expected sizes
    sizes = [214.58, 229.05, 221.56, 234.8]

    # Execute test
    _execute(polygon, points, sizes)


def test_desmos():
    # Polygon
    polygon = BoundingBox(0, 25, 0, 25)

    # Points
    points = [
        (4.6, 11.44),
        (10, 15.44),
        (10, 3),
        (12.7, 10.6),
        (8.7, 7.7),
        (13.9, 6.76),
        (7.1, 4.24),
        (2.3, 12),
        (12, 1.20),
        (5.3, 2),
        (3.4, 2.9),
        (7.8, 8.4),
    ]

    # Expected sizes
    sizes = [26.01, 202.48, 15.87, 95.95, 12.32, 108.89, 14.05, 57.78, 31.34, 12.08, 31.21, 17.03]

    # Execute test
    _execute(polygon, points, sizes)


def test_rounding_errors():
    # Polygon
    polygon = BoundingBox(0, 25, 0, 25)

    # Points
    points = [
        (10, 3),
        (13.9, 6.76),
        (12, 1.20),
    ]

    # Expected sizes
    sizes = [128.59, 465.07, 31.34]

    # Execute test
    _execute(polygon, points, sizes)


def test_corners():
    # Polygon
    polygon = BoundingBox(0, 10, 0, 10)

    # Points
    points = [
        (0, 10),
        (10, 0),
        (0, 0),
        (10, 10),
    ]

    # Expected sizes
    sizes = [25.0, 25.0, 25.0, 25.0]

    # Execute test
    _execute(polygon, points, sizes)


def test_horizontal():
    # Polygon
    polygon = BoundingBox(0, 8, 0, 10)

    # Points
    points = [
        (2, 2.5),
        (4, 2.5),
        (6, 2.5),
    ]

    # Expected sizes
    sizes = [30.0, 20.0, 30.0]

    # Execute test
    _execute(polygon, points, sizes)


def test_left_arc():
    # Polygon
    polygon = BoundingBox(0, 25, 0, 25)

    # Points
    points = [
        (3.125, 3.125),
        (9.375, 3.125),
        (15.625, 3.125),
        (21.875, 3.125),
        (3.125, 9.375),
    ]

    # Expected sizes
    sizes = [39.06, 58.59, 117.19, 156.25, 253.91]

    # Execute test
    _execute(polygon, points, sizes)


def test_multi_diamond():
    # Polygon
    polygon = BoundingBox(-1, 26, -1, 26)

    # Points
    points = [
        (3.125, 3.125),
        (9.375, 3.125),
        (15.625, 3.125),
        (21.875, 3.125),
        (3.125, 9.375),
        (9.375, 9.375),
        (15.625, 9.375),
        (21.875, 9.375),
        (3.125, 15.625),
        (9.375, 15.625),
        (15.625, 15.625),
        (21.875, 15.625),
        (3.125, 21.875),
        (9.375, 21.875),
        (15.625, 21.875),
        (21.875, 21.875),
        (6.25, 18.75),
        (12.5, 18.75),
        (18.75, 18.75),
        (6.25, 12.5),
        (12.5, 12.5),
        (18.75, 12.5),
        (6.25, 6.25),
        (12.5, 6.25),
        (18.75, 6.25),
        (0.0, 12.5),
        (0.0, 18.75),
        (6.25, 25.0),
        (12.5, 25.0),
        (18.75, 25.0),
        (25.0, 18.75)
    ]

    # Expected sizes
    sizes = [47.68, 35.55, 35.55, 47.68, 27.04, 19.53, 19.53, 35.55, 19.53, 19.53, 19.53, 27.04, 30.66, 19.53, 19.53,
             30.66, 19.53, 19.53, 19.53, 19.53, 19.53, 19.53, 19.53, 19.53, 19.53, 16.52, 16.52, 16.52, 16.02, 16.52,
             17.02]

    # Execute test
    _execute(polygon, points, sizes)


def test_triangle_from_left():
    # Polygon
    polygon = _triangle(100, 100)

    # Points
    points = [(13, 93), (20, 89), (33, 69)]

    # Expected sizes
    sizes = [218.59, 629.68, 4151.73]

    # Execute test
    _execute(polygon, points, sizes)


def test_triangle_from_right():
    # Polygon
    polygon = _triangle(100, 100)

    # Points
    points = [(100 - 13, 93), (100 - 20, 89), (100 - 33, 69)]

    # Expected sizes
    sizes = [218.59, 629.68, 4151.73]

    # Execute test
    _execute(polygon, points, sizes)


def test_lines_outside_triangle():
    # Polygon
    polygon = _triangle(100, 100)

    # Points
    points = [
        (57, 75),
        (35, 85),
        (92, 98),
        (81, 87),
    ]

    # Expected sizes
    sizes = [2590.11, 1589.77, 147.0, 673.12]

    # Execute test
    _execute(polygon, points, sizes)


def test_another_line_outside_triangle():
    # Polygon
    polygon = _triangle(100, 100)

    # Points
    points = [
        (54, 90),
        (5, 95),
        (16, 85),
    ]

    # Expected sizes
    sizes = [3490.08, 136.19, 1373.73]

    # Execute test
    _execute(polygon, points, sizes)


def test_max_distance():
    # Polygon
    polygon = _triangle(100, 100)

    # Points
    points = [
        (45, 13),
        (57, 71),
        (39, 82),
        (61, 81),
    ]

    # Expected sizes
    sizes = [899.09, 1299.22, 1629.42, 1172.27]

    # Execute test
    _execute(polygon, points, sizes)


def test_calc_cell_sizes():
    # Polygon
    polygon = _triangle(100, 100)

    # Points
    points = [
        (45, 13),
        (43, 85),
        (39, 82),
        (22, 95),
        (27, 90),
    ]

    # Expected sizes
    sizes = [1161.4, 1958.77, 1128.36, 341.33, 410.13]

    # Execute test
    _execute(polygon, points, sizes)


# Test case added thanks to alexdiab (https://github.com/Yatoom/voronoi/issues/4)
def test_alexdiab():
    points = [(3.45, 3.66), (6.0, 4.54), (7.82, 5.35), (5.65, 3.09), (1.99, 4.66)]
    polygon = Polygon([
        (0, 0),
        (0, 6),
        (9, 0),
        (9, 6)
    ])
    sizes = [14.04, 5.63, 6.11, 16.66, 11.57]
    _execute(polygon, points, sizes)


# Test case added thanks to mars0001 (https://github.com/Yatoom/voronoi/issues/5)
def test_mars0001_1():
    points = [(20.1273, 18.7303), (26.5107, 18.7303), (20.1273, 23.8437), (26.5107, 23.8437)]

    polygon = Polygon([
        (15., 15.),
        (15., 30.),
        (30., 30.),
        (30., 15.),
    ])
    sizes = [52.3, 42.0, 72.48, 58.21]
    _execute(polygon, points, sizes)


# Test case added thanks to mars0001 (https://github.com/Yatoom/voronoi/issues/5)
def test_mars0001_2():
    points = [(0.3308, 0.204), (10.1432, 0.204), (19.9556, 0.204), (29.768, 0.204), (0.3308, 7.942), (10.1432, 7.942),
              (19.9556, 7.942), (29.768, 7.942), (0.3308, 15.6801), (10.1432, 15.6801), (19.9556, 15.6801),
              (29.768, 15.6801), (0.3308, 23.4181), (10.1432, 23.4181), (19.9556, 23.4181), (29.768, 23.4181)]

    polygon = Polygon([
        (0, -10),
        (0., 35.),
        (35., 35.),
        (35., -10.),
    ])

    sizes = [73.7, 138.09, 138.09, 142.67, 40.52, 75.93, 75.93, 78.45, 40.52, 75.93, 75.93, 78.45, 80.92, 151.61,
             151.61, 156.64]
    _execute(polygon, points, sizes)


# Test case added thanks to mars0001 (https://github.com/Yatoom/voronoi/issues/5)
# This test is used to detect rounding errors
def test_large_grid():
    points = [[0.3308, 0.204], [4.5361, 0.204], [8.7414, 0.204], [12.9467, 0.204], [17.1521, 0.204], [21.3574, 0.204],
              [25.5627, 0.204], [29.768, 0.204], [0.3308, 3.5203], [4.5361, 3.5203], [8.7414, 3.5203],
              [12.9467, 3.5203], [17.1521, 3.5203], [21.3574, 3.5203], [25.5627, 3.5203], [29.768, 3.5203],
              [0.3308, 6.8366], [4.5361, 6.8366], [8.7414, 6.8366], [12.9467, 6.8366], [17.1521, 6.8366],
              [21.3574, 6.8366], [25.5627, 6.8366], [29.768, 6.8366], [0.3308, 10.1529], [4.5361, 10.1529],
              [8.7414, 10.1529], [12.9467, 10.1529], [17.1521, 10.1529], [21.3574, 10.1529], [25.5627, 10.1529],
              [29.768, 10.1529], [0.3308, 13.4692], [4.5361, 13.4692], [8.7414, 13.4692], [12.9467, 13.4692],
              [17.1521, 13.4692], [21.3574, 13.4692], [25.5627, 13.4692], [29.768, 13.4692], [0.3308, 16.7855],
              [4.5361, 16.7855], [8.7414, 16.7855], [12.9467, 16.7855], [17.1521, 16.7855], [21.3574, 16.7855],
              [25.5627, 16.7855], [29.768, 16.7855], [0.3308, 20.1018], [4.5361, 20.1018], [8.7414, 20.1018],
              [12.9467, 20.1018], [17.1521, 20.1018], [21.3574, 20.1018], [25.5627, 20.1018], [29.768, 20.1018],
              [0.3308, 23.4181], [4.5361, 23.4181], [8.7414, 23.4181], [12.9467, 23.4181], [17.1521, 23.4181],
              [21.3574, 23.4181], [25.5627, 23.4181], [29.768, 23.4181]]

    polygon = Polygon([
        (0, -10),
        (0., 35.),
        (35., 35.),
        (35., -10.),
    ])

    sizes = [28.87, 49.88, 49.88, 49.88, 49.88, 49.88, 49.88, 87.0, 8.07, 13.95, 13.95, 13.95, 13.95, 13.95, 13.95, 24.32, 8.07, 13.95, 13.95, 13.95, 13.95, 13.95, 13.95, 24.32, 8.07, 13.95, 13.95, 13.95, 13.95, 13.95, 13.95, 24.32, 8.07, 13.95, 13.95, 13.95, 13.95, 13.95, 13.95, 24.32, 8.07, 13.95, 13.95, 13.95, 13.95, 13.95, 13.95, 24.32, 8.07, 13.95, 13.95, 13.95, 13.95, 13.95, 13.95, 24.32, 32.22, 55.68, 55.68, 55.68, 55.68, 55.68, 55.68, 97.11]
    _execute(polygon, points, sizes)


def _test_vertices_correct(polygon, points, expected):
    # Initialize the algorithm
    v = Algorithm(polygon)

    # Create the diagram
    v.create_diagram(points)

    result = [
        [
            [edge.get_origin().as_float_tuple(), edge.twin.get_origin().as_float_tuple()]
            for edge in sorted(vertex.connected_edges, key=_sort_edges)
        ]
        for vertex in sorted(v.vertices, key=_sort_vertices)
    ]

    assert result == expected, result

def _sort_vertices(vertex):
    return vertex.point.y, vertex.point.x


def _sort_edges(edge):
    return edge.get_origin().y, edge.get_origin().x

def test_vertices_correct():
    points = [
        (2.5, 2.5),
        (4, 7.5),
        (7.5, 2.5),
        (6, 7.5),
        (4, 4),
        (3, 3),
        (6, 3),
    ]

    # Define a bounding box
    polygon = Polygon([
        (2.5, 10),
        (5, 10),
        (10, 5),
        (10, 2.5),
        (5, 0),
        (2.5, 0),
        (0, 2.5),
        (0, 5),
    ])

    expected = [[[(2.5, 0.0), (4.642857142857143, 0.0)], [(2.5, 0.0), (0.0, 2.5)]], [[(4.642857142857143, 0.0), (4.5, 1.0)], [(4.642857142857143, 0.0), (5.0, 0.0)], [(4.642857142857143, 0.0), (2.5, 0.0)]], [[(5.0, 0.0), (6.0, 0.5)], [(5.0, 0.0), (4.642857142857143, 0.0)]], [[(6.0, 0.5), (7.583333333333333, 5.25)], [(6.0, 0.5), (10.0, 2.5)], [(6.0, 0.5), (5.0, 0.0)]], [[(4.5, 1.0), (4.5, 2.5)], [(4.5, 1.0), (0.16666666666666607, 5.333333333333334)], [(4.5, 1.0), (4.642857142857143, 0.0)]], [[(0.0, 2.5), (2.5, 0.0)], [(0.0, 2.5), (0.0, 5.0)]], [[(4.5, 2.5), (5.875, 5.25)], [(4.5, 2.5), (1.25, 5.75)], [(4.5, 2.5), (4.5, 1.0)]], [[(10.0, 2.5), (10.0, 5.0)], [(10.0, 2.5), (6.0, 0.5)]], [[(0.0, 5.0), (0.16666666666666607, 5.333333333333334)], [(0.0, 5.0), (0.0, 2.5)]], [[(0.0, 5.0), (0.16666666666666607, 5.333333333333334)], [(0.0, 5.0), (0.0, 2.5)]], [[(10.0, 5.0), (9.25, 5.75)], [(10.0, 5.0), (10.0, 2.5)]], [[(5.875, 5.25), (5.0, 5.75)], [(5.875, 5.25), (7.583333333333333, 5.25)], [(5.875, 5.25), (4.5, 2.5)]], [[(7.583333333333333, 5.25), (6.0, 0.5)], [(7.583333333333333, 5.25), (5.875, 5.25)], [(7.583333333333333, 5.25), (9.25, 5.75)]], [[(0.16666666666666607, 5.333333333333334), (4.5, 1.0)], [(0.16666666666666607, 5.333333333333334), (0.0, 5.0)], [(0.16666666666666607, 5.333333333333334), (0.4624999999999999, 5.925)]], [[(1.25, 5.75), (4.5, 2.5)], [(1.25, 5.75), (5.0, 5.75)], [(1.25, 5.75), (0.4624999999999999, 5.925)]], [[(5.0, 5.75), (1.25, 5.75)], [(5.0, 5.75), (5.0, 10.0)], [(5.0, 5.75), (5.875, 5.25)]], [[(9.25, 5.75), (7.583333333333333, 5.25)], [(9.25, 5.75), (5.0, 10.0)], [(9.25, 5.75), (10.0, 5.0)]], [[(0.4624999999999999, 5.925), (1.25, 5.75)], [(0.4624999999999999, 5.925), (0.16666666666666607, 5.333333333333334)], [(0.4624999999999999, 5.925), (2.5, 10.0)]], [[(2.5, 10.0), (0.4624999999999999, 5.925)], [(2.5, 10.0), (5.0, 10.0)]], [[(5.0, 10.0), (2.5, 10.0)], [(5.0, 10.0), (5.0, 10.0)]], [[(5.0, 10.0), (5.0, 5.75)], [(5.0, 10.0), (5.0, 10.0)], [(5.0, 10.0), (9.25, 5.75)]]]

    _test_vertices_correct(polygon, points, expected)
