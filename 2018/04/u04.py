#!/usr/bin/env python

__motd__ = '--- Day 4: Repose Record ---'

__url__ = 'http://adventofcode.com/2018/day/4'

import re


verbose = 0


class Log:

    def __init__(self):
        self.table = {}
        self.sym = {
            'awake': '.',
            'sleep': '#'
        }
        self.tmp = {}

    def show(self, table=None, cellfrm='%1s'):
        """ print table """
        if table is None: table = self.table
        row = "%-12s %s"
        # header
        print
        print row % ('date id', 'minute')
        print row % (' ', ''.join([cellfrm % (m / 10) for m in range(60)]))
        print row % (' ', ''.join([cellfrm % (m % 10) for m in range(60)]))
        #
        for dateid in sorted(table.keys()):
            print row % (dateid, ''.join( [cellfrm % table[dateid][m] for m in range(60) ] ))
        #

    def record_key(self, guard, date):
        """ get key to table """
        return ' '.join([date, guard])

    def record_guard(self, guard, date):
        """ create a new record for guard assuming no sleep """
        key = self.record_key(guard, date)
        self.table[key] = dict([ (i,self.sym['awake']) for i in range(60)])

    def record_sleep(self, guard, date, minsleep, minwakeup):
        """ record sleep period for guard #id """
        key = self.record_key(guard, date)
        for m in range(int(minsleep), int(minwakeup)):
            self.table[key][m] = self.sym['sleep']

    def input_line(self, str):
        """ [1518-11-04 00:02] Guard #99 begins shift """
        pattern = {
            # [1518-11-04 00:02] Guard #99 begins shift
            'guard':  re.compile(r'\[\d{4}-(\d{2}-\d{2}) \d{2}:(\d{2})\] Guard (#\d+) begins shift'),
            # [1518-11-04 00:36] falls asleep
            'sleep':  re.compile(r'\[\d{4}-(\d{2}-\d{2}) \d{2}:(\d{2})\] falls asleep'),
            # [1518-11-05 00:55] wakes up
            'wakeup': re.compile(r'\[\d{4}-(\d{2}-\d{2}) \d{2}:(\d{2})\] wakes up')
        }
        for event,pat in pattern.items():
            m = pat.match(str)
            if m:
                date,time = m.group(1),m.group(2)
                if event == 'guard':
                    self.tmp['gid']  = m.group(3)
                    self.tmp['date'] = date
                    self.record_guard(self.tmp['gid'], self.tmp['date'])
                if event == 'sleep':
                    self.tmp['start'] = time
                if event == 'wakeup':
                    self.record_sleep(self.tmp['gid'], self.tmp['date'], self.tmp['start'], time)
                break
        else:
            return 'invalid input line'
        return None

    def input_lst(self, input):
        for line in sorted(input):
            err = self.input_line(line)
            if err: print "ERR:",err
        if verbose: self.show()
        return

    def agg_by_guard(self):
        """ aggregate table by guard: guard -> minute = sleep """
        # create guard[#id] -> { minute: sum(sleep) }
        guard = {}
        # symbols to integer translation
        sym2int = {
            self.sym['awake']: 0,
            self.sym['sleep']: 1
        }
        #
        for dateid, record in self.table.items():
            date, id = dateid.split(' ')
            guard[id] = dict([(m, guard.get(id, {}).get(m, 0) + sym2int[record[m]]) for m in range(60)])
        #
        if verbose: self.show(table=guard, cellfrm='%2x')
        return guard

    def find_max_sleeper(self):
        # row summary per guard
        guard = self.agg_by_guard()
        # guard -> sleep oer shift aggregated
        gsagg = dict( [ (gid, sum(agg.values())) for gid,agg in guard.items() ] )
        # find guard id for max sleep
        gidmax = max(gsagg, key=gsagg.get)
        # find minute for max probbability sleep mps
        mps = max(guard[gidmax], key=guard[gidmax].get)
        # remove leading #
        return int(gidmax[1:]), mps

    def find_max_probability_minute(self):
        # row summary per guard
        guard = self.agg_by_guard()
        #
        #dict( [ (gid, max(agg.values())) for gid,agg in guard.items() ] )
        # max probability guard -> minute of max probability
        found = {}
        for guard, record in guard.items():
            minute = max(record, key=record.get)
            if found.get('probab', 0) > record[minute]: continue
            found = {
                'gid': guard,
                'minute': minute,
                'probab': record[minute]
            }
        # remove leading #
        return int(found['gid'][1:]), found['minute']

    def task_a(self, input):
        """ task A """
        self.input_lst(input)
        id, m = self.find_max_sleeper()
        return id * m

    def task_b(self, input):
        """ task B """
        self.input_lst(input)
        id, m = self.find_max_probability_minute()
        return id * m


def testcase(sut, input, result, task_b=False):
    " testcase verifies if input returns result "
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [line.rstrip() for line in f]
    #
    print "TestCase for input:",data if 'data' in vars() else input,"\t expected result:",result,
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    #r = f.find_duplo(input) if task_b else f.change_seq(input)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    print

# ========
#  Task A
# ========

# test cases
data = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
"""
testcase(Log(), data.strip().split('\n'), 240)
# 39584
testcase(Log(), None, 39584)

# ========
#  Task B
# ========

testcase(Log(), data.strip().split('\n'), 4455, task_b=True)
# 55053
testcase(Log(), None, 55053, task_b=True)

