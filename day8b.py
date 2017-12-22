from day8a import Registers, TEST_INPUT, EXAMPLE_INPUT


def answer(lines):
    re = Registers()
    global_max = 0
    for line in lines:
        re.do(line)
        local_max = max(re.values)
        global_max = max((local_max, global_max))
    return global_max


def test_answer():
    assert answer(EXAMPLE_INPUT) == 10


if __name__ == '__main__':
    print answer(TEST_INPUT)
