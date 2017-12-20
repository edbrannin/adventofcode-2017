from day6a import INPUT, rebalance

def answer(state):
    states = list()
    while state not in states:
        states.append(state)
        state = rebalance(state)
    return len(states) - states.index(state)

def test_example():
    assert answer((0, 2, 7, 0)) == 4

if __name__ == '__main__':
    print answer(INPUT)

