#!/usr/bin/env python3

__day__  = 6

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-01'

verbose = 0


class BoatRace:

    def __init__(self):
        pass

    def travelled_distance(self, racetime: int, buttonpress: int) -> int:
        """ calc travelled distance for button press """
        if 0 < buttonpress < racetime:
            runtime = racetime - buttonpress
            return runtime * buttonpress
        return 0

    def travelled_distances(self, racetime: int) -> list:
        """ calc traveled distance up to time limit """
        dist = []
        for button in range(racetime):
            d = self.travelled_distance(racetime, button)
            dist.append(d)
        return dist

    def winning_button(self, racetime: int, record: int) -> list:
        """ winning button times for racetime """
        winningbuttontimes = [ button for button,dist in enumerate(self.travelled_distances(racetime)) if dist > record ]
        return winningbuttontimes

    def winning_button_cnt(self, racetime: int, record: int) -> int:
        """ only count of winning button times for racetime """
        cnt = 0
        for button in range(racetime):
            dist = self.travelled_distance(racetime, button)
            if dist > record:
                cnt += 1
        return cnt

    def parse(self, input: list) -> tuple:
        """ parse time and distance striings to lists """
        for line in input:
            # Time:      7  15   30
            if line.startswith('Time:'):
                _, timestr = line.split(':')
                ms = [ int(timems) for timems in timestr.split() ]
                continue
            # Distance:  9  40  200
            if line.startswith('Distance:'):
                _, diststr = line.split(':')
                dist = [ int(d) for d in diststr.split() ]
                continue
        return ms, dist

    def parse_ignorespaces(self, input: list) -> tuple:
        """ parse time and distance striings to lists """
        for line in input:
            # Time:      7  15   30
            if line.startswith('Time:'):
                _, timestr = line.split(':')
                ms = int(timestr.replace(' ', ''))
                continue
            # Distance:  9  40  200
            if line.startswith('Distance:'):
                _, diststr = line.split(':')
                dist = int(diststr.replace(' ', ''))
                continue
        return ms, dist

    def task_a(self, input: list):
        """ task A """
        r = 1
        racems, dist = self.parse(input)
        for race, record in zip(racems, dist):
            winningbuttontimes = self.winning_button(race, record)
            r = r * len(winningbuttontimes)
        return r

    def task_b(self, input: list):
        """ task B """
        racems, dist = self.parse_ignorespaces(input)
        cnt = self.winning_button_cnt(racems, dist)
        return cnt


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
Time:      7  15   30
Distance:  9  40  200
"""

# ========
#  Task A
# ========

# test cases
testcase_a(BoatRace(), testdata,  288)

# 303600
testcase_a(BoatRace(),   None, 303600)

# ========
#  Task B
# ========

# test cases
testcase_b(BoatRace(), testdata, 71503)

# 23654842
testcase_b(BoatRace(),   None, 23654842)
