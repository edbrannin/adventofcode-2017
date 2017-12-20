#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fileinput

def is_valid(phrase):
    words = set()
    for word in phrase.split(' '):
        if word in words:
            return False
        words.add(word)
    return True

def test_is_valid():
    assert is_valid("aa bb cc dd ee")
    assert not is_valid("aa bb cc dd aa")
    assert is_valid("aa bb cc dd aaa")

def main():
    total_valid = 0
    for line in fileinput.input("day4-input.txt"):
        line = line.strip()
        if is_valid(line):
            total_valid += 1
    print total_valid


if __name__ == '__main__':
    main()

