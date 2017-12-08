#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(challenge):
    answer = 0
    last_char = challenge[-1]
    """docstring for main"""
    for char in challenge:
        if char == last_char:
            answer += int(char)
        last_char = char
    return answer

def test1():
    assert main("1122") == 3

def test2():
    assert main("1111") == 4

def test3():
    assert main("1234") == 0

def test5():
    assert main("91212129") == 9

if __name__ == '__main__':
    print main(open('day1-input.txt', 'r').read().strip())

