#!/usr/bin/env python3

__day__  = 15

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-15'

verbose = 0


class Hash:

    def __init__(self):
        pass

    def calc_hash(self, s: str) -> int:
        """ calc hash of a string s """
        current = 0
        for c in s:
            current += ord(c)
            current *= 17
            current %= 256
        return current

    def find_label_in_box(self, box: list, label: str) -> list:
        """ find index of label in a box (label, focal_length) """
        found = [ idx for idx,lbfl in enumerate(box) if lbfl[0] == label ]
        return found

    def parse_instruction(self, boxes: dict, instruction: str) -> dict:
        """ update boxes based on instruction """
        # remove lens
        if instruction.endswith('-'):
            label = instruction[:-1]
            boxidx = self.calc_hash(label)
            box = boxes.get(boxidx, [])
            for idx in self.find_label_in_box(box, label):
                del box[idx]
        # add/replace lens
        if '=' in instruction:
            label, focallengthstr = instruction.split('=')
            boxidx = self.calc_hash(label)
            focallength = int(focallengthstr)
            box = boxes.get(boxidx, [])
            idxs = self.find_label_in_box(box, label)
            if len(idxs) == 0:
                box.append((label, focallength))
            else:
                for idx in idxs:
                    box[idx] = (label, focallength)
            boxes[boxidx] = box
        return boxes

    def focusing_power(self, boxes: dict) -> int:
        """ calc focusing power """
        fp = []
        for id,box in boxes.items():
            vals = [ (id+1) * (i+1) * lb_fp[1] for i,lb_fp in enumerate(box) ]
            v = sum(vals)
            fp.append(v)
        return fp

    def task_a(self, input: list):
        """ task A """
        hashes = []
        for instruction in input.split(','):
            h = self.calc_hash(instruction)
            hashes.append(h)
        return sum(hashes)

    def task_b(self, input: list):
        """ task B """
        boxes = {}
        for instruction in input.split(','):
            boxes = self.parse_instruction(boxes, instruction)
        fp = self.focusing_power(boxes)
        return sum(fp)


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

testdata = "HASH"

# ========
#  Task A
# ========

# test cases
#testcase_a(Hash(), testdata,  52)

testdata = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

# test cases
testcase_a(Hash(), testdata, 1320)

# 505379
testcase_a(Hash(),   None, 505379)

# ========
#  Task B
# ========

# test cases
testcase_b(Hash(), testdata, 145)

# 263211
testcase_b(Hash(),   None, 263211)
