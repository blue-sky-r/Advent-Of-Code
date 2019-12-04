#!/usr/bin/env python

__motd__ = '--- Day 4: Secure Container ---'

__url__ = 'http://adventofcode.com/2019/day/4'

import math

verbose = 0


class Password:

    def __init__(self):
        """ init """
        self.lh = None

    def set_range(self, l_h):
        """ preset range from string L-H """
        l, h = l_h.split('-')
        self.lh = int(l), int(h)

    def validate_a(self, psw):
        """ validate password psw """
        # return self.is_Xdigit(psw) and self.has_double(psw) and self.is_inc(psw)
        return self.has_double(psw) and self.is_inc(psw)

    def validate_b(self, psw):
        """ validate password psw """
        # return self.is_Xdigit(psw) and self.has_double(psw) and self.is_inc(psw)
        return self.has_double(psw, exact=2) and self.is_inc(psw)

    def is_Xdigit(self, psw, x=6):
        """ It is a six-digit number """
        return len(psw) == x

    def has_double(self, psw, exact=None):
        """ Two adjacent digits are the same (like 22 in 122345) """
        for d in range(10):
            cnt = psw.count('%d' % d)
            if not exact and cnt > 1: return True
            if exact and cnt == exact: return True
        return False

    def is_inc(self, psw):
        """ from left to right, the digits never decrease """
        left = int(psw[0])
        for d in psw[1:]:
            if left > int(d): return False
            left = int(d)
        return True

    def all_psw(self):
        """ generate all valid passwords within range """
        for num in range(self.lh[0], self.lh[1]+1):
            yield "%d" % num

    def task_a(self, input):
        """ task A """
        if self.lh:
            cnt = 0
            for psw in self.all_psw():
                if self.validate_a(psw):
                    if verbose: print 'DBG: psw:', psw, 'OK'
                    cnt += 1
            return cnt
        return self.validate_a(input)

    def task_b(self, input):
        """ task B """
        if self.lh:
            cnt = 0
            for psw in self.all_psw():
                if self.validate_b(psw):
                    if verbose: print 'DBG: psw:', psw, 'OK'
                    cnt += 1
            return cnt
        return self.validate_b(input)


def testcase(sut, input, result, task_b=False):
    """ testcase verifies if input returns result """
    # read default input file
    if '-' in input:
        sut.set_range(input)
    #
    print "TestCase", "B" if task_b else "A",
    print "for input:", data if 'data' in vars() else input,
    print "\t expected result:", result,
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    print

# ========
#  Task A
# ========

input = '273025-767253'

# test cases
testcase(Password(), '111111', True)
testcase(Password(), '223450', False)
testcase(Password(), '123789', False)

# 910
testcase(Password(), input, 910)

# ========
#  Task B
# ========

# test cases
testcase(Password(), '112233', True,    task_b=True)
testcase(Password(), '123444', False,   task_b=True)
testcase(Password(), '111122', True,    task_b=True)

# 598
testcase(Password(), input, 598, task_b=True)
