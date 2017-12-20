#!/usr/bin/env python
# -*- coding: utf-8 -*-

INPUT = tuple([int(x) for x in "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14".split()])

def rebalance(state):
    state = list(state)
    value = max(state)
    index = state.index(value)
    state[index] = 0
    while value > 0:
        index = (index + 1) % len(state)
        state[index] += 1
        value -= 1
    return tuple(state)

def answer(state):
    states = set()
    while state not in states:
        states.add(state)
        state = rebalance(state)
    return len(states)

def test_example():
    assert answer((0, 2, 7, 0)) == 5

if __name__ == '__main__':
    print answer(INPUT)
