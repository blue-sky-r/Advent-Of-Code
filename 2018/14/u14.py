#!/usr/bin/env python

__motd__ = '--- Day  ---'

__url__ = 'http://adventofcode.com/2018/day/'


verbose = 0


class Choco:

    def __init__(self):
        """ start conditions """
        self.recipe = [3, 7]
        self.elfs = {
            'a': 0,
            'b': 1
        }

    def show(self):
        """ visualize recipes """
        s = []
        for idx,r in enumerate(self.recipe):
            if idx == self.elfs['a']:
                s.append("(%d)" % r)
                continue
            if idx == self.elfs['b']:
                s.append("[%d]" % r)
                continue
            s.append(" %d " % r)
        print ' '.join(s)

    def add_new_recipe(self):
        """ add new recipe """
        new = sum([ self.recipe[idx] for elf,idx in self.elfs.items() ])
        if new < 10:
            self.recipe.append(new)
        else:
            a,b = new // 10, new % 10
            self.recipe.append(a)
            self.recipe.append(b)

    def pick_new_recipe(self):
        """ pick new recipe """
        #ones = self.recipe.count(1)
        length = len(self.recipe)
        self.elfs = dict([ (e, sum([idx, 1, self.recipe[idx]]) % length) for e,idx in self.elfs.items() ])

    def task_a(self, input):
        """ task A """
        after = input
        rlen = 10
        while True:
            if verbose: self.show()
            self.add_new_recipe()
            self.pick_new_recipe()
            if len(self.recipe) > after + rlen:
                break
        # show result
        if verbose:
            print "result:"
            self.show()
        #
        return ''.join([ "%d" % r for r in self.recipe[input:input+rlen] ])

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
    print "TestCase", "B" if task_b else "A", "for input:", data if 'data' in vars() else input, "\t expected result:", result,
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    #r = f.find_duplo(input) if task_b else f.change_seq(input)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    print

# ========
#  Task A
# ========

# test cases
testcase(Choco(),    5, '0124515891')
testcase(Choco(),    9, '5158916779')
testcase(Choco(),   18, '9251071085')
testcase(Choco(), 2018, '5941429882')

# 4910101614
testcase(Choco(), 793031, '4910101614')
xxx
#
testcase((), None, 1)

# ========
#  Task B
# ========

# test cases
testcase((), ['', '', '', ''],            2, task_b=True)

# [1m 34s] 56360
testcase((), None, 2, task_b=True)
