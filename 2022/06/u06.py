#!/usr/bin/env python3

__day__  = 6

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class TuningTrouble:

    def __init__(self):
        pass

    def is_marker(self, str):
        """ validate if string s is marker (each char is exactly once) """
        once = [ str.count(c) == 1 for c in str ]
        return all(once)

    def start_of_marker(self, input, marklen=4):
        """ find 1st position of SOP """
        for idx in range(len(input)-marklen):
            sop = input[idx:idx+marklen]
            if self.is_marker(sop):
                return idx+marklen

    def task_a(self, input: list):
        """ task A """
        return self.start_of_marker(input, marklen=4)

    def task_b(self, input: list):
        """ task B """
        return self.start_of_marker(input, marklen=14)


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

# ========
#  Task A
# ========

# test cases
testcase_a(TuningTrouble(), "mjqjpqmgbljsphdztnvjfqwrcgsmlb",     7)
testcase_a(TuningTrouble(), "bvwbjplbgvbhsrlpgdmjqwftvncz",       5)
testcase_a(TuningTrouble(), "nppdvjthqldpwncqszvftbrmjlhg",       6)
testcase_a(TuningTrouble(), "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10)
testcase_a(TuningTrouble(), "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",  11)

# 1909
testcase_a(TuningTrouble(),   None,    1909)

# ========
#  Task B
# ========

# test cases
testcase_b(TuningTrouble(), "mjqjpqmgbljsphdztnvjfqwrcgsmlb",    19)
testcase_b(TuningTrouble(), "bvwbjplbgvbhsrlpgdmjqwftvncz",      23)
testcase_b(TuningTrouble(), "nppdvjthqldpwncqszvftbrmjlhg",      23)
testcase_b(TuningTrouble(), "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29)
testcase_b(TuningTrouble(), "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",  26)

# 3380
testcase_b(TuningTrouble(),   None,   3380)
