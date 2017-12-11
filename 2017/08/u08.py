#!/usr/bin/env python

__motd__ = '--- Day 8: I Heard You Like Registers ---'

__url__ = 'http://adventofcode.com/2017/day/8'


verbose = 0


class CPU:

    def __init__(self):
        self.reg = {}
        self.peak = 0
        
    def max_peak(self):
        self.peak = max([self.peak] + [val for reg,val in self.reg.items()])
        
    def get_reg(self, id):
        return self.reg.get(id, 0)
        
    def set_reg(self, id, val):
        self.reg[id] = val

    def run_program(self, lst):
        for line in lst:
            self.instruction(line)
        return self.reg_max_peak()
                
    def instruction(self, str):
        # c inc -20 if c == 10
        ins,_,cond = str.partition(' if ')
        if self.condition(cond): 
            if verbose: print "EXEC \t",str,
            self.incdec(ins)
        else:
            if verbose: print "SKIP \t",str,
        if verbose: print "\t REGS:",self.reg
        self.max_peak()
        
    def incdec(self, str):
        a,ins,b = str.partition(' inc ')
        if ins: return self.inc_reg(a, b)
        a,ins,b = str.partition(' dec ')
        if ins: return self.dec_reg(a, b)
        
    def inc_reg(self, id, val):
        self.set_reg(id, self.get_reg(id) + int(val))

    def dec_reg(self, id, val):
        self.set_reg(id, self.get_reg(id) - int(val))
    
    def condition(self, str):
        # a > 1
        l,cmp,r = str.split()
        if cmp == '==': return self.get_reg(l) == int(r)
        if cmp == '>=': return self.get_reg(l) >= int(r)
        if cmp == '<=': return self.get_reg(l) <= int(r)
        if cmp == '!=': return self.get_reg(l) != int(r)
        if cmp == '>': return self.get_reg(l) > int(r)
        if cmp == '<': return self.get_reg(l) < int(r)
        
    def reg_max_peak(self):
        return max([ val for reg,val in self.reg.items()]),self.peak


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    c = CPU()
    stat = c.run_program(input)
    r = stat[1] if task_b else stat[0]
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

str = [
"b inc 5 if a > 1",
"a inc 1 if b < 5",
"c dec -10 if a >= 1",
"c inc -20 if c == 10"
]

testcase(str, 1)

data = __file__.replace('.py', '.input')
c = CPU()
with open(data) as f:
    stat = c.run_program(f.read().splitlines())
# 6611
print 'Task A input file:',data,'Result:',stat[0]

# ========
#  Task A
# ========

testcase(str, 10, task_b=True)

# 6619
print 'Task B input file:',data,'Result:',stat[1]
