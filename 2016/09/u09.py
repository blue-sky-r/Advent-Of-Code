#!/usr/bin/env python

__motd__ = '--- Day 9: Explosives in Cyberspace ---'

__url__ = 'http://adventofcode.com/2016/day/9'

verbose = 0

import re

class Decompress:

    BoM = '('   # Begin of Marker
    EoM = ')'   # End of Marker

    def __init__(self):
        self.trace = []

    def string(self, str, recurs=False):
        " decompress string $str with markers (12x34) -> returns string"
        r = []
        for c in self.decode_recurs(str, recurs, lengthonly=False):
            r.append(c)
        return ''.join(r)

    def length(self, str, recurs=True):
        " calculate decompressed string $str length only -> returns length"
        return self.decode_recurs(str, recurs, lengthonly=True)

    def decode_recurs(self, str, recurs=True, lengthonly=False):
        " decompress recursively iterable $str with markers (12x34)ABC"
        if verbose: self.trace.append('#Dec:%s' % ''.join(str))
        length,repeat = 0,0; buff = []
        r = 0 if lengthonly else []
        for c in str:
            # collect sequence up to $length into $buff
            if length and repeat:
                buff, done = self.collect_n(c, buff, length)
                if done:
                    generated = self.repeat_it_n(buff, repeat)
                    r += self.decode_recurs(generated, recurs, lengthonly) if recurs \
                        else (len(generated) if lengthonly else generated)
                    length,repeat = 0,0; buff = []
                continue
            # begin of the marker
            if c ==  self.BoM:
                buff = [ self.BoM ]
                continue
            # parse marker
            if buff:
                buff, done = self.collect_marker(c, buff)
                if done:
                    length, repeat = self.marker_axb(buff)
                    # invalid marker - just pass it to output
                    if not length or not repeat:
                        r += len(buff) if lengthonly else buff
                    buff = []
                continue
            # copy
            if lengthonly:
                r += 1
            else:
                r.append(c)
                if verbose: self.trace.append(c)
        #
        return r

    def collect_marker(self, c, lst):
        " collect to $lst buffer marker up to EoM character"
        lst.append(c)
        return lst, c == self.EoM

    def collect_n(self, c, lst, n=1):
        " collect $n items to $lst buffer"
        lst.append(c)
        return lst, len(lst) == n

    def marker_axb(self, lst):
        " parse marker $lst - format (AxB) "
        m = re.match(r'\((\d+)x(\d+)\)', ''.join(lst))
        if m:
            length = int(m.group(1))
            repeat = int(m.group(2))
            if verbose: self.trace.append("#Mark:%s len:%d rep:%d" % (''.join(lst), length, repeat))
            return length, repeat
        return None, None

    def repeat_it_n(self, it, n=1):
        ' generate $n times buffer $it '
        if verbose: self.trace.append("#Rep %dx:%s" % (n,''.join(it)))
        return [ c for i in range(n) for c in it ]


def testcase(input, result=None, resultlen=None, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input:",input,"\t",
    deco = Decompress()
    if result:
        print "expected result:",result,
        r = deco.string(input, recurs=True) if b else deco.string(input, recurs=False)
        print 'got:',r,'OK' if r == result else 'ERR'
    if resultlen:
        print "\t","expected length:",resultlen,
        l = deco.length(input, recurs=True) if b else deco.length(input, recurs=False)
        print 'got:',l, 'OK' if l == resultlen else 'ERR'
    if verbose: print "Trace:",deco.trace
    print

# ========
#  Task A
# ========

# test cases
testcase('ADVENT',              'ADVENT',   6)
testcase('A(1x5)BC',            'ABBBBBC',  7)
testcase('(3x3)XYZ',            'XYZXYZXYZ',9)
testcase('A(2x2)BCD(2x2)EFG',   'ABCBCDEFEFG',11)
testcase('(6x1)(1x3)A',         '(1x3)A',       6)
testcase('X(8x2)(3x3)ABCY',     'X(3x3)ABC(3x3)ABCY',18)

data = __file__.replace('.py', '.input')
deco = Decompress()
with open(data) as f:
    str = f.read().strip()
l = deco.length(str, recurs=False)
# 99145
print 'Task A input file:',data,'Result:',l
if verbose: print 'Trace:',deco.trace
print

# ========
#  Task B
# ========

# test cases
testcase('ADVENT',                                                      'ADVENT', 6,  b=True)
testcase('X(8x2)(3x3)ABCY',                                             'XABCABCABCABCABCABCY', 20, b=True)
testcase('(27x12)(20x12)(13x14)(7x10)(1x12)A',                          None, 241920, b=True)
testcase('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN',    None, 445,    b=True)

deco = Decompress()
with open(data) as f:
    str = f.read().strip()
r = deco.length(str, recurs=True)
# 10943094568 run-time 1h30m
print 'Task A input file:', data, 'Result:', r
if verbose: print 'Trace:', deco.trace
print
