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

    def find_start(self):
        """ start node has no dependencies """
        found = []
        # depend on
        depon = [d for c, dep in self.dependency.items() for d in dep]
        for c in self.dependency:
            if c in depon: continue
            if c not in found: found.append(c)
        # sort
        found.sort()
        if verbose: print "find_start()",found
        return found

    def walk(self, act):
        r = [ act ]
        # tree = walk recursively
        if act in self.dependency:
            for c in sorted(self.dependency[act]):
                if verbose: print "walk(",act,") -> ", self.dependency[act]
                r = r + self.walk(c)
        return r

    def can_go(self, path, b):
        """ true if can go to b """
        if b in path: return False
        # all b dependensies
        for check in self.dependency.get(b, []):
            # if fullfilled just continue
            if check in path: continue
            # dependency failed
            return False
        return True

    def walk_lin(self):
        """ linear walk """
        allnodes = sorted(list(set([ y for x in self.dependency.values() for y in x ] + self.dependency.keys())))
        path = []
        while True:
            # check all moves
            avail = [ node for node in allnodes if self.can_go(path, node) ]
            if verbose: print "walk-lin() path:",path,"avail:",avail
            if len(avail) == 0: break
            node = sorted(avail)[0]
            path = path + [ node ]
            allnodes.remove(node)
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
        r = self.walk_lin()
        #start = self.find_start()
        #r = self.walk(start[0])
        #if verbose: print "walk() ->",r
        ## reduce all double nodes to the last single instance
        #r = [ c for i,c in enumerate(r) if c not in r[i+1:] ]
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
