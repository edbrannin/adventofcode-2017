from day3a import Ring
from collections import defaultdict, deque

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Nav(object):
    def __init__(self):
        self.turn_order = deque([
                RIGHT, UP, LEFT, DOWN
                ])
        self.turn_order.reverse()

    def next(self):
        answer = self.turn_order.pop()
        self.turn_order.appendleft(answer)
        return answer


def test_nav():
    nav = Nav()
    assert nav.next() == RIGHT
    assert nav.next() == UP
    assert nav.next() == LEFT
    assert nav.next() == DOWN
    assert nav.next() == RIGHT
    assert nav.next() == UP

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def next(self, x, y):
        return Point(self.x + x, self.y + y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

def INNER_FACTORY():
    return defaultdict(int)

STEP_RANGE = (-1, 0, 1)

class Map(object):
    def __init__(self):
        self.space = defaultdict(INNER_FACTORY)
        self.location = Point()
        self.nav = Nav()
        for x in range(3):
            # Make "Right" the next diretion
            self.nav.next()
        self.current_direction = self.nav.next()
        self.next_direction = self.nav.next()
        self[self.location] = 1

    def __getitem__(self, point):
        return self.space[point.x][point.y]

    def __setitem__(self, point, value):
        self.space[point.x][point.y] = value

    def peek(self, x, y):
        return self[self.location.next(x, y)]

    def move(self, x, y):
        self.location = self.location.next(x, y)

    def calculate(self):
        if self[self.location] != 0:
            return self[self.location]
        total = 0
        for x in STEP_RANGE:
            for y in STEP_RANGE:
                total += self.peek(x, y)
        self[self.location] = total
        print "Value at {} is now {}".format(self.location, self[self.location])
        return total

    def next(self):
        self.calculate()
        print "Current direction is {}".format(self.current_direction)
        if self.peek(*self.next_direction) == 0:
            print "Turning to {}".format(self.next_direction)
            self.current_direction = self.next_direction
            self.next_direction = self.nav.next()
            print "New current direction is {}, new next direction is {}".format(
                    self.current_direction, self.next_direction)
        print "Moving from {} towards {}".format(self.location, self.current_direction)
        self.move(*self.current_direction)
        print "New location is {}".format(self.location)

def test_map_move():
    m = Map()
    assert m.location == Point(0, 0)

    m.move(*RIGHT)
    assert m.location == Point(1, 0)

    m.move(*RIGHT)
    assert m.location == Point(2, 0)

    m.move(*RIGHT)
    assert m.location == Point(3, 0)


def test_map_next():
    m = Map()
    assert m.location == Point()

    m.next()
    assert m.location == Point(*RIGHT)

    m.next()
    assert m.location == Point(1, 1)

    m.next()
    assert m.location == Point(*UP)

def test_map_nav():
    m = Map()
    assert m[m.location] == 1
    assert m.location == Point()
    assert m.calculate() == 1

    m.move(1, 1)
    assert m[m.location] == 0
    assert m.location == Point(1, 1)
    assert m.calculate() == 1
    assert m[m.location] == 1
    assert m.peek(-1, -1) == 1
    assert m.peek(1, 1) == 0

def test_map_values():
    m = Map()
    p = Point()
    assert m[p] == 1
    m[p] += 1
    assert m[p] == 2
    m[p] += 2
    assert m[p] == 4

    # Mess with another point
    p = p.next(1, 0)
    assert m[p] == 0
    m[p] += 1
    assert m[p] == 1
    m[p] += 5
    assert m[p] == 6

    # Check the origin again
    assert m[Point()] == 4

def value_at_step(steps):
    m = Map()
    for x in range(steps-1):
        m.next()
    return m.calculate()


def first_value_above(floor):
    m = Map()
    while m.calculate() < floor:
        m.next()
    return m.calculate()


"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
"""

def test_example():
    assert value_at_step(1) == 1

    assert value_at_step(2) == 1
    assert value_at_step(3) == 2
    assert value_at_step(4) == 4
    assert value_at_step(5) == 5
    assert value_at_step(6) == 10
    assert value_at_step(7) == 11
    assert value_at_step(8) == 23
    assert value_at_step(9) == 25

    assert value_at_step(10) == 26
    assert value_at_step(11) == 54
    assert value_at_step(12) == 57
    assert value_at_step(13) == 59
    assert value_at_step(14) == 122
    assert value_at_step(15) == 133
    assert value_at_step(16) == 142
    assert value_at_step(17) == 147
    assert value_at_step(18) == 304
    assert value_at_step(19) == 330
    assert value_at_step(20) == 351
    assert value_at_step(21) == 362
    assert value_at_step(22) == 747
    assert value_at_step(23) == 806

if __name__ == '__main__':
    print first_value_above(277678)
