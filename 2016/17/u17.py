#!/usr/bin/env python

__motd__ = '--- Day 17: Two Steps Forward ---'

__url__ = 'http://adventofcode.com/2016/day/17'

verbose = 0

import hashlib

class Rooms:

    def __init__(self, passcode, dim = (4,4)):
        " set passcode and dimensions "
        self.passcode = passcode
        self.dim = dim
        # code for open doors
        self.opencode = 'bcdef'
        # the first hash chars mapped to doors directions
        self.door_hash_map = 'UDLR'
        self.reset()

    def reset(self, pos=(1,1), vault=(4,4), limit=1000):
        " set starting values "
        self.pos = pos
        self.vault = vault
        self.limit = limit
        self.solution = { 'min': None, 'max': None }

    def find_min_max_moves(self, limit=1000):
        " find min, max moves to solve up to the limit "
        self.reset(limit=limit)
        self.solve()
        return self.solution

    def solve(self, position=None, track=''):
        " solve recursing all moves from position  "
        if position is None: position = self.pos
        if self.solved(position):
            self.update_solution(track)
            return track
        if self.over_limit(track):
            return False
        if verbose: print "pos:",position,"moves:",self.possible_moves(position, track),"\t track:",track
        for move in self.possible_moves(position, track):
            self.solve(self.new_position(position, move), track+move)
        return False

    def solved(self, position):
        " we have reached the vault "
        return position == self.vault

    def update_solution(self, track):
        l = len(track)
        if self.solution['min'] is None or l > len(self.solution['max']):
            self.solution['max'] = track
        if self.solution['min'] is None or l < len(self.solution['min']):
            self.solution['min'] = track

    def over_limit(self, track):
        " we are over limit of moves "
        return len(track) >= self.limit

    def possible_moves(self, position, track):
        " get valid possible moves at this position "
        hash = self.md5(track)
        return [ door for door in self.open_doors(hash) if self.is_valid_direction(position, door) ]

    def is_valid_direction(self, position, door):
        " valid move direction has to stay inside building "
        x,y = position
        maxx,maxy = self.dim
        if door == 'U': return y > 1
        if door == 'D': return y < maxy
        if door == 'L': return x > 1
        if door == 'R': return x < maxx

    def new_position(self, position, move):
        " move to new position "
        x,y = position
        if move == 'U': return x,y-1
        if move == 'D': return x,y+1
        if move == 'L': return x-1,y
        if move == 'R': return x+1,y
        return x,y

    def open_doors(self, hash):
        " list of open doors "
        return [ door for idx,door in enumerate(self.door_hash_map) if self.is_open_code(hash[idx]) ]

    def is_open_code(self, code):
        " true if code means open door "
        return code in self.opencode

    def md5(self, track):
        " calc md5 from salt "
        return hashlib.md5(self.salt(track)).hexdigest()

    def salt(self, track):
        " combine static and dynamic part of salt "
        return self.passcode + track


def testcase(input, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input:",input,"\t expected result:",result,
    rm = Rooms(input)
    r = len(rm.find_min_max_moves()['max']) if b else rm.find_min_max_moves()['min']
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

# test cases
testcase('ihgpwlah', 'DDRRRD')
testcase('kglvqrro', 'DDUDRLRRUDRD')
testcase('ulqzkmiv', 'DRURDRUDDLLDLUURRDULRLDUUDDDRR')

#
data = 'gdjjyniy'
rm = Rooms(data)
r = rm.find_min_max_moves()
# DUDDRLRRRD
print 'Task A input file:',data,'Result:',r['min']
print

# ========
#  Task B
# ========

# test cases
testcase('ihgpwlah', 370, b=True)
testcase('kglvqrro', 492, b=True)
testcase('ulqzkmiv', 830, b=True)

# 578
print 'Task B input file:',data,'Result:',len(r['max'])
print
