#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class Spreadsheet(object):
    def __init__(self, data):
        strings = [ re.split('\D+', line) for line in data.strip().splitlines() ]
        self.data = [ [ int(x) for x in line ] for line in strings ]

    def row_value(self, row):
        for x in row:
            for y in row:
                if x == y:
                    pass
                elif x % y == 0:
                    return x / y

    def answer(self):
        return sum([self.row_value(row) for row in self.data])

def test():
    data = """
    5	9	2	8
    9	4	7	3
    3	8	6	5
    """
    assert main(data) == 9

def main(data):
    return Spreadsheet(data).answer()

if __name__ == '__main__':
    print main(open('day2-input.txt', 'r').read())
