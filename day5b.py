
class JumpMaze(object):
    def __init__(self, text):
        self.offsets = list()
        for line in text.split():
            self.offsets.append(int(line))

    def solve(self):
        step = 0
        position = 0
        while position >= 0 and position < len(self.offsets):
            step += 1
            next_jump = self.offsets[position]
            if self.offsets[position] >= 3:
                self.offsets[position] -= 1
            else:
                self.offsets[position] += 1
            position += next_jump
        return step

def test_example():
    TEST_INPUT = """0
    3
    0
    1
    -3
    """
    assert JumpMaze(TEST_INPUT).solve() == 10

if __name__ == '__main__':
    with open('day5-input.txt', 'r') as infile:
        print JumpMaze(infile.read()).solve()
