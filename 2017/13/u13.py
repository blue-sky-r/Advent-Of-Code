#!/usr/bin/env python

__motd__ = '--- Day 13: Packet Scanners ---'

__url__ = 'http://adventofcode.com/2017/day/13'


verbose = 0


class Layer:

    def __init__(self, depth):
        self.depth = depth
        self.reset()

    def reset(self):
        self.dir = 1
        self.pos = 0

    def step(self):
        self.pos += self.dir
        if self.pos+1 == self.depth or self.pos == 0:
            self.dir = - self.dir

    def is_on_top(self):
        return self.pos == 0

    def visualize(self, format='[%s]'):
        for i in range(self.depth):
            c = 'S' if i == self.pos else ' '
            if i > 0: format = '[%s]'
            print format % c,
        print


class Firewall:

    def __init__(self):
        self.layers = {}
        self.reset()

    def reset(self):
        for l in self.layers:
            self.layers[l].reset()
        self.caught = []
        self.timestamp = 0
        self.pos = 0
        self.size = len(self.layers)
        self.data = [ None for i in self.layers ]

    def visualize(self, timestamp):
        print "Timestamp:",timestamp,"ps","delay:",self.delay,"pos:",self.pos
        for l in range(max(self.layers.keys())+1):
            print "%d" % l,
            if self.layers.get(l):
                f = '(%s)' if l == self.pos else '[%s]'
                self.layers[l].visualize(f)
            else:
                print '(.)' if l == self.pos else '...'
        print

    def parse_file(self, fname):
        with open(fname) as f:
            for line in f:
                line = line.strip()
                if not line: continue
                self.parse_line(line)

    def parse_line(self, str):
        level, _, depth = str.partition(': ')
        self.add_layer(int(level), int(depth))

    def add_layer(self, level, depth):
        self.layers[level] = Layer(depth)

    def step(self):
        if verbose: self.visualize(self.timestamp)
        self.timestamp += 1
        self.pos += 1
        for l in self.layers:
            self.layers[l].step()
            if self.hit(l):
                self.caught.append(l)

    def hit(self, level=0):
        return self.layers[level].is_on_top() and self.pos == level

    def severity(self):
        return sum([ l * self.layers[l].depth for l in self.caught ])

    def run(self):
        while self.pos < max(self.layers.keys()):
            self.step()
        return self.severity()

    def find_delay(self):
        self.reset()
        self.timestamp += 1
        self.data.insert(0, self.timestamp)
        while self.pos < max(self.layers.keys()):
            self.step()
            if self.caught:

        return self.timestamp

    def ts_pass(self):
        return self.data[self.size]

def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    f = Firewall()
    f.parse_file(input)
    r = f.find_delay() if task_b else f.run()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print f.caught
    print

# ========
#  Task A
# ========

testdata = __file__.replace('.py', '.test.input')
testcase(testdata, 24)

# use testcase to get result
data = __file__.replace('.py', '.input')
# 1876
testcase(data, 1876)

# ========
#  Task B
# ========

testcase(testdata, 10, task_b=True)

# use testcase to get result
# takes looong time to run, needs different algo
testcase(data, 0, task_b=True)
