#!/usr/bin/env python3

__day__  = 5

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-05'

verbose = 0


class Map:

    def __init__(self, name: str):
        self.name = name
        self.ranges = []

    def addrangestring(self, line: str):
        """ dst src len as string """
        dst, src, size = line.split()
        return self.addrange(int(dst), int(src), int(size))

    def addrange(self, dst: int, src: int, size: int):
        """ add mapping range src -> dst with length size """
        r = {
            'srclo': src,
            'srchi': src + size - 1,
            'dstlo': dst,
            'dsthi': dst + size - 1
        }
        self.ranges.append(r)
        return self

    def translate(self, srcval: int) -> int:
        """ translate/map src value to destination """
        for r in self.ranges:
            if r['srclo'] <= srcval <= r['srchi']:
                offset = srcval - r['srclo']
                return r['dstlo'] + offset
        return srcval


class Gardener:

    def __init__(self):
        pass

    def find_location(self, seed: int, mappings: dict) -> int:
        """ find location for seed via mappings"""
        mapsequence = [
            'seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light',
            'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location'
        ]
        #if verbose: print('Seed: ', seed, end='. ')
        r = seed
        for m in mapsequence:
            r = mappings[m].translate(r)
            #if verbose: print(m, r, end='. ')
        #if verbose: print()
        return r

    def parse_almanac(self, input: list) -> tuple:
        """ parse string input """
        seeds, mappings, name = [], {}, None
        for line in input:
            if line.startswith('seeds:'):
                _, seedstxt = line.split(':')
                seeds = [ int(s) for s in seedstxt.split() ]
                continue
            if line.endswith('map:'):
                name, _ = line.split()
                mappings[name] = Map(name)
                continue
            if len(line) > 0 and name is not None:
                mappings[name].addrangestring(line)
                continue
            name = None
        return seeds, mappings

    def find_min_location(self, seeds: list, mappings: dict) -> int:
        """ find only min location """
        minloc = None
        for s,l in zip(seeds[::2], seeds[1::2]):
            for seed in range(s, s+l):
                loc = self.find_location(seed, mappings)
                if minloc is None:
                    minloc = loc
                else:
                    minloc = min(minloc, loc)
        return minloc

    def task_a(self, input: list):
        """ task A """
        seeds, mappings = self.parse_almanac(input)
        loc = [ self.find_location(seed, mappings) for seed in seeds ]
        return min(loc)

    def task_b(self, input: list):
        """ task B """
        seeds, mappings = self.parse_almanac(input)
        # this takes forever and consumes memory
        #loc = [ self.find_location(seed, mappings) \
        #        for s,l in zip(seeds[::2], seeds[1::2]) \
        #        for seed in range(s, s+l) ]
        #return min(loc)
        #
        minloc = self.find_min_location(seeds, mappings)
        return minloc


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
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
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
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Gardener(), testdata,  35)

# 51752125
testcase_a(Gardener(), None, 51752125)

# ========
#  Task B
# ========

# test cases
testcase_b(Gardener(), testdata, 46)

# 11h 52m 35s = 12634632
testcase_b(Gardener(),   None, 12634632)
