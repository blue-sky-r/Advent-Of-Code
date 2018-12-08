#!/usr/bin/env python

__motd__ = '--- Day 7: The Sum of Its Parts ---'

__url__ = 'http://adventofcode.com/2018/day/4'

import re


verbose = 0


class Sequence:

    def __init__(self, workers=2, stepsec=1):
        self.dependency = {}
        # part B only
        self.workers = workers
        self.stepsec = stepsec

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
            if verbose: print "walk() path:",path,"avail:",avail
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

    def cooperative_walk(self, workers):
        """ cooperation mode """
        # prepare all possible nodes sorted alphabetically
        allnodes = sorted(list(set([y for x in self.dependency.values() for y in x] + self.dependency.keys())))
        worker, path = {}, []
        # time up to 1k
        for time in range(1000):
            # free workers
            free_workers = [ id for id in range(self.workers) if worker.get(id, []) == [] ]
            if verbose > 2: print "time:",time,"free_workers:",free_workers
            # do we have any worker free
            if free_workers != []:
                # check all available nodes
                avail = [node for node in allnodes if self.can_go(path, node)]
                if verbose > 2: print "time:",time,"avail:",avail
                # check if all avail nodes are already in queues
                for anode,awid in zip(avail, free_workers):
                    # skip if a new node already in any worker queue
                    if any([ anode in que for id,que in worker.items() ]): continue
                    # assign available node anode to worker id awid
                    worker[ awid ] = [ anode ] * (ord(anode) - ord('A') + 1 + self.stepsec)
                #
                if verbose > 2: print "time:",time,"worker queues:",worker

            # visualize
            #
            if verbose: print time,' '.join([ '.' if worker.get(id,[]) == [] else worker[id][-1] for id in range(self.workers) ]),path

            # remove from queues
            for id,queue in worker.items():
                # nothing to remove from empty queue
                if queue == []: continue
                # remove (pop)
                done = queue.pop()
                # completed ?
                if queue == []:
                    # yes, walk on
                    path.append(done)
                    # remove from available
                    allnodes.remove(done)
                    #
                    if verbose > 2: print "time:",time,"path updated:",path

            # no more any nodes available => end
            if len(avail) == 0: break
        else:
            return "ERR: timeout - increase time limit"
        #
        return time

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
        #
        r = self.walk()
        return ''.join(r)

    def task_b(self, input):
        """ task B """
        for line in input:
            err = self.input_line(line)
            if err: print err
        #
        if verbose: print "dependency:", self.dependency
        #
        r = self.cooperative_walk(self.workers)
        return r


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

# ========
#  Task B
# ========

# test cases
testcase(Sequence(), data.strip().split('\n'),  15, task_b=True)
# 903
testcase(Sequence(workers=5, stepsec=60), None, 903, task_b=True)
