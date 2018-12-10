#!/usr/bin/env python

__motd__ = '--- Day 10: The Stars Align ---'

__url__ = 'http://adventofcode.com/2018/day/10'


import re


verbose = 0


class Stars:

    def __init__(self):
        self.star = []
        # huge value for finding minimum dx
        self.dx = 111222

    def add_star(self, position, velocity):
        """ add star with pos (x,y) and velocity (dx,dy) """
        self.star.append( {
            'pos': position,
            'vel': velocity
        } )

    def show(self, tm):
        """ visualize """
        xrange, yrange = self.xy_range()
        #
        stars = dict([ (s['pos'],s['vel']) for s in self.star])
        print "time:",tm,"dx:",xrange[1]-xrange[0],"dy:",yrange[1]-yrange[0]
        for y in range(yrange[0], yrange[1]+1):
            for x in range(xrange[0], xrange[1]+1):
                if stars.get((x,y)):
                    print '#',
                else:
                    print '.',
            print

    def xy_range(self):
        """ get x range, y range """
        xmin = min([s['pos'][0] for s in self.star])
        xmax = max([s['pos'][0] for s in self.star])
        ymin = min([s['pos'][1] for s in self.star])
        ymax = max([s['pos'][1] for s in self.star])
        if verbose > 1: print "xy_range() x:",xmin,"..",xmax, "y:",ymin,"..",ymax,"dx:",xmax-xmin,"dy:",ymax-ymin
        return (xmin, xmax), (ymin, ymax)

    def is_text(self):
        """ text has x positive and y positive only """
        xrange, yrange = self.xy_range()
        dx, dy = xrange[1] - xrange[0], yrange[1] - yrange[0]
        lastdx = self.dx
        self.dx = dx
        return dy == 9 and dx < 256 and lastdx < dx

    def input_line(self, str):
        """ position=< 9,  1> velocity=< 0,  2> """
        m = re.match(r'position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>', str)
        if m is None: return "ERR: malformatted input line: %s" % str
        pos = int(m.group(1)), int(m.group(2))
        vel = int(m.group(3)), int(m.group(4))
        self.add_star(pos, vel)
        return ''

    def time_step(self, dir=+1):
        """ time step, use dir=-1 for undo """
        r = []
        for s in self.star:
            newpos = s['pos'][0] + dir * s['vel'][0], s['pos'][1] + dir * s['vel'][1]
            r.append({
                'pos': newpos,
                'vel': s['vel']
            })
        self.star = r

    def find_text(self, timeout=11000):
        """ cycle time until text if found """
        found = False
        for t in range(0, timeout):
            if self.is_text():
                self.show(t)
            self.time_step()
            if verbose: self.show(t)
        return found, t

    def task_a(self, input):
        """ task A """
        for line in input:
            err = self.input_line(line)
            if err: print err
        if verbose: self.show(0)
        ok, t = self.find_text()
        if ok: self.show(t)
        return t

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
position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
"""
# test cases
testcase(Stars(), data.strip().split('\n'),          None)

# XPFXXXKL 10521
testcase(Stars(), None, 1)
xxx
# ========
#  Task B
# ========

# test cases
testcase((), ['', '', '', ''],            2, task_b=True)

# [1m 34s] 56360
testcase((), None, 2, task_b=True)
