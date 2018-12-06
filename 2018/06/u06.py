#!/usr/bin/env python

__motd__ = '--- Day 6: Chronal Coordinates  ---'

__url__ = 'http://adventofcode.com/2018/day/6'


verbose = 0


class DistMap:

    def __init__(self, size=10, limit=32):
        self.size = size
        self.limit = limit
        self.point = {}

    def show_grid(self, grid):
        """ visualize """
        print
        for y in range(self.size):
            for x in range(self.size):
                print grid[(x,y)],
            print

    def manhattan_distance(self, a, b):
        """ calc manhattan distance """
        return sum([ abs(b[i] - a[i]) for i in range(2) ])

    def points_distance(self, herexy):
        """ calc distances to all points from herexy"""
        dist = dict([ (id, self.manhattan_distance(herexy, xy)) for id, xy in self.point.items() ])
        if verbose > 2: print 'points_distance(', herexy, ')',dist
        return dist

    def closest_points_distance(self, herexy):
        """ filterout only closest points distances """
        dist = self.points_distance(herexy)
        # closest
        mindstidx = min(dist, key=dist.get)
        # firter ou only closest - could be more than one
        points =  [ pnt for pnt,dst in dist.items() if dst == dist[mindstidx] ]
        if verbose > 1: print 'closest_points_distance(',herexy,')',points
        return points

    def grid_distances(self):
        """ calc all distances to all points for entire grid (xy) -> {pointa->dista, pointb->distb}"""
        grid = dict([ ( (x,y), self.points_distance((x, y)) ) for x in range(self.size) for y in range (self.size) ])
        return grid

    def grid_closest_distances(self):
        """ calc the distances to closest point(s) only for entire grid (x,y) -> [pointz,pointb] """
        grid = dict([ ( (x,y), self.closest_points_distance(herexy=(x, y)) ) for x in range(self.size) for y in range(self.size) ])
        return grid

    def calc_areas(self, grid):
        """ calc all areas on limited grid, skip points equidistant from more points """
        area = {}
        for xy, points in grid.items():
            # skip if xy has the same dist to more than one point
            if len(points) > 1: continue
            # get point id
            key = points[0]
            # count in
            area[key] = area.get(key, 0) + 1
        if verbose: print "calc_areas()",area
        return area

    def area_no_infinity(self, grid, area):
        """ remove infinite (grid borderline) areas from area """
        # elmiminate infinite areas
        for i in range(self.size):
            # iterate borders: left right bottom top
            for xy in [(0, i), (self.size - 1, i), (i, 0), (i, self.size - 1)]:
                # remove
                pnt = grid[xy]
                # skip equidistant points
                if len(pnt) > 1: continue
                # get point id
                point = pnt[0]
                # remove
                if point in area: del area[point]
        # area without infinites
        if verbose: print "area_no_inf()", area
        return area

    def find_max_area(self, area):
        # max
        maxidx = max(area, key=area.get)
        if verbose: print "find_max_area() ",area[maxidx]
        return area[maxidx]

    def sum_dist_le_limit(self, grid, limit=32):
        """ find points with sum manhattan distance less than limit """
        # summary distances (x,y) -> sum
        sumgrid = dict([ (xy, sum(dst.values())) for xy,dst in grid.items() ])
        # filter only sums bellow limit
        filteredsumgrid = dict([ (xy, summ) for xy,summ in sumgrid.items() if summ < limit ])
        return filteredsumgrid

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
        grid = self.grid_closest_distances()
        if verbose: self.show_grid(grid)
        area = self.area_no_infinity(grid, self.calc_areas(grid))
        return self.find_max_area(area)

    def task_b(self, input):
        """ task B """
        for line in input:
            self.input_line(line)
        grid = self.grid_distances()
        if verbose: self.show_grid(grid)
        r = self.sum_dist_le_limit(grid, limit=self.limit)
        return len(r)


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
testcase(DistMap(), data.strip().split('\n'),   17)
# [18s] 3722
testcase(DistMap(size=500), None, 3722)

# ========
#  Task B
# ========

# test cases
testcase(DistMap(limit=32), data.strip().split('\n'),   16, task_b=True)
# [18s] 44634
testcase(DistMap(size=500, limit=10000), None, 44634, task_b=True)
