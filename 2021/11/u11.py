#!/usr/bin/env python3

__day__  = 11

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class OctoMap:

    def __init__(self):
        self.energy = []

    def is_valid_xy(self, xy:tuple):
        x,y = xy[0], xy[1]
        return 0<=x<len(self.energy[0]) and 0<=y<len(self.energy)

    def get_xy(self, xy:tuple):
        x,y = xy[0], xy[1]
        return self.energy[y][x]

    def set_xy(self, xy:tuple, val:int):
        x,y = xy[0], xy[1]
        self.energy[y][x] = val

    def adjanced_xy(self, xy: tuple):
        x,y = xy[0], xy[1]
        adj = [ (x+dx,y+dy) for dx in [-1,0,+1] for dy in [-1,0,+1] if not (dx==0 and dy==0) and self.is_valid_xy((x+dx,y+dy)) ]
        return adj

    def inc_adj_xy(self, xy: tuple, inc=1):
        for xy in self.adjanced_xy(xy):
            e = self.get_xy(xy)
            self.set_xy(xy, e+inc)

    def iterate_xy(self):
        for y in range(len(self.energy)):
            for x in range(len(self.energy[y])):
                yield (x,y)

    def print(self, step:int):
        print("=== step: %d ===" % step)
        for row in self.energy:
            print(' '.join([ '*' if i==0 else '%s' % i for i in row]))
        print

    def build_energy_map(self, input:list):
        self.energy = []
        for line in input:
            self.energy.append(list(map(int, list(line))))

    def flash_xy(self, xy: tuple):
        self.inc_adj_xy(xy)
        self.set_xy(xy, 0)

    def find_flash_ready(self, threshold=10):
        ready = []
        for xy in self.iterate_xy():
            energy = self.get_xy(xy)
            if energy>=threshold:
                ready.append(xy)
        return ready

    def energy_inc(self, inc=1):
        flash = []
        for xy in self.iterate_xy():
            energy = self.get_xy(xy) + inc
            self.set_xy(xy, energy)
            if energy>9:
                flash.append(xy)
        return flash

    def flash(self, ready: list):
        #ready = self.find_flash_ready()
        if len(ready)==0: return 0
        for xy in ready:
            self.inc_adj_xy(xy)
        for xy in ready:
            self.set_xy(xy, 0)
        re = self.find_flash_ready()
        re_cnt = self.flash(re)
        for xy in ready + re:
            self.set_xy(xy, 0)
        return len(ready) + len(re)

    def single_step(self):
        f = self.energy_inc()
        return self.flash(f)

    def count_flashes(self, steps:int):
        cnt = 0
        for s in range(steps):
            if verbose: self.print(step=s)
            c = self.single_step()
            count0 = len([ xy for xy in self.iterate_xy() if self.get_xy(xy) == 0 ])
            cnt += count0
        if verbose:
            self.print(step=steps)
            print("cnt=",cnt)
        return cnt

    def task_a(self, input: list, steps=100):
        """ task A """
        self.build_energy_map(input)
        cnt = self.count_flashes(steps)
        return cnt

    def task_b(self, input: list):
        """ task B """
        return None


def testcase_a(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ line.strip() for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()

def testcase_b(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ line.strip() for line in input.splitlines() ]
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
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

testdataX = """
11111
19991
19191
19991
11111
"""

# ========
#  Task A
# ========

# test cases
testcase_a(OctoMap(), testdata,  1656)

# 1702
testcase_a(OctoMap(),   None,     1702)
