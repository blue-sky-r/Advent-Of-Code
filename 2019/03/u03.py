#!/usr/bin/env python

__motd__ = '--- Day 3: Crossed Wires ---'

__url__ = 'http://adventofcode.com/2019/day/3'

verbose = 0


class Grid:

    def __init__(self, size=10, start=(0,0), empty='.'):
        """ init empty grid/matrix """
        self.size = size
        self.start = start
        self.position = start
        self.empty = empty
        #self.matrix = dict([ ((x-start[0],y-start[1]), empty) for y in range(size+1) for x in range(size+1) ])
        self.matrix = {}

    def show(self, path):
        """ display the grid """
        print 'Added path:', path
        #print '\n'.join([for x in range(self.size)[''.join([self.matrix[(x, y)] for y in range(self.size)])])
        for y in range(self.size+1, -self.start[1]-1, -1):
            print ''.join([ 'o' if (x,y) == self.start else self.matrix.get((x,y), self.empty) for x in range(-self.start[0], self.size+1) ])
        print

    def position_within_viewport(self):
        """ check if position is within viewport """
        return (-self.size <= self.position[0] <= self.size) and \
               (-self.size <= self.position[1] <= self.size)

    def up_down_left_right(self, cnt, sym='*', dx=0, dy=0):
        """ route wire with id up/down/left/right cnt steps """
        for x in range(cnt):
            self.position = self.position[0]+dx, self.position[1]+dy
            if self.position_within_viewport():
                self.matrix[self.position] = sym if self.matrix.get(self.position, self.empty) in [self.empty, sym] else 'X'
        return self

    def up(self, cnt, id):
        """ route wire up cnt steps """
        return self.up_down_left_right(cnt, sym=id, dy=+1)

    def down(self, cnt, id):
        """ route wire down cnt steps """
        return self.up_down_left_right(cnt, sym=id, dy=-1)

    def left(self, cnt, id):
        """ route wire up left steps """
        return self.up_down_left_right(cnt, sym=id, dx=-1)

    def right(self, cnt, id):
        """ route wire up right steps """
        return self.up_down_left_right(cnt, sym=id, dx=+1)

    def wire(self, path, id):
        """ layout te wire based on path (string) """
        self.position = self.start
        for step in path.split(','):
            cnt = int(step[1:])
            if step.startswith('U'):
                self.up(cnt, id)
            elif step.startswith('D'):
                self.down(cnt, id)
            elif step.startswith('L'):
                self.left(cnt, id)
            elif step.startswith('R'):
                self.right(cnt, id)
            else:
                print 'ERROR: wire() routing step:', step
        return self

    def manhattan_distance(self, xy):
        """ calc manhattan distance from xy to start """
        return abs(xy[0] - self.start[0]) + abs(xy[1] - self.start[1])

    def all_intersections(self):
        """ calc all intersections manhattan distances """
        # return dict([ (self.manhattan_distance((x,y)), (x, y)) for y in range(self.size) for x in range(self.size) if self.matrix[(x,y)] == 'X' ])
        return dict([(self.manhattan_distance(xy), xy) for xy,id in self.matrix.items() if id == 'X'])

    def task_a(self, input):
        """ task A """
        for id, path in enumerate(input):
            self.wire(path, id='%d' % id)
            if verbose > 2: self.show(path)
        all_x = self.all_intersections()
        if not all_x: print 'ERROR - no intersection found inside viewport, increase viewport size !'
        if verbose: print 'DBG: intersections within viewport:',all_x
        closest = min(all_x)
        return closest

    def task_b(self, input):
        """ task B """
        return


def testcase(sut, input, result, task_b=False):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = f.readlines()
    #
    print "TestCase", "B" if task_b else "A",
    print "for input:", data if 'data' in vars() else input,
    print "\t expected result:", result,
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    print

# ========
#  Task A
# ========

# test cases
testcase(Grid(10),  ['R8,U5,L5,D3','U7,R6,D4,L4'],  6)
testcase(Grid(200), ['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83'],     159)
testcase(Grid(200), ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'],     135)

# 3247
testcase(Grid(5000),   None,  3247)

# ========
#  Task B
# ========

# test cases

