#!/usr/bin/env python
# -*- coding: utf-8 -*-

def previous_odd_square(target):
    last_x = 0
    for x in range(target + 2):
        if x**2 > target:
            return last_x
        last_x = x
    raise Exception("Couldn't find an odd square <= {} (tried up to {})".format(target, last_x))

def next_odd_square_root(target):
    for x in range(1, target + 2, 2):
        if x**2 >= target:
            return x

class Ring(object):
    """Each square on the grid is allocated in a spiral pattern starting at
    a location marked 1 and then counting up while spiraling outward.

    For example, the first few squares are allocated like this:

    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...
    """

    def __init__(self, position):
        self.position = position
        self.side_length = next_odd_square_root(self.position)
        self.ceiling = self.side_length ** 2
        self.level = level(self.position)

        self.cardinals = self._cardinals()
        self.offset_to_ceiling = self.ceiling - self.position
        self.distance_from_middle = min([
            abs(self.position - cardinal) for cardinal in self.cardinals
            ])

    def _cardinals(self):
        if self.level == 0:
            return (1,)
        distance = self.side_length - 1
        south = self.ceiling - distance / 2
        west = south - distance
        north = west - distance
        east = north - distance
        return (east, north, west, south)

    def __repr__(self):
        return "Ring({})".format( self.position,)


    def __str__(self):
        return repr(self) + "<level={}, ceiling={}, offset_to_ceiling={}>".format(
                self.level,
                self.ceiling,
                self.offset_to_ceiling,
                )

    def manhattan(self):
        if self.position == 1:
            return 0
        return self.level + self.distance_from_middle

def level(position):
    next_ceiling = next_odd_square_root(position)
    level = (next_ceiling - 1) / 2
    return level



def test_get_level():
    assert level(1) == 0
    assert level(2) == 1
    assert level(3) == 1
    assert level(4) == 1
    assert level(5) == 1
    assert level(6) == 1
    assert level(7) == 1
    assert level(8) == 1
    assert level(9) == 1
    assert level(10) == 2
    assert level(11) == 2
    assert level(12) == 2
    assert level(25) == 2
    assert level(26) == 3


def test_next_odd_square():
    assert next_odd_square_root(1) == 1
    assert next_odd_square_root(2) == 3
    assert next_odd_square_root(3) == 3
    assert next_odd_square_root(9) == 3
    assert next_odd_square_root(10) == 5

def test_previous_odd_square():
    assert previous_odd_square(1) == 1
    assert previous_odd_square(2) == 1
    assert previous_odd_square(3) == 1
    assert previous_odd_square(9) == 3
    assert previous_odd_square(10) == 3

def test_ring0():
    ring = Ring(1)
    assert ring.position == 1
    assert ring.level == 0
    assert ring.side_length == 1
    assert ring.cardinals == (1,)

def test_ring2():
    ring = Ring(2)
    assert ring.position == 2
    assert ring.level == 1
    assert ring.side_length == 3
    assert ring.cardinals == (2, 4, 6, 8)

def test_ring4():
    ring = Ring(4)
    assert ring.position == 4
    assert ring.level == 1
    assert ring.side_length == 3
    assert ring.cardinals == (2, 4, 6, 8)

def test_ring12():
    ring = Ring(12)
    assert ring.position == 12
    assert ring.level == 2
    assert ring.side_length == 5
    assert ring.cardinals == (11, 15, 19, 23)

def test_ring23():
    ring = Ring(23)
    assert ring.position == 23
    assert ring.level == 2
    assert ring.side_length == 5
    assert ring.cardinals == (11, 15, 19, 23)

def test_ring26():
    ring = Ring(26)
    assert ring.position == 26
    assert ring.level == 3
    assert ring.cardinals == (28, 34, 40, 46)
    assert ring.side_length == 7

def test_ring27():
    ring = Ring(27)
    assert ring.position == 27
    assert ring.level == 3
    assert ring.cardinals == (28, 34, 40, 46)

def test1():
    assert Ring(1).manhattan() == 0

def test2():
    assert Ring(11).manhattan() == 2

def test3():
    assert Ring(23).manhattan() == 2

def test2():
    assert Ring(12).manhattan() == 3

def test4():
    assert Ring(1024).manhattan() == 31

def main():
    print Ring(277678).manhattan()

if __name__ == '__main__':
    main()
