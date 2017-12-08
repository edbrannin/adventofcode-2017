#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test():
    data = """
    5	1	9	5
    7	5	3
    2	4	6	8
    """.strip()
    assert main(data) == 18

def main(data):
    total = 0
    for row in data.splitlines():
        print row
        values = [int(x) for x in row.split('\t')]
        print values
        total += (max(values) - min(values))
    return total

if __name__ == '__main__':
    print main(open('day2-input.txt', 'r').read().strip())
