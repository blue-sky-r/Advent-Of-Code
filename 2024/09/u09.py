#!/usr/bin/env python3

__motd__ = "--- Day 9: Disk Fragmenter ---"

__url__ = "http://adventofcode.com/2024/day/9"

verbose = 0


class Filesystem:

    def __init__(self):
        self.freesym = "."

    def visualize(self, label: str, bmap: list):
        if verbose == 0:
            return
        print(label, "".join(["%s" % c for c in bmap]))

    def blockmap(self, input) -> list:
        """represent the layout of files and free space"""
        bmap, id, used = [], 0, True
        for c in input:
            if used:
                bmap += [id] * int(c)
                id += 1
            else:
                bmap += [self.freesym] * int(c)
            used = not used
        return bmap

    def compact(self, bmap) -> list:
        """reuse free blocks"""
        compacted, idx, popidx = [], 0, len(bmap)
        while idx < popidx:
            if bmap[idx] == self.freesym:
                # pop
                while True:
                    popidx -= 1
                    s = bmap[popidx]
                    if s != self.freesym:
                        break
            else:
                s = bmap[idx]
            compacted.append(s)
            idx += 1
        return compacted

    def checksum(self, compacted):
        """sum position * id"""
        blocks = [i * id for i, id in enumerate(compacted)]
        return sum(blocks)

    def task_a(self, input):
        """task A"""
        bmap = self.blockmap(input)
        self.visualize("blockmap:", bmap)
        compacted = self.compact(bmap)
        self.visualize("compacted:", compacted)
        csum = self.checksum(compacted)
        return csum

    def task_b(self, input):
        """task B"""
        return


def testcase(sut, input, result, task_b=False):
    """testcase verifies if input returns result"""
    # read default input file
    if input is None:
        data = __file__.replace(".py", ".input")
        with open(data) as f:
            input = [line.strip() for line in f][0]
    #
    print(f"TestCase {"B" if task_b else "A"} ", end="")
    print(f"for input: {data if 'data' in vars() else input}", end="")
    print(f"\t expected result: {result} ", end="")
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    print(f"got: {r} \t {'[ OK ]' if r == result else '[ ERR ]'}")
    print()


# ========
#  Task A
# ========

input = "2333133121414131402"
# test cases
testcase(Filesystem(), input, 1928)

# 6216544403458
testcase(Filesystem(), None, 6216544403458)

