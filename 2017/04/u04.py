#!/usr/bin/env python

__motd__ = '--- Day 4: High-Entropy Passphrases ---'

__url__ = 'http://adventofcode.com/2017/day/4'


verbose = 0


class Passphrase:

    def valid_A(self, str):
        return not self.has_duplicates(str)

    def has_duplicates(self, str):
        words = str.split()
        for w in words:
            if words.count(w) > 1:
                if verbose: print "word:",w,"is more than once in passphrase:",str
                return True
        return False

    def valid_B(self, str):
        return not self.has_anagrams(str)

    def has_anagrams(self, str):
        normalized = ' '.join([ self.normalize_word(w) for w in str.split() ])
        return self.has_duplicates(normalized)

    def normalize_word(self, str):
        return ''.join(sorted(list(str)))


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    p = Passphrase()
    r = p.valid_B(input) if task_b else p.valid_A(input)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

testcase('aa bb cc dd ee',  True)
testcase('aa bb cc dd aa',  False)
testcase('aa bb cc dd aaa', True)

data = __file__.replace('.py', '.input')
p = Passphrase()
cnt = 0
with open(data) as f:
    for line in f:
        if not line: continue
        v = p.valid_A(line.strip())
        if v: cnt += 1
# 451
print 'Task A input file:',data,'Result:',cnt
print

# ========
#  Task B
# ========

testcase('abcde fghij',              True, task_b=True)
testcase('abcde xyz ecdab',         False, task_b=True)
testcase('a ab abc abd abf abj',     True, task_b=True)
testcase('iiii oiii ooii oooi oooo', True, task_b=True)
testcase('oiii ioii iioi iiio',     False, task_b=True)

p = Passphrase()
cnt = 0
with open(data) as f:
    for line in f:
        if not line: continue
        v = p.valid_B(line.strip())
        if v: cnt += 1
# 223
print 'Task B input file:',data,'Result:',cnt
print
