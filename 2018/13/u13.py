#!/usr/bin/env python

__motd__ = '--- Day 13: Mine Cart Madness ---'

__url__ = 'http://adventofcode.com/2018/day/13'


verbose = 5


class Tracks:

    def __init__(self):
        self.tracks = {}
        self.carts = {}

    def show(self, time):
        """ visualize """
        mx, my = max(self.tracks.keys(), key=lambda item: item[0])[0], max(self.tracks.keys(), key=lambda item: item[1])[1]
        print "MAP @",time
        for y in range(my+1):
            row = []
            for x in range(mx + 1):
                trk = self.tracks.get((x, y), '.')
                crt = self.carts.get((x,y),{}).get('sym')
                row.append(crt if crt else trk)
        #            print y,''.join([ self.carts[(x,y)] if self.carts.get((x,y)) else self.tracks.get((x,y), ' ') for x in range(m[0]+1) ])
            print y,''.join(row)
        print

    def input_line(self, str, y):
        """  | /-+--+-\  | """
        for x,m in enumerate(str):
            # skip spaces
            if m == ' ': continue
            # tracks
            if m in '|/-+\\':
                self.tracks[(x,y)] = m
                continue
            # cart
            if m in '<>':
                self.tracks[(x,y)] = '-'
                self.carts[(x,y)]  = {
                    'sym': m,
                    'turn': 0
                }
                continue
            # cart
            if m in '^v':
                self.tracks[(x, y)] = '|'
                self.carts[(x, y)] = {
                    'sym': m,
                    'turn': 0
                }
                continue
            # ignore rest
        return

    def collision(self):
        """ detect collision """
        for cart,symbol in self.carts.items():
            pass

    def xy_move(self, xy, dir):
        """ move xy tuple """
        x,y = xy
        if dir == '>': return x+1,y
        if dir == '<': return x-1,y
        if dir == '^': return x,y-1
        if dir == 'v': return x,y+1
        print "ERR - invalid dir: xy_move(xy:",xy,",dir:",dir,")"

    def move_cart(self, xy):
        """ move cart at current position xy """
        # [direction][track] -> updated direction
        # left - straight - right
        turns = {
            '>': {
                '/' : '^',
                '\\': 'v',
                '+' : ['^','>','V']
            },
            '<': {
                '/' : 'v',
                '\\': '^',
                '+' : ['v','<','^']
            },
            '^': {
                '/' : '>',
                '\\': '<',
                '+' : ['<','^','>']
            },
            'v': {
                '/' : '<',
                '\\': '>',
                '+' : ['>','v','<']
            },
        }
        # cart direction
        dir = self.carts[xy]['sym']
        # track at xy
        trackxy = self.tracks.get(xy)
        # check for updated direction
        newdir = turns.get(dir).get(trackxy)
        # round robbin selection at intersection
        if trackxy == '+':
            # current turn index
            idx = self.carts[xy]['turn'] % 3
            # get dir from list
            dir = newdir[idx]
            # update index and direction
            self.carts[xy]['turn'] += 1
            self.carts[xy]['sym'] = dir
        # just update dir if updated dir exists
        else:
            # update dir if found in turn rules
            if newdir:
                dir = newdir
                self.carts[xy]['sym'] = dir
        # new xy
        newxy = self.xy_move(xy, dir)
        if verbose > 2: print "move_cart(xy:",xy,") -> newxy:",newxy
        return newxy

    def time_tick(self):
        """ move carts on the tracks and detect collision """
        carts = {}
        for xy,symbol in self.carts.items():
            newxy = self.move_cart(xy)
            # detect collision
            if newxy in carts:
                self.carts[newxy] = {
                    'sym': 'X'
                }
                return newxy
            carts[newxy] = self.carts[xy]
        if verbose > 1: print "time_tick() carts:",carts
        # no collision, update carts
        self.carts = carts
        return None

    def task_a(self, input):
        """ task A """
        for y,line in enumerate(input):
            self.input_line(line, y)
            if verbose > 4: self.show('building ...')
        #
        for t in range(20):
            if verbose: self.show(time=t)
            colxy = self.time_tick()
            if colxy: break
        #
        if verbose: self.show(time=t)
        return colxy

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

data="""
/->-\        
|   |  /----\ 
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   
"""
# test cases
testcase(Tracks(), data.strip().split('\n'),          (7,3))

#
testcase(Tracks(), None, (0,0))
xxx
# ========
#  Task B
# ========

# test cases
testcase((), ['', '', '', ''],            2, task_b=True)

# [1m 34s] 56360
testcase((), None, 2, task_b=True)
