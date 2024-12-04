#!/usr/bin/env python3

__motd__ = '--- Day 1: Historian Hysteria ---'

__url__ = 'http://adventofcode.com/2024/day/1'

verbose = 0


class Distance:

    def __init__(self):
        pass

    def cols2list(self, input):
        """ create lists from columns """
        list0, list1 = [], []
        for line in input if type(input) == list else input.splitlines():
            line = line.strip()
            if not line: continue
            l, r = line.split()
            list0.append(int(l))
            list1.append(int(r))
        return list0, list1

    def calcdistance(self, list0: list, list1: list) -> int:
        """ calc distance """
        d = [ abs(b - a) for a,b in zip(sorted(list0), sorted(list1)) ]
        return sum(d)

    def calcoccurence(self, list0: list, list1: list) -> int:
        """ calc occurence """
        multocc = [ i * list1.count(i) for i in list0 ]
        return sum(multocc)

    def task_a(self, input):
        """ task A """
        list0, list1 = self.cols2list(input)
        d = self.calcdistance(list0, list1)
        return d

    def task_b(self, input):
        """ task B """
        list0, list1 = self.cols2list(input)
        d = self.calcoccurence(list0, list1)
        return d


def testcase(sut, input, result, task_b=False):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    #
    print(f"TestCase {"B" if task_b else "A"} ", end='')
    print(f"for input: {data if 'data' in vars() else input}", end='')
    print(f"\t expected result: {result} ", end='')
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    print(f"got: {r} \t {'[ OK ]' if r == result else '[ ERR ]'}")
    print()

# ========
#  Task A
# ========

inputa = """
3   4
4   3
2   5
1   3
3   9
3   3
"""
# test cases
testcase(Distance(),  inputa,  11)

# 2066446
testcase(Distance(),  None,  2066446)

# ========
#  Task B
# ========

# test cases
testcase(Distance(),  inputa,  31, task_b=True)

# 24931009
testcase(Distance(),  None,  24931009, task_b=True)
