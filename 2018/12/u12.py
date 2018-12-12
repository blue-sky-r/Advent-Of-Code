#!/usr/bin/env python

__motd__ = '--- Day  ---'

__url__ = 'http://adventofcode.com/2018/day/'


verbose = 1


class Plants:

    def __init__(self, bumper=(-5,15)):
        """ """
        # pre- and post- bumper for visualization
        self.bumper = bumper
        self.rules = {}

    def start(self, pots):
        """ initial condition """
        # potnum -> plant
        self.pots = dict([(i, p) for i, p in enumerate(pots)])
        self.range = [i for i in range(self.bumper[0], len(self.pots) + self.bumper[1])]

    def show(self, pots, gen=0, header=False):
        """ visualize """
        if header:
            print '\t', ''.join(['%d' % (i // 10) for i in self.range])
            print '\t', ''.join(['%d' % (i % 10)  for i in self.range])
        #
        print "%3d\t" % gen,''.join([ pots.get(i,'.') for i in self.range])

    def add_rule(self, rule, result):
        """ store rule """
        self.rules[rule] = result

    def apply_rules(self, pots):
        """ apply single rule to pots """
        nextgen = {}
        for potnum in self.range:
            pot = pots.get(potnum, '.')
            key = ''.join([
                pots.get(potnum-2, '.'),
                pots.get(potnum-1, '.'),
                pot,
                pots.get(potnum+1, '.'),
                pots.get(potnum+2, '.')
            ])
            val = self.rules.get(key, '.')
            if verbose > 1: print "apply_rules() potnum:",potnum,"key:",key,'val:',val
            nextgen[potnum] = val
        return nextgen

    def calc_sum(self, pots):
        """ pots[num] -> plant """
        return sum([ n for n,p in pots.items() if p=='#' ])

    def input_line(self, str):
        """ .##.. => # """
        if str.startswith('initial state:'):
            _, _, init = str.split()
            self.start(init)
            return
        #
        key,_,val = str.partition(' => ')
        self.add_rule(key, val)
        return

    def task_a(self, input):
        """ task A """
        for line in input:
            self.input_line(line)
        #
        if verbose: self.show(self.pots, gen=0, header=True)
        for g in range(20):
            self.pots = self.apply_rules(self.pots)
            if verbose: self.show(self.pots, gen=g+1)
        #
        r = self.calc_sum(self.pots)
        return r

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

data="""
initial state: #..#.#..##......###...###
...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
"""
# test cases
testcase(Plants(), data.strip().split('\n'), 325)

# 3798
testcase(Plants(bumper=(-5,30)), None, 3798)
xxx
# ========
#  Task B
# ========

# test cases
testcase(Plants(), ['', '', '', ''],            2, task_b=True)

# [1m 34s] 56360
testcase((), None, 2, task_b=True)
