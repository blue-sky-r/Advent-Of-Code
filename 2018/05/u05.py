#!/usr/bin/env python

__motd__ = '--- Day 5: Alchemical Reduction ---'

__url__ = 'http://adventofcode.com/2018/day/5'


verbose = 1


class Polymer:

    def __init__(self):
        pass

    def input_line(self, str):
        """ aAbBcAa """
        self.formula = str
        return

    def react(self, a, b):
        """ (x X) (X x) """
        return (a.islower() and a.upper() == b) or (a.isupper() and a.lower() == b)

    def reduce(self):
        if verbose: print "reduce(",self.formula, ") -> (",
        nf,cnt = [],0
        i = 0
        while i < len(self.formula):
            a,b = self.formula[i:i+1], self.formula[i+1:i+2]
            if self.react(a,b):
                if verbose: print ">",a,b,"<",
                i += 2
                cnt += 1
                continue
            nf.append(a)
            i += 1
        self.formula = ''.join(nf)
        if verbose: print self.formula,") react:",cnt
        return cnt

    def task_a(self, input):
        """ task A """
        for line in input:
            self.input_line(line)
        while len(self.formula) >= 2:
            if self.reduce() == 0: break
        return len(self.formula)

    def task_b(self, input):
        """ task B """
        return


def testcase(sut, input, result, task_b=False):
    " testcase verifies if input returns result "
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [line.rstrip() for line in f]
    #
    print "TestCase for input:",data if 'data' in vars() else input,"\t expected result:",result,
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    #r = f.find_duplo(input) if task_b else f.change_seq(input)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    print

# ========
#  Task A
# ========

# test cases
testcase(Polymer(), ['aA'],     0)
testcase(Polymer(), ['abBA'],   0)
testcase(Polymer(), ['abAB'],   4)
testcase(Polymer(), ['aabAAB'], 6)
testcase(Polymer(), ['dabAcCaCBAcCcaDA'], 10)   # dabCBAcaDA
# 10978
testcase(Polymer(), None, 10978)
xxx
# ========
#  Task B
# ========

# test cases
testcase((), ['', '', '', ''],            2, task_b=True)

# [1m 34s] 56360
testcase((), None, 2, task_b=True)
