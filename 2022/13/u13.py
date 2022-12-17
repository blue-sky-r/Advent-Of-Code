#!/usr/bin/env python3

__day__  = 13

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class DistressSignal:

    def __init__(self):
        pass

    def parse_validate(self, input: list):
        """ parse and validate pairs """
        idx, left, right, pairs, okpairs = 0, None, None, 0, []
        while idx < len(input):
            line = input[idx]
            idx += 1
            if not line:
                left, right = None, None
                continue
            if left is None:
                left = eval(line)
                continue
            if right is None:
                pairs += 1
                right = eval(line)
                if self.compare(left, right) == -1:
                    okpairs.append(pairs)
                    if verbose: print('pair:', pairs,'is ok', left, right)
        return okpairs

    def parse_add_div(self, input: list, dividers=[]):
        """ just parse and add markers """
        # start with dividers
        result = dividers
        for line in input:
            if line:
                result.append(eval(line))
        return result

    def sorted(self, input: list):
        """ bubble sort input """
        swap = 1
        while swap:
            swap = 0
            for idx in range(len(input)-1):
                if self.compare(input[idx], input[idx+1]) == +1:
                    input[idx], input[idx+1] = input[idx+1], input[idx]
                    swap += 1
        return input

    def compare(self, l, r):
        """ compare left / right : l<r -1/ l=r 0/ l>r +1 """
        # compare scalars
        if type(l) != list and type(r) != list:
            if l > r: return +1
            if l < r: return -1
            return 0
        # if one is list convert other to list also
        if type(l) == list and type(r) != list:
            r = [r]
        if type(l) != list and type(r) == list:
            l = [l]
        # compare lists
        for a, b in zip(l, r):
            c = self.compare(a, b)
            if c != 0:
                return c
        return self.compare(len(l), len(r))

    def div_pos_mult(self, l: list, dividers: list):
        """ locate dividers and calculate multiplication of position1 """
        mult = 1
        for divider in dividers:
            idx = l.index(divider)
            if idx is not None:
                mult = mult * (idx+1)
        return mult

    def task_a(self, input: list):
        """ task A """
        okpairs = self.parse_validate(input)
        return sum(okpairs)

    def task_b(self, input: list):
        """ task B """
        # dividers
        div1, div2 = [[2]], [[6]]
        lst = self.parse_add_div(input, dividers=[div1, div2])
        lst = self.sorted(lst)
        return self.div_pos_mult(lst, [div1, div2])


def testcase_a(sut, input, result, trim=str.rstrip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()

def testcase_b(sut, input, result, trim=str.rstrip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
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
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

# ========
#  Task A
# ========

# test cases
testcase_a(DistressSignal(), testdata,  13)

# 5196
testcase_a(DistressSignal(),   None,  5196)

# ========
#  Task B
# ========

# test cases
testcase_b(DistressSignal(), testdata,  140)

# 22134
testcase_b(DistressSignal(),   None,  22134)
