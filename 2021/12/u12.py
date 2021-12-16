#!/usr/bin/env python3

__day__  = 12

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Cave:

    def __init__(self):
        # { node: [connected_nodes], ... }
        self.graph = {}

    def graph_add_edge(self, nodeA, nodeB):
            # existing nodeA
            if self.graph.get(nodeA):
                # do not add duplicities
                if not nodeB in self.graph[nodeA]:
                    self.graph[nodeA].append(nodeB)
            else:
                # create/add nodeA
                self.graph[nodeA] = [nodeB]

    def init_graph(self, input: list):
        for line in input:
            nodeA, nodeB = line.split('-')
            # A -> B
            self.graph_add_edge(nodeA, nodeB)
            # B -> A
            self.graph_add_edge(nodeB, nodeA)

    def walk_graph_a(self, path=''):
        if verbose: print("walk_graph(",path,")")
        visited = path.split()
        # source node
        last = visited[-1]
        # result
        r = []
        # walk all edges from last node
        for dst in self.graph[last]:
            # if end reached do not dive deeper
            if dst == 'end':
                r.append(dst)
                continue
            # do not visit locase nodes more than once
            if dst.lower() == dst and dst in visited:
                continue
            # dive deeper
            found = self.walk_graph_a(path + ' ' + dst)
            # add all found alternatives
            for f in found:
                r.append(dst + ' ' + f)
        #
        if verbose: print("walk_graph(",path,")","=",", ".join(r))
        return r

    def task_a(self, input: list):
        """ task A """
        self.init_graph(input)
        return len(self.walk_graph_a('start'))

    def task_b(self, input: list):
        """ task B """
        return None


def testcase_a(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ line.strip() for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()

def testcase_b(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ line.strip() for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_b(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()


# ======
#  MAIN
# ======

print()
print(__motd__, __url__)
print()

testdata = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

testdata2 = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

testdata3 = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Cave(), testdata,   10)

# test cases
testcase_a(Cave(), testdata2,  19)

# test cases
testcase_a(Cave(), testdata3, 226)

# 5252
testcase_a(Cave(),   None,   5252)

