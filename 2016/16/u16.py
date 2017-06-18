#!/usr/bin/env python

__motd__ = '--- Day 16: Dragon Checksum ---'

__url__ = 'http://adventofcode.com/2016/day/16'

verbose = 0

class DragonCurve:

    def __init__(self, iv):
        " store iv and init result as list "
        self.iv = iv
        self.result = list(iv)

    def checksum(self, length, lst=None):
        " calc checksum for length $length of lst (default result) "
        # default input
        if lst is None: lst = self.result[:length]
        # end of recursion if length is odd - make string from list
        if len(lst) % 2: return ''.join(lst)
        # reduce list
        r = [ '1' if a == b else '0' for a,b in zip(lst[:length-1:2], lst[1:length:2]) ]
        # recursion with reduced list
        return self.checksum(len(r), r)

    def as_str(self,glue=''):
        " get generated result list as string "
        return glue.join(self.result)

    def gen_len(self, length):
        " generate at least length 0/1 symbols "
        while len(self.result) < length:
            l = self.reverse(self.result)
            b = self.inverse(l)
            self.result.append('0')
            self.result += b
        return self

    def reverse(self, lst):
        " reverse list a,b,c->c,b,a"
        return lst[::-1]

    def inverse(self, lst):
        " iverse 0->1 and 1->0 in lst "
        # replace 0->x 1->0 x->1
        lst = self.replace('0','x', lst)
        lst = self.replace('1','0', lst)
        lst = self.replace('x','1', lst)
        return lst

    def replace(self, find, replace, lst):
        " find $find and replace to $replace in list $lst "
        return [ replace if item == find else item for item in lst ]


def testcase_data(input, result, b=False):
    " testcase for data generation  "
    print "TestCase Data",'B' if b else 'A',
    print "for input:",input,"\t expected result:",result,
    dc = DragonCurve(input)
    r = dc.gen_len(len(result)).as_str()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

def testcase_checksum(input, result, b=False):
    " testcase for checksum "
    print "TestCase Checksum",'B' if b else 'A',
    print "for input:",input,"\t expected result:",result,
    dc = DragonCurve(input)
    r = dc.checksum(len(input), input)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

def testcase(input, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input:",input,"\t expected result:",result,
    iv, length = input[0], input[1]
    dc = DragonCurve(iv)
    r = dc.gen_len(length).checksum(length)
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

# test cases
testcase_data('1',               '100')
testcase_data('0',               '001')
testcase_data('11111',           '11111000000')
testcase_data('111100001010',    '1111000010100101011110000')

testcase_checksum('110010110100', '100')

data = '10000'; length = 20
testcase((data, length), '01100')

mydata, mylength = '10111100110001111', 272
dc = DragonCurve(mydata)
r = dc.gen_len(mylength).checksum(mylength)
# 11100110111101110
print 'Task A input:',(mydata,mylength),'Result:',r
print

# ========
#  Task B
# ========

mydata, mylength = '10111100110001111', 35651584
dcb = DragonCurve(mydata)
r = dc.gen_len(mylength).checksum(mylength)
# 10001101010000101
print 'Task A input:',(mydata,mylength),'Result:',r
print
