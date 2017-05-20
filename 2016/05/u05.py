#!/usr/bin/env python

__motd__ = '--- Day 5: How About a Nice Game of Chess? ---'

__url__  = 'http://adventofcode.com/2016/day/5'

# note: verbosity will break the animation
verbose = 0

import hashlib
import animation

class Door:

    def __init__(self, id):
        self.id = id
        self.anim = animation.Animation(slowdown=3E4)

    def hash_gen(self, prefix='00000'):
        idx = 0
        while True:
            str = '%s%d' % (self.id, idx)
            md5 = hashlib.md5(str).hexdigest()
            self.anim.searching(idx)
            if md5.startswith(prefix):
                yield md5
            idx += 1

    def password(self, hashidx=6, length=8):
        pswd = []
        for hash in self.hash_gen():
            pswd.append(hash[hashidx-1])
            self.anim.update(pswd)
            if verbose: print "password() hash:",hash,"pswd:",pswd
            if len(pswd) >= length: break
        return ''.join(pswd)

    def password2(self, hashpos=6, hashidx=7, length=8):
        pswd = {}
        for hash in self.hash_gen():
            position  = int(hash[hashpos-1], 16)
            if verbose: print "password() hash:",hash,"pos:",position
            # ignore position outside password
            if position >= length: continue
            # ignore multiple finds for the same position
            if position in pswd:  continue
            character = hash[hashidx-1]
            pswd[position] = character
            if verbose: print "password() hash:",hash,"pswd:",pswd
            self.anim.update(pswd)
            if len(pswd) >= length: break
        return ''.join(pswd.values())


def testcase(input, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input:",input,"\t expected result:",result,"got: ",
    pswd = Door(input)
    r = pswd.password2() if b else pswd.password()
    print r,'\t','OK' if r == result else 'ERR'
    if verbose: print "Trace:",
    print

# ========
#  Task A
# ========

# test cases
testcase('abc', '18f47a30')

data = 'ojvtpuvg'
pswd = Door(data)
print 'Task A input:',data,'Result: ',
r = pswd.password()
# 4543c154
print r
print

# ========
#  Task B
# ========

# test cases
testcase('abc', '05ace8e3', b=True)

pswd = Door(data)
print 'Task B input:',data,'Result: ',
r = pswd.password2()
# 1050cbbd
print r
print
