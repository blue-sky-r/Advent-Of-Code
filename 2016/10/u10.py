#!/usr/bin/env python

__motd__ = '--- Day 10: Balance Bots ---'

__url__ = 'http://adventofcode.com/2016/day/10'

verbose = 0

import re

class Robots:

    def __init__(self, pair):
        self.bins = {}
        self.pair = pair
        self.match = []

    def move_value_to_bin(self, val, bin):
        " move uchip to bin "
        if not self.bins.get(bin):
            self.bins[bin] = [ val ]
        else:
            #if val not in self.bins[bin]:
            self.bins[bin].append(val)
        return True

    def bot_gives_low_high(self, (bot, low, high)):
        " return false if bin is empty or has less than 2 uchips "
        if not self.bins.get(bot) or len(self.bins[bot]) < 2: return False
        #
        if min(self.bins[bot]) == min(self.pair) and max(self.bins[bot]) == max(self.pair):
            self.match.append(bot)
        #
        l,h = min(self.bins[bot]), max(self.bins[bot])
        self.bins[bot].remove(l)
        self.move_value_to_bin(l, low)
        self.bins[bot].remove(h)
        self.move_value_to_bin(h, high)
        return True

    def program(self, fname):
        " execute prpogram, from file $fname "
        move = []
        # read program, execute init. instructions and collect move instructions
        with open(fname) as f:
            for line in f:
                if not line: continue
                #
                if self.ins_goesto(line): continue
                move.append(line)
        #
        if verbose: print "Initial state:",self.bins
        # execute moves in loop until done
        while move:
            move = [ ins for ins in move if not self.ins_gives(ins) ]
        #
        if verbose: print "Finaal state:",self.bins

    def ins_goesto(self, ins):
        " instruction: value 5 goes to bot 2 "
        m = re.search(r'value (\d+) goes to (bot \d+)', ins)
        if not m: return False
        val = int(m.group(1))
        bot = m.group(2)
        return self.move_value_to_bin(val, bot)

    def ins_gives(self, ins):
        " instruction: bot 2 gives low to bot 1 and high to bot 0 "
        m = re.search(r'(bot \d+) gives low to (\w+ \d+) and high to (\w+ \d+)', ins)
        if not m: return False
        return self.bot_gives_low_high(m.group(1,2,3))


def testcase(input, search, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input:",input,"\t expected result:",result,
    bots = Robots(search)
    bots.program(input)
    r = bots.match[0]
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

tcdata = __file__.replace('.py', '.tc.input')
data   = __file__.replace('.py', '.input')

# test cases
testcase(tcdata, (2,5), 'bot 2')

#
bots = Robots((17,61))
bots.program(data)
r = bots.match[0]
# 27
print 'Task A input file:',data,'Result:',r
print

# ========
#  Task B
# ========

r = reduce(lambda a,b: a*b, [ int(bots.bins[idx][0]) for idx in ['output 0','output 1','output 2'] ])
# 13727
print 'Task B input file:',data,'Result:',r
