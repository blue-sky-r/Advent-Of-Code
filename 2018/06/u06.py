#!/usr/bin/env python

__motd__ = '--- Day 6: Chronal Coordinates  ---'

__url__ = 'http://adventofcode.com/2018/day/6'


verbose = 0


class DistMap:

    def __init__(self, size=10):
        self.size = size
        self.point = {}
        #self.grid = dict([ (x,y) for x in range(size) for y in range(size) ])
        self.grid = {}

    def show(self, grid):
        """ visualize """
        print
        for y in range(self.size):
            for x in range(self.size):
                print grid[(x,y)],
            print

    def manhattan_distance(self, a, b):
        """ calc manhattan distance """
        return sum([ abs(b[i] - a[i]) for i in range(2) ])

    def closest_points(self, herexy):
        """ """
        distto = {}
        for id,xy in self.point.items():
            distto[id] = self.manhattan_distance(herexy, xy)
        if verbose: print "closest_points(",herexy,") -> ",distto,
        mindstidx = min(distto, key=distto.get)
        points =  [ pnt for pnt,dst in distto.items() if dst == distto[mindstidx] ]
        if verbose: print ' min:',points
        return points

    def grid_distances(self):
        """ """
        for y in range(self.size):
            for x in range(self.size):
                dist = self.closest_points(herexy=(x,y))
                self.grid[(x,y)] = dist
        return

    def calc_areas(self):
        """ clc all areas on limited grid """
        area = {}
        for xy, points in self.grid.items():
            # skip if xy has the same dist to more than one point
            if len(points) > 1: continue
            key = points[0]
            area[key] = area.get(key, 0) + 1
        if verbose: print "calc_areas()",area
        return area

    def area_no_inf(self, area):
        # elmiminate infinite areas
        for i in range(self.size):
            # iterate borders: left right bottom top
            for xy in [(0, i), (self.size - 1, i), (i, 0), (i, self.size - 1)]:
                # remove
                pnt = self.grid[xy]
                if len(pnt) > 1: continue
                point = pnt[0]
                if point in area: del area[point]
        # area without infinites
        if verbose: print "area_no_inf()", area
        return area

    def find_max_area(self, area):
        # max
        maxidx = max(area, key=area.get)
        if verbose: print "find_max_area() ",area[maxidx]
        return area[maxidx]

    def sum_dist(self, limit):
        """ find points with sum manhattan distance less than limit """
        #area = self.grid_distances()

        return

    def add_point(self, str):
        """ add point coordinates x, y """
        xy = tuple([ int(p) for p in str.split(", ") ])
        key = max(self.point.keys()) if len(self.point) > 0 else 0
        self.point[key+1] = xy
        return xy

    def input_line(self, str):
        """ x, y """
        return self.add_point(str)

    def task_a(self, input):
        """ task A """
        for line in input:
            self.input_line(line)
        self.grid_distances()
        if verbose: self.show(self.grid)
        a = self.area_no_inf( self.calc_areas() )
        return self.find_max_area(a)

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
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
"""
# test cases
testcase(DistMap(), data.strip().split('\n'), 17)
# 3722
testcase(DistMap(size=500), None, 3722)
xxx
#
testcase((), None, 1)

# ========
#  Task B
# ========

# test cases
testcase((), ['', '', '', ''],            2, task_b=True)

# [1m 34s] 56360
testcase((), None, 2, task_b=True)
