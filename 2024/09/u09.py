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

    def defrag(self, bmap):
        """ defrag files in blockmap """

        def lastfile(files, fromidx):
            """ find the last file starting from fromidx """
            # skip free space
            while files[fromidx] == self.freesym and fromidx > 0:
                fromidx -= 1
            if fromidx == 0:
                return
            # file found
            fileid = files[fromidx]
            length = 0
            # calc file size
            while files[fromidx] == fileid and fromidx >= 0:
                fromidx -= 1
                length += 1
            return fileid, length, fromidx+1

        def findfreeareaforfile(files, length):
            """ find the first free area that can hold a file of length """
            found = 0
            for idx,s in enumerate(files):
                if s == self.freesym:
                    found += 1
                    if found == length:
                        return idx-length+1
                else:
                    found = 0

        def movefile(files, fromidx, toidx, length):
            """ move file from fromidx to toidx with length """
            for i in range(length):
                files[toidx+i] = files[fromidx+i]
                files[fromidx+i] = self.freesym
            return files

        lastidx = len(bmap)
        while lastidx > 0:
            self.visualize('blockmap:', bmap)
            fileid, length, lastidx = lastfile(bmap, lastidx-1)
            availidx = findfreeareaforfile(bmap, length)
            if availidx is not None and availidx < lastidx:
                bmap = movefile(bmap, lastidx, availidx, length)
        return bmap


    def checksum(self, compacted):
        """sum position * id"""
        blocks = [i * id for i, id in enumerate(compacted) if id != self.freesym]
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
        bmap = self.blockmap(input)
        self.visualize("blockmap:", bmap)
        defragmented = self.defrag(bmap)
        self.visualize("defragmented:", defragmented)
        csum = self.checksum(defragmented)
        return csum


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

# ========
#  Task B
# ========

# test cases
testcase(Filesystem(), input, 2858, task_b=True)

# [35s] 6237075041489
testcase(Filesystem(), None, 6237075041489, task_b=True)
