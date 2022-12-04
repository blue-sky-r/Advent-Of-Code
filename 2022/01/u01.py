#!/usr/bin/env python3

__day__  = 1

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Calories:

    def __init__(self):
        pass

    def aggregate_calories(self, input):
        """ sum of calories per Elve """
        elve, calories, inventory = 1, [], {}
        for line in input:
            if not line:
                inventory[elve] = sum(calories)
                elve, calories = elve+1, []
                continue
            calories.append(int(line))
        inventory[elve] = sum(calories)
        return inventory

    def max_calories(self, calories: dict):
        """ return max calories """
        max_key = max(calories, key=lambda k: calories[k])
        return calories[max_key]

    def topN_calories(self, calories, top=3):
        """ sum of top N calories """
        calories_asc = sorted(calories, key=lambda k: calories[k])
        return sum([ calories[k] for k in calories_asc[-top:] ])

    def task_a(self, input: list):
        """ task A """
        inventory = self.aggregate_calories(input)
        return self.max_calories(inventory)

    def task_b(self, input: list):
        """ task B """
        inventory = self.aggregate_calories(input)
        return self.topN_calories(inventory)


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
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Calories(), testdata,  24000)

# 70509
testcase_a(Calories(),   None,    70509)

# ========
#  Task B
# ========

# test cases
testcase_b(Calories(), testdata,  45000)

# 208567
testcase_b(Calories(),   None,   208567)
