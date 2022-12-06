#!/usr/bin/env python3

__day__  = 3

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Rucksack:

    def __init__(self):
        pass

    def common_item(self, rucksack):
        """ find common item in both rucksack compartments """
        half = int(len(rucksack)/2)
        compartment_a, compartment_b = rucksack[:half], rucksack[-half:]
        common = [ item for item in compartment_a if compartment_b.count(item) > 0 ]
        return ''.join(set(common))

    def chr_priority(self, c):
        """ calc item/character priority a-z -> 1-26 A-Z -> 27-52 """
        if 'a' <= c <= 'z': return ord(c) - ord('a') + 1
        if 'A' <= c <= 'Z': return ord(c) - ord('A') + 27

    def task_a(self, input: list):
        """ task A """
        common_items = [ self.common_item(rucksack) for rucksack in input ]
        common_items_priority = [ self.chr_priority(c) for c in common_items ]
        return sum(common_items_priority)

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
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Rucksack(), testdata,  157)

# 8252
testcase_a(Rucksack(),   None,   8252)

# ========
#  Task B
# ========

# test cases
#testcase_b(C(), testdata,  2)

# 2
#testcase_b(C(),   None,    2)
