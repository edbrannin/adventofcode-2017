from collections import defaultdict
import re

LINE_REGEX = re.compile(r'(\w+) (inc|dec) (-?\d+) if (\w+) ([><=!]+) (-?\d+)')

class Registers(object):
    def __init__(self):
        self.state = defaultdict(int)

    def __getitem__(self, key):
        return self.state[key]

    def do(self, line):
        op = Operation(line)
        if op.condition(self.state):
            if op.operation == 'inc':
                self.state[op.target_register] += op.amount
            elif op.operation == 'dec':
                self.state[op.target_register] -= op.amount
            else:
                raise Exception("Unexpected operation '{}' in line: {}".format(op.operation, line))

    @property
    def values(self):
        return self.state.values()

    @property
    def keys(self):
        return self.state.keys()

class Operation(object):
    def __init__(self, line):
        m = LINE_REGEX.match(line)
        if not m:
            raise Exception("Could not match line: {}".format(line))
        self.target_register = m.group(1)
        self.operation = m.group(2)
        self.amount = int(m.group(3))
        self.condition_register = m.group(4)
        self.condition_operation = m.group(5)
        self.condition_value = int(m.group(6))

    def condition(self, registers):
        actual_value = registers[self.condition_register]
        expr = "{} {} {}".format(actual_value, self.condition_operation, self.condition_value)
        return eval(expr)

def answer(lines):
    re = Registers()
    for line in lines:
        re.do(line)
    return max(re.values)


EXAMPLE_INPUT = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
""".strip().splitlines()

def test_example_op0():
    op = Operation(EXAMPLE_INPUT[0])
    assert op.target_register == 'b'
    assert op.operation == 'inc'
    assert op.amount == 5
    assert op.condition_register == 'a'
    assert op.condition_operation == '>'
    assert op.condition_value == 1

def test_example():
    r = Registers()
    assert len(r.state) == 0

    r.do(EXAMPLE_INPUT[0])
    assert r['a'] == 0
    assert r['b'] == 0

    r.do(EXAMPLE_INPUT[1])
    assert r['a'] == 1
    assert r['b'] == 0

    r.do(EXAMPLE_INPUT[2])
    assert r['a'] == 1
    assert r['b'] == 0
    assert r['c'] == 10

    r.do(EXAMPLE_INPUT[3])
    assert r['a'] == 1
    assert r['b'] == 0
    assert r['c'] == -10

def test_answer():
    assert answer(EXAMPLE_INPUT) == 1

TEST_INPUT = open('day8-input.txt').read().strip().splitlines()

if __name__ == '__main__':
    print answer(TEST_INPUT)
