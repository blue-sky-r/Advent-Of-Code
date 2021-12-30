#!/usr/bin/env python3

__day__  = 14

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Polymerization:

    def __init__(self):
        pass

    def print(self, msg, data):
        print(msg,''.join(data) if type(data) is list else data)

    def init_polymer(self, input:list):
        template = input[0]
        self.formula = {}
        for line in input[2:]:
            # CH -> B
            l, r = line.split(' -> ')
            self.formula[l] = r
        return template

    def step(self, template:list):
        newtemplate = [template[0]]
        for idx in range(len(template)-1):
            a,b = template[idx],template[idx+1]
            c = self.formula[''.join([a,b])]
            newtemplate.extend([c,b])
        return newtemplate

    def grow(self, template, steps=10):
        result = list(template)
        for step in range(steps):
            result = self.step(result)
            if verbose: self.print('step %d:' % (step+1),result)
        return result

    def calc_elements(self, result:list):
        # list of unique elements
        elements = list(set(self.formula.values()))
        elementbycount = dict([ (e,result.count(e)) for e in elements ])
        #countbyelement = sorted(elementcount, key=get)
        cnt = elementbycount.values()
        return max(cnt) - min(cnt)

    def task_a(self, input: list):
        """ task A """
        template = self.init_polymer(input)
        polymer = self.grow(template)
        return self.calc_elements(polymer)

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
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Polymerization(), testdata,  1588)

# 3213
testcase_a(Polymerization(),   None,    3213)

