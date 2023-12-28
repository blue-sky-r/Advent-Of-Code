#!/usr/bin/env python3

__day__  = 13

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-13'

verbose = 0


class Reflections:

    def __init__(self):
        pass

    def transpose(self, m: list) -> list:
        """ transpose matrix m """
        transposed = []
        for col in range(len(m[0])):
            trow = ''.join([ row[col] for row in m ])
            transposed.append(trow)
        return transposed

    def find_vertical_reflection(self, pattern: list) -> int:
        """ find vertical reflection """
        tpattern = self.transpose(pattern)
        x = self.find_horizontal_reflection(tpattern)
        return x

    def find_horizontal_reflection(self, pattern: list) -> int:
        """ find horizontal reflection """
        for y, line01 in enumerate(zip(pattern, pattern[1:])):
            # cut line found ?
            if line01[0] == line01[1]:
                # verify more lines
                for line0, line1 in zip(pattern[y+2:], reversed(pattern[:y])):
                    if line0 != line1:
                        break
                else:
                    return y

    def summarize(self, reflections: list) -> int:
        """ summarize all reflections: 10 * y1 + x1 """
        s = [ 100 * (y+1 if y is not None else 0) + (x+1 if x is not None else 0) for x,y in reflections ]
        return sum(s)

    def find_reflections(self, patterns: list) -> list:
        """ find h/v reflections for all patterns """
        r = []
        for pattern in patterns:
            yreflection = self.find_horizontal_reflection(pattern)
            xreflection = self.find_vertical_reflection(pattern)
            r.append((xreflection,yreflection))
        return r

    def parse_patterns(self, input: list) -> list:
        """ nuild list of patterns """
        patterns, pattern = [], []
        for line in input:
            if not line:
                if pattern:
                    patterns.append(pattern)
                    pattern = []
                continue
            pattern.append(line)
        if pattern:
            patterns.append(pattern)
        return patterns

    def task_a(self, input: list):
        """ task A """
        patterns = self.parse_patterns(input)
        reflections = self.find_reflections(patterns)
        r = self.summarize(reflections)
        return r

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
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Reflections(), testdata, 405)

# 33520
testcase_a(Reflections(),   None, 33520)

