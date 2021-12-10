#!/usr/bin/env python3

__day__  = 8

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Digit:

    def __init__(self):
        pass




class Segments:

    def __init__(self):
        self.signal = []
        self.digits = []
        # value -> sorted on segments
        self.val2segments = {
            0: 'abcefg',
            1: 'cf',
            2: 'acdeg',
            3: 'acdfg',
            4: 'bcdf',
            5: 'abdfg',
            6: 'abdefg',
            7: 'acf',
            8: 'abcdefg',
            9: 'abcdfg'
        }

    def segments_to_values(self):
        """ segment -> [values] """
        d = {}
        for segment in 'abcdefg':
            d[segment] = [ val for val,segments in self.val2segments.items() if segment in segments ]
        return d

    def process_input(self, input: list):
        for line in input:
            signal, value = line.split(' | ')
            self.signal.append([''.join(sorted(s)) for s in signal.split()])
            self.digits.append([''.join(sorted(v)) for v in value.split()])

    def count_digits_with_num_segments(self, num: int):
        r = [ digit for value in self.digits for digit in value if len(digit) == num ]
        return len(r)

    def count_digits(self, digits: list):
        return sum([self.count_digits_with_num_segments(len(self.val2segments[d])) for d in digits])

    def solve_by_segments_on(self, signal: list):
        """ [acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab] ->
            {abcdefg:[8] bcdef:[2,3,5] acdfg:[2,3,5] abcdf:[2,3,5] abd:[7] abcdef:[0,6,9] bcdefg:[0,6,9] abef:[4] abcdeg:[0,6,9] ab:[1]} """
        wiring = {}
        for s in signal:
            wiring[s] = [ val for val,segments in self.val2segments.items() if len(s) == len(segments) ]
        return wiring

    def segment_to_wire(self, signal, connected):
        """ find segment connection to wire """
        # { a: [0,2,3,5,6,7,8,9] ... }
        for segment, numbers in self.segments_to_values().items():
            # ship already connected
            if segment in connected:
                continue
            # possible variants (all - already connected)
            wireto = set('abcdefg') - set(connected.values())
            # {abcdefg:[8] bcdef:[2,3,5] acdfg:[2,3,5] abcdf:[2,3,5] abd:[7] abcdef:[0,6,9] bcdefg:[0,6,9] abef:[4] abcdeg:[0,6,9] ab:[1]}
            for wiredsegs, wiredvals in self.solve_by_segments_on(signal).items():
                if set(numbers) >= set(wiredvals):
                    wireto = wireto & set(wiredsegs)
                    if len(wireto) == 1:
                        return segment, wireto
                    if len(wireto) == 0:
                        break
        return None

    def wiring_solver(self, signal: list):
        """ [acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab] ->
            {ab:1 dab:7 eafb:4 acedgfb:8 cdfbe:5 gcdfa:2 fbcad:3 cefabd:9 cdfgeb:6 cagedb:0} """
        # segment -> wire_label
        connected = {}
        # repeat until all segments are connected
        while len(connected) < 7:
            segment, wireto = self.segment_to_wire(signal, connected)
            if wireto and len(wireto) == 1:
                connected[segment] = list(wireto)[0]
        #
        return connected

    def decode_value(self, wiring: dict, digits: list):
        """ {segment: wire} [cdfeb fcadb cdfeb cdbaf] -> 5353 """
        # build new segment wiring
        wire2val = {}
        for val,seg in self.val2segments.items():
            wires = ''.join(sorted([ wiring[s] for s in seg ]))
            wire2val[wires] = str(val)
        #
        return int(''.join([ wire2val[d] for d in digits ]))

    def values_solver(self):
        values = []
        for signal, digits in zip(self.signal, self.digits):
            wiring = self.wiring_solver(signal)
            value = self.decode_value(wiring, digits)
            values.append(value)
        return values

    def task_a(self, input: list):
        """ task A """
        self.process_input(input)
        return self.count_digits([1, 4, 7, 8])

    def task_b(self, input: list):
        """ task B """
        self.process_input(input)
        values = self.values_solver()
        return sum(values)


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
    if input.count('\n'):
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
    if input.count('\n'):
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
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce   
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Segments(), testdata,  26)

# 365
testcase_a(Segments(),   None,    365)

# ========
#  Task B
# ========

testdata2 = """
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
"""

# test cases
testcase_b(Segments(), testdata2, 5353)

# test cases
testcase_b(Segments(), testdata, 61229)

# 975706
testcase_b(Segments(),   None,    975706)
