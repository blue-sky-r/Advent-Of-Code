#!/usr/bin/env python

__motd__ = '--- Day 4: Security Through Obscurity ---'

__url__ = 'http://adventofcode.com/2016/day/4'

verbose = 0

class Room:

    def __init__(self, txt):
        self.txt = txt

    def checksum(self):
        leftb  = self.txt.find('[')
        rightb = self.txt.find(']', leftb)
        return self.txt[leftb+1:rightb]

    def id(self):
        leftb  = self.txt.find('[')
        rdash  = self.txt.rfind('-')
        return int(self.txt[rdash+1:leftb])

    def name(self):
        rdash = self.txt.rfind('-')
        return self.txt[:rdash]

    def chr_cnt(self):
        " returns dictionary char => count "
        name = self.name()
        count = {}
        for c in name:
            if c in count: continue
            if c == '-':   continue
            count[c] = name.count(c)
        return count

    def calc_checksum(self):
        count = self.chr_cnt()
        chksum = []
        # sort by count, reversed ascii code as tuple
        for chr,cnt in sorted(count.items(), key=lambda x: (x[1],ord('z')-ord(x[0])), reverse=True):
            chksum.append(chr)
        return ''.join(chksum)[:5]

    def is_real(self):
        return self.checksum() == self.calc_checksum()

    def chr_rot(self, c, num):
        # hyphens -> space
        if c == '-': return ' '
        # calc ascii code
        ascii = ord('a') + ((ord(c) - ord('a') + num) % 26)
        # return new char
        return chr(ascii)

    def decrypted_name(self):
        rot = self.id()
        decrypted = []
        for c in self.name():
            decrypted.append(self.chr_rot(c, rot))
        return ''.join(decrypted)


def testcaseA(input, result):
    " testcase verifies if input returns result "
    print "TestCase A",
    print "for input:",input,"\t expected result:",result,
    room = Room(input)
    r = room.is_real()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    if verbose:
        print "id:",room.id(),"name:",room.name(),"chksum:",room.checksum(),"calc:",room.calc_checksum(),"chr_cnt",room.chr_cnt()
    print
    return room.id() if r else 0

def testcaseB(input, result):
    " testcase verifies if input returns result "
    print "TestCase B",
    print "for input:",input,"\t expected result:",result,
    room = Room(input)
    r = room.decrypted_name()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    if verbose:
        print "id:",room.id(),"name:",room.name(),"chksum:",room.checksum(),"calc:",room.calc_checksum(),"chr_cnt",room.chr_cnt()
    print

# ========
#  Task A
# ========

# test cases
expected_sum = 1514
sum = 0
sum += testcaseA('aaaaa-bbb-z-y-x-123[abxyz]',    True)
sum += testcaseA('a-b-c-d-e-f-g-h-987[abcde]',    True)
sum += testcaseA('not-a-real-room-404[oarel]',    True)
sum += testcaseA('totally-real-room-200[decoy]', False)
print "TestCases \t Sum:",sum,"Expected:",expected_sum,"\t","OK" if sum == expected_sum else "ERR"
print

data = __file__.replace('.py', '.input')
sum = 0
with open(data) as f:
    for line in f:
        if not line: continue
        room = Room(line)
        real = room.is_real()
        if real:
            sum += room.id()
        if verbose:
            print "input:",line.strip(),"is_real:",real
            print "id:",room.id(),"name:",room.name(),"chksum:",room.checksum(),"calc:",room.calc_checksum(),"chr_cnt",room.chr_cnt()
            print

# 361724
print 'Task A input file:',data,'Result:',sum
print

# ========
#  Task B
# ========

# test cases
testcaseB('qzmt-zixmtkozy-ivhz-343[x]', 'very encrypted name')

data   = __file__.replace('.py', '.input')
search = ' object'
found = []
with open(data) as f:
    for line in f:
        if not line: continue
        room = Room(line)
        real = room.is_real()
        name = room.decrypted_name()
        if verbose:
            print "input:",line.strip(),"is_real:",real,"decrypted_name:",name
        if real and search in name:
            print "Found string:",search,' id:',room.id(),'name:',name
            found.append(room.id())
    print

# 482
print 'Task B input file:',data,'Result:',','.join(["%d" % i for i in found])
print
