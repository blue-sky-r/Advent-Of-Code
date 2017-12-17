#!/usr/bin/env python

__motd__ = '--- Day 12: ---'

__url__ = 'http://adventofcode.com/2017/day/12'


verbose = 1


class Pipes:

    def __init__(self):
        self.nodes = {}

    def parse_file(self, fname):
        nodes = {}
        with open(fname) as f:
            for line in f:
                line = line.strip()
                if not line: continue
                id,connected = self.parse_line(line)
                nodes[id] = connected
        self.nodes = nodes

    def travel(self, id, visited=None):
        if visited is None: visited = []
        visited.append(id)
        for con in self.nodes.get(id).split(', '):
            if con not in visited:
                visited = self.travel(con, visited)
        return visited
        
    def parse_line(self, str):
        id,_,csv = str.partition(' <-> ')
        return id, csv


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    p = Pipes()
    p.parse_file(input)
    r = len(p.travel(id='0'))
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

#
testdata = __file__.replace('.py', '.test.input')
testcase(testdata, 6)

# use testcase for task data and result
data = __file__.replace('.py', '.input')
# 130
testcase(data, 130)
