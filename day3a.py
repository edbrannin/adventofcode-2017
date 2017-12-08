#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Ring(object):
    def __init__(self, position):
        self.position = position
        self.level, self.floor = self._values(self.position)
        self.offset = self.position - self.floor
        self.cardinals = self._cardinals()
        self.distance_from_middle = 0 #FIXME

    def _values(self, position):
        last_answer = 0
        last_level = 0
        for level, x in enumerate(range(1, position+1, 2)):
            square = level ** 2
            if square == position:
                return (level, x)
            elif square > position:
                return (last_level, last_answer + 1)
            elif square % 2 != 0:
                last_answer = square
                last_level = level
        raise Exception("Unable to find a value")

    def _cardinals(self):
        if self.level == 1:
            return (1,)
        corner_distance = (self.level - 1) ** 2
        first_cardinal = self.floor + corner_distance - 1
        return tuple([first_cardinal + corner_distance*x for x in range(4)])

    def __repr__(self):
        return "Ring({})".format( self.position,)


    def __str__(self):
        return repr(self) + "<level={}, floor={}, offset={}>".format(
                self.level,
                self.floor,
                self.offset,
                )

    def manhattan(self):
        return self.level + self.distance_from_middle


class Grid(object):
    """Each square on the grid is allocated in a spiral pattern starting at
    a location marked 1 and then counting up while spiraling outward.

    For example, the first few squares are allocated like this:

    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...
    """

    def biggest_odd_square(self, position):
        pass

    def manhattan(self, location):
        """docstring for manhattan"""
        return 0

def test_ring0():
    ring = Ring(1)
    assert ring.position == 1
    assert ring.level == 0
    assert ring.floor == 1
    assert ring.offset == 0
    assert ring.cardinals == (1,)

def test_ring2():
    ring = Ring(2)
    assert ring.position == 2
    assert ring.level == 1
    assert ring.floor == 2
    assert ring.offset == 0
    assert ring.cardinals == (2, 4, 6, 8)

def test_ring4():
    ring = Ring(4)
    assert ring.position == 4
    assert ring.level == 1
    assert ring.floor == 2
    assert ring.offset == 2
    assert ring.cardinals == (2, 4, 6, 8)

def test_ring12():
    ring = Ring(12)
    assert ring.position == 12
    assert ring.level == 2
    assert ring.floor == 10
    assert ring.offset == 2
    assert ring.cardinals == (11, 15, 19, 23)

def test_ring23():
    ring = Ring(23)
    assert ring.position == 23
    assert ring.level == 2
    assert ring.floor == 10
    assert ring.offset == 13
    assert ring.cardinals == (11, 15, 19, 23)

def test_ring26():
    ring = Ring(26)
    assert ring.position == 26
    assert ring.level == 3
    assert ring.floor == 26
    assert ring.offset == 0
    # assert ring.cardinals == (11, 15, 19, 23)
    assert 49 in ring.cardinals


def test_ring27():
    ring = Ring(27)
    assert ring.position == 27
    assert ring.level == 3
    assert ring.floor == 26
    assert ring.offset == 1
    # assert ring.cardinals == (11, 15, 19, 23)
    assert 49 in ring.cardinals


def test1():
    assert Grid().manhattan(1) == 0

def test2():
    assert Grid().manhattan(11) == 2

def test3():
    assert Grid().manhattan(23) == 2

"""
def test2():
    assert Grid().manhattan(12) == 3

def test4():
    assert Grid().manhattan(1024) == 31
"""

def main():
    print Grid().manhattan(277678)

if __name__ == '__main__':
    for x in range(1, 35):
        r = Ring(x)
        print (x, r.level)
    main()
