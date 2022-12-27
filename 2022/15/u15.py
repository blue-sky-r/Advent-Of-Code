#!/usr/bin/env python3

__day__  = 15

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

import re

verbose = 1


class BeaconExclusionZone:

    def __init__(self):
        pass

    def print(self, txt='', map=None):
        """ visualize map """
        if not verbose: return
        x = [ xy[0] for xy in map.keys() ] + [ xy[0] for xy in map.values() ]
        y = [ xy[1] for xy in map.keys() ] + [ xy[1] for xy in map.values() ]
        minx, maxx = min(x), max(x)
        miny, maxy = min(y), max(y)
        #
        if txt: print(txt)
        print('x', '\t', ''.join(['%1s' % int(col / 10) for col in range(minx, maxx+1)]))
        print('i', '\t', ''.join(['%1s' % (col % 10) for col in range(minx, maxx+1)]))
        for row in range(miny, maxy+1):
            r = [ 'S' if map.get((col,row)) else '.' for col in range(minx, maxx+1) ]
            print(row, '\t', ''.join(r))
        print()

    def print2(self, txt='', map=None):
        """ visualize map """
        if not verbose: return
        x = [ xy[0] for xy in map.keys() ]
        y = [ xy[1] for xy in map.keys() ]
        minx, maxx = min(x), max(x)
        miny, maxy = min(y), max(y)
        #
        if txt: print(txt)
        print('x', '\t', ''.join(['%1s' % int(col / 10) for col in range(minx, maxx+1)]))
        print('i', '\t', ''.join(['%1s' % (col % 10) for col in range(minx, maxx+1)]))
        for row in range(miny, maxy+1):
            r = [ map.get((col,row), '.') for col in range(minx, maxx+1) ]
            print(row, '\t', ''.join(r))
        print()

    def coverage(self):
        """ fill coverage to the map """
        covermap = {}
        for sensorxy, beaconxy in self.sbmap.items():
            if verbose: print('sensor', sensorxy, 'beacon', beaconxy, 'size of coverage map is', len(covermap))
            d = self.manhattan_dist(sensorxy, beaconxy)
            covermap.setdefault(sensorxy, 'S')
            covermap.setdefault(beaconxy, 'B')
            for xy in self.manhattan_square(sensorxy, d):
                covermap.setdefault(xy, '#')
        return covermap

    def manhattan_dist(self, sensorxy, beaconxy):
        """ calc hamming distance between sensor (xy0 to the closest beacon (xy) """
        dx, dy = beaconxy[0] - sensorxy[0], beaconxy[1] - sensorxy[1]
        return abs(dx) + abs(dy)

    def manhattan_square(self, centerxy, d: int):
        """ generate all xy within manhattan distance d from center xy """
        for r in range(1, d+1):
            for x in range(-r, r+1):
                for y in range(-r, r+1):
                    xy = centerxy[0]+x, centerxy[1]+y
                    if self.manhattan_dist(centerxy, xy) > d: continue
                    yield xy

    def parse(self, input: list):
        """ parse string list input """
        # sensor -> beacon
        sbmap = {}
        for idx, line in enumerate(input):
            sensorxy, beaconxy = self.parse_line(line)
            if sensorxy is None or beaconxy is None:
                print('ERR parsing line:', idx+1, ':', line)
                continue
            sbmap[sensorxy] = beaconxy
        return sbmap

    def parse_line(self, line: str):
        """ parse: Sensor at x=2, y=18: closest beacon is at x=-2, y=15 """
        m = re.match('Sensor at x=(?P<sx>-?\d+), y=(?P<sy>-?\d+): closest beacon is at x=(?P<bx>-?\d+), y=(?P<by>-?\d+)', line)
        if not m: return None, None
        sensorxy = (int(m['sx']), int(m['sy']))
        beaconxy = (int(m['bx']), int(m['by']))
        return sensorxy, beaconxy

    def count_nosignal_at_row(self, cmap, row: int):
        """ """
        r = [ cmap.get(xy) for xy in cmap.keys() if xy[1] == row  ]
        return r.count('#')

    def task_a(self, input: list, result):
        """ task A """
        # sensor -> beacon
        self.sbmap = self.parse(input)
        #self.print('sensors', self.sbmap)
        cmap = self.coverage()
        #self.print2('coverage', cmap)
        return self.count_nosignal_at_row(cmap, result[0])

    def task_b(self, input: list):
        """ task B """
        return None


def testcase_a(sut, input, result, trim=str.rstrip):
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
    r = sut.task_a(input, result)
    print('\t got:',r,'\t','[ OK ]' if r == result[1] else '[ ERR ]')
    print()

def testcase_b(sut, input, result, trim=str.rstrip):
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
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

# ========
#  Task A
# ========

# test cases
testcase_a(BeaconExclusionZone(), testdata,  (10, 26))

# ?
testcase_a(BeaconExclusionZone(),  None, (2000000, 1))


