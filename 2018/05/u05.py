#!/usr/bin/env python

__motd__ = '--- Day 5: Alchemical Reduction ---'

__url__ = 'http://adventofcode.com/2018/day/5'


verbose = 0


class Polymer:

    def __init__(self):
        pass

    def input_line(self, str):
        """ aAbBcAa """
        return [ c for c in str ]

    def react(self, a, b):
        """ (x X) (X x) """
        return (a.islower() and a.upper() == b) or (a.isupper() and a.lower() == b)

    def reduce_1pass(self, formula):
        """ do a single reduce pass through formula """
        if verbose > 2: print "reduce(",''.join(formula), ") -> (",
        nf, cnt, i = [], 0, 0
        while i < len(formula):
            a,b = formula[i], formula[i+1] if i < len(formula)-1 else ''
            if self.react(a, b):
                if verbose > 3: print ">",a,b,"<",
                i += 2
                cnt += 1
                continue
            nf.append(a)
            i += 1
        if verbose > 2: print ''.join(nf),") react:",cnt
        return cnt, nf

    def reduce(self, formula):
        """ iterate reduce process until no more reactions """
        while len(formula) > 2:
            cnt, formula = self.reduce_1pass(formula)
            if cnt == 0: break
        return formula

    def task_a(self, input):
        """ task A """
        for line in input:
            formula = self.input_line(line)
        formula = self.reduce(formula)
        return len(formula)

    def improve(self, formula):
        # removed part -> reduced count
        result = {}
        for c in formula:
            key = "%c/%c" % (c.upper(), c.lower())
            # skip if removal of part c has been done
            if key in result: continue
            # remove all key units
            modformula = [ x for x in formula if x not in key ]
            # removed part -> reduced count
            result[key] = len(self.reduce(modformula))
            # debug
            if verbose > 2: print "impprove() key",key," result:",result[key]
        # find key for minimal length
        if verbose: print "impprove() result:", result
        minlenkey = min(result, key=result.get)
        return result[minlenkey]

    def task_b(self, input):
        """ task B """
        for line in input:
            formula = self.input_line(line)
        return self.improve(formula)


def testcase(sut, input, result, task_b=False):
    " testcase verifies if input returns result "
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [line.rstrip() for line in f]
    #
    print "TestCase","B" if task_b else "A","for input:",data if 'data' in vars() else input,"\t expected result:",result,
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

# ========
#  Task B
# ========

# test cases
testcase(Polymer(), ['dabAcCaCBAcCcaDA'], 4, task_b=True)  # C/c

# [1m 48s] 4840
testcase(Polymer(), None, 4840, task_b=True)
