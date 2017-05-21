#!/usr/bin/env python

__motd__ = '--- Day 6: Signals and Noise ---'

__url__ = 'http://adventofcode.com/2016/day/6'

verbose = 0

class Signal:

    def __init__(self, msgfile):
        self.msgfile = msgfile

    def read_col(self, col):
        data = []
        with open(self.msgfile) as f:
            for line in f:
                if not line: continue
                if len(line) < col: continue
                data.append(line[col])
        return data

    def read_line(self, cnt=0):
        line = None
        with open(self.msgfile) as f:
            for row,line in enumerate(f):
                if row >= cnt: break
        return line

    def chr_freq(self, str):
        freq = {}
        for c in str:
            if c in freq: continue
            freq[c] = str.count(c)
        return freq

    def denoise_chr_dict(self, fdict, fnc=max):
        return fnc(fdict, key=fdict.get)

    def err_corrected(self, fnc=max):
        msg = []
        for idx,char in enumerate(self.read_line().strip()):
            col  = self.read_col(idx)
            if verbose: print "idx:",idx,"col:",''.join(col)
            freq = self.chr_freq(col)
            if verbose: print "idx:",idx,"freq:",freq
            msg.append(self.denoise_chr_dict(freq, fnc))
            if verbose: print "idx:",idx, "msg:",msg
        return ''.join(msg)


def testcase(input, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase","B" if b else "A",
    print "for input:",input,"\t expected result:",result,
    sig = Signal(input)
    r = sig.err_corrected(fnc=min if b else max)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

tcdata = __file__.replace('.py', '.tc.input')
data   = __file__.replace('.py', '.input')

# test cases
testcase(tcdata, 'easter')

#
sig = Signal(data)
r = sig.err_corrected()
# tkspfjcc
print 'Task A input file:',data,'Result:',r
print

# ========
#  Task B
# ========

# test cases
testcase(tcdata, 'advent', b=True)

#
sig = Signal(data)
r = sig.err_corrected(fnc=min)
# tkspfjcc
print 'Task A input file:',data,'Result:',r
print
