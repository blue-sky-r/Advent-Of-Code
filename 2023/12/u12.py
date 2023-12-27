#!/usr/bin/env python3

__day__  = 12

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-12'

import datetime

verbose = 0


class HotSprings:

    def __init__(self):
        pass

    def val_to_str(self, val: int, length: int, symbols='.#'):
        """ create bitwise string from decimal value val using bit symbols """
        binstr = f'{val:0{length}b}'
        symstr = binstr.replace('0', symbols[0]).replace('1', symbols[1])
        return symstr

    def replace_mask(self, line: str, replace: str, mask: str = '?') -> str:
        """ replace q-marks in line with bit-symbols string """
        r, ridx = [], 0
        for c in line:
            if c == mask:
                r.append(replace[ridx])
                ridx += 1
            else:
                r.append(c)
        return ''.join(r)

    def line_count_symbol(self, line: str, symbol='#') -> list:
        """ count group of symbols """
        counts, cnt = [], 0
        for c in line:
            if c == symbol:
                cnt += 1
                continue
            if cnt > 0:
                counts.append(cnt)
                cnt = 0
        if cnt > 0:
            counts.append(cnt)
        return counts

    def line_match_nums(self, line: str, nums: list) -> bool:
        """ verify the line match numerals """
        counts = self.line_count_symbol(line)
        return counts == nums

    def brute_force_pattern_match(self, mask: str, nums: list):
        """ replace ? with all possible variants to find a match """
        match, qmarks, hmarks, htotal = [], mask.count('?'), mask.count('#'), sum(nums)
        for val in range(2**qmarks):
            replacement = self.val_to_str(val, qmarks)
            # skip invalid replacements
            if replacement.count('#') + hmarks != htotal:
                continue
            aline = self.replace_mask(mask, replacement)
            # validate number of parts ##..#.#..
            if len([ p for p in aline.split('.') if p ]) != len(nums):
                continue
            if self.line_match_nums(aline, nums):
                match.append(aline)
        return match

    def parse_line(self, line: str) -> tuple:
        """ ???.### 1,1,3 -> tuple(str, list) """
        graph, num = line.split()
        listnum = [ int(i) for i in num.split(',') ]
        return graph, listnum

    def parse_line_5x(self, line: str) -> tuple:
        """ ???.### 1,1,3 -> tuple(str, list) """
        graph, num = line.split()
        listnum = [ int(i) for i in num.split(',') ]
        return '?'.join(5 * [graph]), 5 * listnum

    def task_a(self, input: list):
        """ task A """
        matches = []
        for line in input:
            graph, nums = self.parse_line(line)
            match = self.brute_force_pattern_match(graph, nums)
            matches.append(len(match))
        return sum(matches)

    def task_b(self, input: list):
        """ task B """
        matches = []
        for line in input:
            graph, nums = self.parse_line_5x(line)
            match = self.brute_force_pattern_match(graph, nums)
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), line, ' ... matches:', len(match))
            matches.append(len(match))
        return sum(matches)


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
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

# ========
#  Task A
# ========

# test cases
testcase_a(HotSprings(), testdata, 21)

# [16s] 7771
testcase_a(HotSprings(),   None, 7771)

# ========
#  Task B
# ========

# test cases
testcase_b(HotSprings(), testdata, 525152)

# 2
#testcase_b(C(),   None,    2)
