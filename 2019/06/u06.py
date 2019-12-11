#!/usr/bin/env python

__motd__ = '--- Day 6: Universal Orbit Map ---'

__url__ = 'http://adventofcode.com/2019/day/6'

import math

verbose = 1


class Planet:

    def __init__(self, name):
        self.name = name
        self.orbiters = []

    def add_orbiter(self, planet):
        self.orbiters.append(planet)
        return self

    def has_orbiters(self):
        return len(self.orbiters) > 0


class UniOrbMap:

    def __init__(self):
        self.map = None

    def show(self, segment=None, intend=1):
        """ show map """
        if segment is None: segment = self.map
        if segment is None: return
        planet = segment.name
        for o in segment.orbiters:
            print ' ' * 4 * intend, planet, ')', o.name
            self.show(o, intend+1)

    def planets(self, segment=None):
        """ get all planet names in map segment (none=entire map) """
        if segment is None: segment = self.map
        if segment is None: return []
        parts = [ segment.name ]
        for o in segment.orbiters:
            parts += self.planets(o)
        return parts

    def find_planet(self, name, segment=None):
        """  find planet by name in map segment (none = entire map) """
        if segment is None: segment = self.map
        if segment is None: return
        if segment.name == name: return segment
        for orbiter in segment.orbiters:
            found = self.find_planet(name, orbiter)
            if found: return found

    def from_list(self, los):
        """ create map from list of strings p)o planet->orbiter"""
        while len(los) > 0:
            print len(los),
            # get the first planet
            planet,orbiter  = los[0].split(')')
            # empty map - just add planet+orbiter
            if self.map is None:
                self.map = Planet(planet).add_orbiter(Planet(orbiter))
                del los[0]
                continue
            found = self.find_planet(planet)
            if found:
                found.add_orbiter(Planet(orbiter))
                del los[0]

    def find_depth(self, name, segment=None, depth=0):
        """ get depth for planet name inamap segment  """
        segment = segment if segment else self.map
        if segment is None: return False, depth
        if segment.name == name: return True, depth
        for o in segment.orbiters:
            found, d = self.find_depth(name, o, depth+1)
            if found: return True, d
        return False, depth

    def walk(self, segment=None, depth=0):
        """  walk the map segment """
        segment = segment if segment else self.map
        if segment is None: return depth
        if not segment.has_orbiters(): return depth
        parts = []
        for o in segment.orbiters:
            parts.append(self.walk(o, depth+1))
        if verbose: print segment.name, [ o.name for o in segment.orbiters ], parts
        return sum(parts)

    def count_orbits(self):
        """ count depths for all planets """
        return sum([ self.find_depth(name)[1] for name in self.planets() ])

    def task_a(self, input):
        """ task A """
        self.from_list(input)
        if verbose: self.show()
        return self.count_orbits()

    def task_b(self, input):
        """ task B """
        if type(input) == list:
            for i in input:
                self.add_module_with_fuel(i)
        else:
            self.add_module_with_fuel(input)
        return int(self.fuel)


def testcase(sut, input, result, task_b=False):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    else:
        input = input.split(' ')
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

#         G - H       J - K - L
#        /           /
# COM - B - C - D - E - F
#                \
#                 I
#
data = "COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L"
# test cases
testcase(UniOrbMap(),     data,     42)

#
testcase(UniOrbMap(), None, 42)

# ========
#  Task B
# ========
