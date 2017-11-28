#!/usr/bin/env python

__motd__ = '--- Day 4: The Ideal Stocking Stuffer ---'

__url__ = 'http://adventofcode.com/2015/day/4'


verbose = 0


import hashlib

class AdventCoins:

  def hexhash(self, secret, v):
    return hashlib.md5("%s%s" % (secret,v)).hexdigest()

  def is_coin(self, secret, v, valid):
    md5 = self.hexhash(secret, v)
    return md5.startswith(valid)
  
  def dig_coin(self, secret, v=0, valid='00000'):
    while v<1234567890:
      if self.is_coin(secret, v, valid):
        print "Found:",v,"\t hash:",self.hexhash(secret,v),
        return v
      v += 1
    

def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    c = AdventCoins()
    r = c.dig_coin(input, valid='000000' if task_b else '00000')
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print


# ========
#  Task A
# ========

# test cases
testcase('abcdef',   609043)
testcase('pqrstuv', 1048970)

my_input = 'bgvyzdsv'

# 254575
testcase(my_input, 254575)

# ========
#  Task B
# ========

# 1038736
testcase(my_input, 1038736, task_b=True)
