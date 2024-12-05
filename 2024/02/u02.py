#!/usr/bin/env python3

__motd__ = '--- Day 2: Red-Nosed Reports ---'

__url__ = 'http://adventofcode.com/2024/day/2'


verbose = 0


class SafeReport:

    def row2list(self, input):
        """ create lists from eows """
        r = []
        for line in input if type(input) == list else input.splitlines():
            line = line.strip()
            if not line: continue
            row = [ int(i) for i in line.split() ]
            r.append(row)
        return r

    def issafe(self, diff):
        """ safe if -3 <= diff <= -3 """
        low, high = min(diff), max(diff)
        absdelta = max(abs(low), abs(high))
        return absdelta <= 3 and low * high > 0

    def calcsafe(self, input):
        """ calc safe lists """
        safe = []
        for row in input:
            diff = [ b-a for a,b in zip(row[:-1], row[1:]) ]
            if self.issafe(diff):
                safe.append(row)
        return len(safe)

    def task_a(self, input):
        """ task A """
        rows = self.row2list(input)
        c = self.calcsafe(rows)
        return c

    def task_b(self, input):
        """ task B """
        return


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

input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
# test cases
testcase(SafeReport(),  input,  2)

# 534
testcase(SafeReport(),  None, 534)
