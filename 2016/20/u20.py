#!/usr/bin/env python

__motd__ = '--- Day 20: Firewall Rules ---'

__url__ = 'http://adventofcode.com/2016/day/20'

verbose = 0

class Firewall:

    def __init__(self, max_ip=4294967295):
        " empty block range list, maxip "
        self.block = []
        self.max_ip = max_ip

    def parse_file(self, fname):
        " parse text file "
        with open(fname) as f:
            for line in f:
                self.add_line(line.strip())

    def add_line(self, line, sep='-'):
        " add text range from-to "
        if sep in line:
            low,high = line.split(sep)
            self.add_range( ( int(low),int(high) ) )

    def add_range(self, (low,high)):
        " add blocking range as tuple (from,to) inclusive "
        self.block.append( (low,high) )

    def find_min_pass_ip(self):
        " min passing ip "
        ip = 0
        while ip <= self.max_ip:
            blocked,ip = self.ip_blocked(ip)
            if not blocked:
                return ip
            if verbose: print "ip",ip,"blocked"
            ip += 1

    def count_pass_ip(self):
        " count passing ips "
        ip,cnt = 0,0
        while ip <= self.max_ip:
            blocked,ip = self.ip_blocked(ip)
            if not blocked:
                cnt += 1
            if verbose: print "ip",ip,"blocked"
            ip += 1
        return cnt

    def ip_blocked(self, ip):
        " return tuple boolean,newip "
        for low,high in self.block:
            if low <= ip <= high:
                return True,high
        return False,ip


def testcase(input, result, b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if b else 'A',
    print "for input:",input,"\t expected result:",result,
    fw = Firewall(max_ip=9)
    for line in input:
        fw.add_line(line)
    r = fw.count_pass_ip() if b else fw.find_min_pass_ip()
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    if verbose: print "Trace:",
    print

# ========
#  Task A
# ========

# test cases
testcase(['5-8','0-2','4-7'], 3)

data = __file__.replace('.py', '.input')
fw = Firewall()
fw.parse_file(data)
r = fw.find_min_pass_ip()
# 22887907
print 'Task A input file:',data,'Result:',r
print

# ========
#  Task B
# ========

# test cases
testcase(['5-8','0-2','4-7'], 2, b=True)

r = fw.count_pass_ip()
# 109
print 'Task B input file:',data,'Result:',r
print
