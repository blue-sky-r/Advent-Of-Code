#!/usr/bin/env python3

__motd__ = '--- Day 11: Plutonian Pebbles ---'

__url__ = 'http://adventofcode.com/2024/day/11'

verbose = 0


class PuStones:

    def __init__(self):
        pass

    def parsestones(self, input) -> list[int]:
        input = input[0] if type(input) == list else input
        return [int(stone) for stone in input.split()]

    def rules(sefl, stone: int) -> list[int]:
        """ rules """
        # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1
        if stone == 0:
            return [ 1 ]
        # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones
        s = str(stone)
        l = len(s)
        if l % 2 == 0:
            # The left half of the digits are engraved on the new left stone,
            # and the right half of the digits are engraved on the new right stone
            h = l // 2
            left, right = s[:h],s[h:]
            return [int(left), int(right)]
        # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024
        v = 2024 * stone
        return [ v ]

    def blink1(self, stones) -> list:
        """ blink once """
        nstones = []
        for stone in stones:
            r = self.rules(stone)
            nstones.extend(r)
        return nstones

    def blink(self, stones, n) -> list[int]:
        for i in range(n):
            stones = self.blink1(stones)
        return stones

    def rulenx(self, stone, n):
        """ apply riule N-times]"""
        #print('rule Nx n:',n,'stone:',stone)
        # return length
        if n == 0:
            return len(stone) if type(stone) == list else 1
        # apply rules and recurs
        return sum([ self.rulenx(s, n-1) for s in self.rules(stone) ])

    def blinknx(self, stones, n):
        """ blink n-times to each items sep"""
        return sum([self.rulenx(stone, n) for stone in stones])

    def task_a(self, input):
        """ task A """
        stones = self.parsestones(input)
        stones = self.blink(stones, 25)
        return len(stones)

    def task_b(self, input):
        """ task B """
        stones = self.parsestones(input)
        length = self.blinknx(stones, 75)
        return length


def testcase(sut, input, result, task_b=False):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    #
    print(f"TestCase {"B" if task_b else "A"} ", end='')
    print(f"for input: {data if 'data' in vars() else input}", end='')
    print(f"\t expected result: {result} ", end='')
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    print(f"got: {r} \t {'[ OK ]' if r == result else '[ ERR ]'}")
    print()

# ========
#  Task A
# ========

#input = "0 1 10 99 999"
input = "125 17"
# test cases
testcase(PuStones(),  input,  55312)

# 224529
testcase(PuStones(),  None,  224529)

# ========
#  Task B
# ========

# test cases
testcase(PuStones(),  input,  0, task_b=True)

# [ didn't finish in 12h - improved algo needed ]
testcase(PuStones(),  None,  0, task_b=True)
