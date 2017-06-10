#!/usr/bin/env python

__motd__ = '--- Day 14: One-Time Pad ---'

__url__ = 'http://adventofcode.com/2016/day/14'

verbose = 0

import hashlib

class KeyPad:

    def __init__(self, salt, stretch=0):
        self.salt = salt
        self.stretch = stretch
        self.idx = 0

    def idx_salt(self, offset=0):
        " salt with integer index "
        return "%s%d" % (self.salt, self.idx+offset)

    def streched_md5(self, offset=0):
        " get stretched md5 hash with offsetted salt "
        md5 = hashlib.md5(self.idx_salt(offset=offset)).hexdigest()
        for i in range(self.stretch):
            md5 = hashlib.md5(md5).hexdigest()
        return md5

    def gen_stream(self):
        " generate stream of hashes "
        while True:
            md5 = self.streched_md5()
            yield md5
            self.idx += 1

    def get_nth_key_idx(self, n):
        " get N-th valid key salt index "
        for i,key in enumerate(self.gen_key()):
            if verbose: print "%03d. salt=%s key=%s" % (i+1, self.idx_salt(), key)
            if i+1 == n: return self.idx

    def gen_key(self):
        " valid key generator "
        for md5 in self.gen_stream():
            if self.is_key(md5): yield md5

    def check_next(self, l3, n=1000):
        " check next n (default 100) hashes "
        for i in range(1,n):
            md5 = self.streched_md5(offset=i)
            if self.has_5let(md5, l3):
                if verbose: print "\t 5-let:%s:%s:%s" % (l3, self.idx_salt(offset=i), md5)
                return True
        return False

    def is_key(self, key):
        " valid kay has 3-let and valid 5-let in next 1000 keys "
        l3 = self.has_3let(key)
        if l3 is None: return
        if verbose: print "\t 3-let:%s:%s:%s" % (l3, self.idx_salt(), key)
        if self.check_next(l3, n=1000):
            return key

    def has_3let(self, key):
        " get only the 1st 3-let "
        for idx in range(len(key)-2):
            l3 = key[idx:idx+3]
            if l3[0] == l3[1] == l3[2]:
                return l3

    def has_5let(self, key, l3):
        " check if key has 5-let "
        l5 = l3[0] * 5
        return l5 in key


def testcase(input, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input:",input,"\t expected result:",result,
    k = KeyPad(input, stretch=2016) if b else KeyPad(input)
    r = k.get_nth_key_idx(64)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

# test cases
tcdata = 'abc'
testcase(tcdata, 22728)

data = 'qzyelonm'
k = KeyPad(data)
r = k.get_nth_key_idx(64)
# 15168
print 'Task A input:',data,'Result:',r
print

# ========
#  Task B
# ========

# test cases
# (~ 1h)
testcase(tcdata, 22551, b=True)

k = KeyPad(data, stretch=2016)
r = k.get_nth_key_idx(64)
# 20864 (~ 1h 15m)
print 'Task B input:',data,'Result:',r
print
