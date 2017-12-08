#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rot(challenge, offset):
    length = len(challenge)
    return (offset + (length / 2)) % length

def main(challenge):
    answer = 0
    for idx, char in enumerate(challenge):
        if char == challenge[rot(challenge, idx)]:
            answer += int(char)
    return answer


def test():
    # the list contains 4 items, and all four digits match the digit 2 items ahead.
    assert main("1212") == 6
    # because every comparison is between a 1 and a 2.
    assert main("1221") == 0
    # because both 2s match each other, but no other digit has a match.
    assert main("123425") == 4
    assert main("123123") == 12
    assert main("12131415") == 4

if __name__ == '__main__':
    print main(open('day1-input.txt', 'r').read().strip())

