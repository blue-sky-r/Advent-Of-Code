#!/usr/bin/env python3

__day__  = 9

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)


verbose = 0


class Rope:

    def __init__(self, start=(0,0), dim=None):
        self.head = start
        self.tail = start
        self.track_tail = [ start ]
        self.dim = dim

    def print(self, header='', graphic=['.','#','s','T','H']):
        """ visualize tail trail """
        if not verbose: return
        # autoscale
        if self.dim is None:
            maxx, maxy = max([xy[0] for xy in self.track_tail]), max([xy[1] for xy in self.track_tail])
        else:
            maxx, maxy = self.dim, self.dim
        print(header, 'dim:', maxx, maxy)
        for y in range(maxy-1, -1, -1):
            #row = [ graphic[1 if (x,y) in self.track_tail else 0] for x in range(maxx) ]
            row = []
            for x in range(maxx):
                sym = graphic[0]
                if (x,y) in self.track_tail:
                    sym = graphic[1]
                if (x,y) == (0,0):
                    sym = graphic[2]
                if (x,y) == self.tail:
                    sym = graphic[3]
                if (x,y) == self.head:
                    sym = graphic[4]
                row.append(sym)
            print(' '.join(row))

    def move(self, dir_steps: str):
        """ """
        dir, steps = dir_steps.split()
        dx, dy = 0, 0
        if dir == 'R': dx = +1
        if dir == 'L': dx = -1
        if dir == 'U': dy = +1
        if dir == 'D': dy = -1
        #
        for step in range(int(steps)):
            self.head = self.move_head_delta(dx, dy)
            self.tail = self.tail_follows_head()

    def move_head_delta(self, dx: int, dy: int):
        """ move head (by max 1) """
        return (self.head[0]+dx, self.head[1]+dy)

    def head_tail_delta(self):
        """ """
        dx, dy = self.head[0] - self.tail[0], self.head[1] - self.tail[1]
        return (dx, dy)

    def tail_touching_head(self):
        """  means tail is ok """
        dx, dy = self.head_tail_delta()
        # touching = dx && dy  in range <-1..+1>
        return (-1 <= dx <= +1) and (-1 <= dy <= +1)

    def normalize_delta(self, v):
        """ """
        if v > 0: return +1
        if v < 0: return -1
        return 0

    def tail_follows_head(self):
        """ tail follows the head """
        tailxy = self.tail
        if self.tail_touching_head():
            return tailxy
        dx, dy = self.head_tail_delta()
        stepx, stepy = self.normalize_delta(dx), self.normalize_delta(dy)
        tailxy = (tailxy[0]+stepx, tailxy[1]+stepy)
        if tailxy not in self.track_tail:
            self.track_tail.append(tailxy)
        return tailxy


class RopeBridge:

    def __init__(self):
        pass

    def task_a(self, input: list):
        """ task A """
        rp = Rope()
        for line in input:
            rp.move(line)
            rp.print('after %s' % line)
        return len(rp.track_tail)

    def task_b(self, input: list):
        """ task B """
        return None


def testcase_a(sut, input, result, trim=str.strip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()

def testcase_b(sut, input, result, trim=str.strip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_b(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()


# ======
#  MAIN
# ======

print()
print(__motd__, __url__)
print()

testdata = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

# ========
#  Task A
# ========

# test cases
testcase_a(RopeBridge(), testdata,  13)

# 6011
testcase_a(RopeBridge(),   None,  6011)

