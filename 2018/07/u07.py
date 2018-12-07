#!/usr/bin/env python

__motd__ = '--- Day 7: The Sum of Its Parts ---'

__url__ = 'http://adventofcode.com/2018/day/4'

import re


verbose = 1


class Sequence:

    def __init__(self):
        self.dependency = {}

    def a_depends_b(self, a, b):
        """ a is dependent on b (b must be before a) """
        if a not in self.dependency:
            self.dependency[a] = [b]
            return
        self.dependency[a].append(b)
        return

    def can_go(self, path, b):
        """ true if we can go to b """
        # cannot go twice to the same node
        if b in path: return False
        # check all b dependencies
        for check in self.dependency.get(b, []):
            # if dependency is fullfilled just continue
            if check in path: continue
            # dependency failed
            return False
        # yes - we can go to the b
        return True

    def walk(self):
        """ walk """
        # prepare all possible nodes sorted alphabetically
        allnodes = sorted(list(set([ y for x in self.dependency.values() for y in x ] + self.dependency.keys())))
        # path already walked
        path = []
        while True:
            # check all moves
            avail = [ node for node in allnodes if self.can_go(path, node) ]
            # debug
            if verbose: print "walk-lin() path:",path,"avail:",avail
            # no more any steps available = end
            if len(avail) == 0: break
            # take the (alphabetically) first node from available
            node = sorted(avail)[0]
            # walk on
            path = path + [ node ]
            # remove active node from available nodes to speed-up next searching steps
            allnodes.remove(node)
        # walked path
        return path

    def input_line(self, str):
        """ Step C must be finished before step A can begin. """
        m = re.match(r'Step (.) must be finished before step (.) can begin', str)
        if m is None: return "ERR: malformatted input line: %s" % str
        c,a = m.group(1), m.group(2)
        self.a_depends_b(a, c)
        return ''

    def task_a(self, input):
        """ task A """
        for line in input:
            err = self.input_line(line)
            if err: print err
        #
        if verbose: print "dependency:",self.dependency
        r = self.walklin()
        print "keys:",sorted(self.dependency.keys())
        print "resu:",sorted(r)
        return ''.join(r)

    def task_b(self, input):
        """ task B """
        return


def testcase(sut, input, result, task_b=False):
    " testcase verifies if input returns result "
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [line.rstrip() for line in f]
    #
    print "TestCase", "B" if task_b else "A", "for input:", data if 'data' in vars() else input, "\t expected result:", result,
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    #r = f.find_duplo(input) if task_b else f.change_seq(input)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    print

# ========
#  Task A
# ========
data = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""
# test cases
testcase(Sequence(), data.strip().split('\n'),  'CABDFE')
# GKRVWBESYAMZDPTIUCFXQJLHNO
testcase(Sequence(), None, 'GKRVWBESYAMZDPTIUCFXQJLHNO')
xxx
# ========
#  Task B
# ========

# test cases
testcase((), ['', '', '', ''],            2, task_b=True)

# [1m 34s] 56360
testcase((), None, 2, task_b=True)
