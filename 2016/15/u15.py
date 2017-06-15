#!/usr/bin/env python

__motd__ = '--- Day 15: Timing is Everything ---'

__url__ = 'http://adventofcode.com/2016/day/15'

verbose = 0

class Disc:

    def __init__(self, id, positions):
        self.id = id
        self.positions = positions

    def set_pos(self, pos, time=0):
        " set disc starting position "
        self.time = time
        self.pos = pos
        return self

    def pos_in_time(self, time=0):
        " cacl disc position in time $time "
        return (self.pos + time) % self.positions

    def is_slot_in_time(self, time=0):
        " check if slot for fall through is there in time $time "
        return self.pos_in_time(time) == 0


class Sculpture:

    def __init__(self):
        self.discs = []

    def add_disc(self, disc):
        " add disc to sculpture "
        self.discs.append(disc)
        return self

    def dump(self, time=0):
        " get disc positions in time $time - only for verbose output "
        return [ "%2d" % disc.pos_in_time(time+i) for i,disc in enumerate(self.discs) ]

    def fall_through(self, time=0):
        " check if ball can fall through the slots starting at time $time"
        for disc in self.discs:
            if not disc.is_slot_in_time(time):
                return False
            time += 1
        return True

    def find_time(self, limit=10):
        " find the 1st time for button to be pressed so ball can fall through "
        for time in xrange(limit):
            if verbose: print "t=%03d" % time,"\t"," ".join(self.dump(time+1))
            # disc needs 1 sec to reach disc1
            if self.fall_through(time+1):
                return time


def create_sculpture(disc_init):
    " create sculpture from simple input "
    s = Sculpture()
    for idx, posrot in enumerate(disc_init):
        positions, rot = posrot[0], posrot[1]
        s.add_disc( Disc(idx+1, positions).set_pos(rot) )
    return s

def testcase(input, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input:",input,"\t expected result:",result,
    s = create_sculpture(input)
    r = s.find_time()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

# test cases
# list of tuples (disc_positions, disc_actual_p[osition)
tcdata = [ (5,4), (2,1) ]
testcase(tcdata, 5)

# list of tuples (disc_positions, disc_actual_p[osition)
data = [ (17,5), (19,8), (7,1), (13,7), (5,1), (3,0) ]
sa = create_sculpture(data)
r = sa.find_time(limit=100000)
# 16824
print 'Task A input:',data,'Result:',r
print

# ========
#  Task B
# ========

# add another disc
data.append( (11,0) )
sb = create_sculpture(data)
r = sb.find_time(limit=100000000)
# 3543984
print 'Task B input:',data,'Result:',r
