import re

EXAMPLE_INPUT = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
""".strip().splitlines()

class Forest(object):
    def __init__(self):
        self.towers = dict()
        self.roots = dict()
        self.parent_for_node = dict()

    def add(self, tower):
        self.towers[tower.name] = tower
        if tower.name not in self.parent_for_node:
            self.roots[tower.name] = tower
        for child in tower.children:
            self.parent_for_node[child] = tower.name
            if child in self.roots:
                del self.roots[child]

    def __getitem__(self, key):
        return self.towers[key]

    def weight(self, name):
        t = self[name]
        if not t.total_weight:
            answer = t.weight
            for child in t.children:
                answer += self.weight(child)
            t.total_weight = answer
        return t.total_weight


class Tower(object):
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
        self.total_weight = 0

TOWER_PATTERN = re.compile(r'(\w+) \((\d+)\)( -> (.*))?')
def load_tower(line):
    m = TOWER_PATTERN.match(line)
    if m:
        name = m.group(1)
        weight = int(m.group(2))
        children = m.group(4)
        if children:
            children = children.split(", ")
        else:
            children = []
        return Tower(name, weight, children)

def load_forest(lines):
    forest = Forest()
    for line in lines:
        tower = load_tower(line)
        if tower is None:
            print "NO TOWER: {}".format(line)
        forest.add(tower)
    return forest


def test_parse():
    t = load_tower(EXAMPLE_INPUT[0])
    assert t.name == 'pbga'
    assert t.weight == 66
    assert t.children == []

    t = load_tower(EXAMPLE_INPUT[-3])
    assert t.name == 'ugml'
    assert t.weight == 68
    assert t.children == ['gyxo', 'ebii', 'jptl']

def test_root():
    f = load_forest(EXAMPLE_INPUT)
    assert len(f.roots) == 1
    assert 'tknk' in f.roots

if __name__ == '__main__':
    INPUT = open('day7-input.txt').read().splitlines()
    print load_forest(INPUT).roots.keys()
