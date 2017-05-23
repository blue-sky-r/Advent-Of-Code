#!/usr/bin/env python

__motd__ = '--- Day 7: Internet Protocol Version 7 ---'

__url__ = 'http://adventofcode.com/2016/day/7'

verbose = 0

import re

class IPv7:

    def __init__(self):
        pass

    def address(self, str):
        " parse IPv7 str address into parts "
        self.addr = str.strip()
        # hypernet
        self.hypernet = re.findall(r'\[[a-z]+\]', self.addr)
        # abba
        self.abba = self.findall_abba_overlap(self.addr)
        # bab
        self.bab =  self.findall_xyx(self.hypernet)
        # supernet
        self.supernet = re.split(r'\[[a-z]+\]', self.addr)
        # aba
        self.aba =  self.findall_xyx(self.supernet)
        # only for debug, not used in task solution
        self.xyx = self.findall_xyx(self.addr)
        #
        return self

    def findall_xyx(self, iterable):
        " get xyx patterns from iterable (string or list) "
        if type(iterable) is list:
            l = []
            for el in iterable:
                l += self.findall_xyx_overlap(el)
            return l
        if type(iterable) is str:
            return self.findall_xyx_overlap(iterable)

    def findall_xyx_nonoverlap(self, iterable):
        " re.findall() returns only non-overlapping matches "
        if type(iterable) is list:
            return [ xyx[0] \
                     for item in iterable \
                        for xyx in re.findall(r'(([a-z])([a-z])\2)', item) \
                            if xyx[1] != xyx[2] \
                   ]
        if type(iterable) is str:
            return [ xyx[0] \
                     for xyx in re.findall(r'(([a-z])([a-z])\2)', iterable) \
                        if xyx[1] != xyx[2] \
                   ]

    def findall_xyx_overlap(self, str):
        " returns also overlapping triplets xyx "
        xyx = []
        for c1,c2,c3 in zip(str,str[1:],str[2:]):
            if c1 == c3 and c1 != c2 and c2 not in ['[',']']:
                xyx.append("%c%c%c" % (c1,c2,c3))
        return xyx

    def findall_abba_overlap(self, str):
        " returns also overlapping quadruplets abba "
        abba = []
        for c1,c2,c3,c4 in zip(str,str[1:],str[2:],str[3:]):
            if c2 == c3 and c1 == c4 and \
            c1 != c2 and c1 not in ['[',']'] and c2 not in ['[',']']:
                abba.append("%c%c%c%c" % (c1,c2,c3,c4))
        return abba

    def print_parts(self):
        " for debug only "
        print "IPv7 address:",self.addr
        print "\t","[hypernet]:",self.hypernet
        print "\t","Supernet:",self.supernet
        print "\t","ABBA:",self.abba
        print "\t","BAB: ",self.bab
        print "\t","ABA: ",self.aba
        print "\t","ANY xyx: ",self.xyx

    def TLS_supported(self):
        " checks if TLS is supported "
        if not self.abba: return False
        for abba in self.abba:
            if any(abba in ht for ht in self.hypernet): return False
        return True

    def SSL_supported(self):
        " checks if SSL is supported "
        if not self.bab: return False
        for bab in self.bab:
            aba = "%c%c%c" % (bab[1],bab[0],bab[1])
            if any(aba in sn for sn in self.supernet): return True
        return False

def testcase(input, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input:",input,"\t expected result:",result,
    ip = IPv7()
    ip.address(input)
    r = ip.SSL_supported() if b else ip.TLS_supported()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    if verbose: ip.print_parts()
    print

# ========
#  Task A
# ========

# test cases
testcase('abba[mnop]qrst', True)
testcase('abcd[bddb]xyyx', False)
testcase('aaaa[qwer]tyui', False)
testcase('ioxxoj[asdfgh]zxcvbn', True)

data = __file__.replace('.py', '.input')
ok = 0
ip  = IPv7()
with open(data) as f:
    for line in f:
        if not line: continue
        r = ip.address(line).TLS_supported()
        if r: ok += 1
        if verbose: print line.strip(),"\t","YES" if r else "NO"
# 115
print 'Task A input file:',data,'Result:',ok
print

# ========
#  Task B
# ========

# test cases
testcase('aba[bab]xyz',   True,  b=True)
testcase('xyx[xyx]xyx',   False, b=True)
testcase('aaa[kek]eke',   True,  b=True)
testcase('zazbz[bzb]cdb', True,  b=True)

ok = 0
ip  = IPv7()
with open(data) as f:
    for line in f:
        if not line: continue
        r = ip.address(line).SSL_supported()
        if r: ok += 1
        if verbose: print line.strip(),"\t","YES" if r else "NO"
# 231
print 'Task B input file:',data,'Result:',ok
print