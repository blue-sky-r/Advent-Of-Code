#!/usr/bin/env python

__motd__ = '--- Day 3: Squares With Three Sides ---'

__url__ = 'http://adventofcode.com/2016/day/3'

verbose = 0

def is_triangle(a, b, c):
        err = []
        if not (a+b) > c: err.append('a+b > c')
        if not (a+c) > b: err.append('a+c > b')
        if not (b+c) > a: err.append('b+c > a')
        return err if err else True


# ========
#  Task A
# ========

data = __file__.replace('.py', '.input')

with open(data) as f:
    ok,err = 0,0
    for line in f:
        if not line: continue
        a,b,c = line.split()
        if verbose: print "a(%s) b(%s) c(%s)" % (a,b,c),"\t",
        res = is_triangle(int(a), int(b), int(c))
        if res == True:
            ok  += 1
            if verbose: print 'OK'
        else:
            err += 1
            if verbose: print 'ERR:',res

# 982
print 'Task A input file:',data,'Result:',ok
print

# ========
#  Task B
# ========

with open(data) as f:
    ok,err = 0,0
    group = []
    for line in f:
        if not line: continue
        group.append(line)
        # read 3 lines
        if len(group) == 3:
            a3 = group[0].split()
            b3 = group[1].split()
            c3 = group[2].split()
            # check each column
            for i in range(3):
                a = int(a3[i])
                b = int(b3[i])
                c = int(c3[i])
                if verbose: print "a(%s) b(%s) c(%s)" % (a,b,c),"\t",
                res = is_triangle(a, b, c)
                if res == True:
                    ok  += 1
                    if verbose: print 'OK'
                else:
                    err += 1
                    if verbose: print 'ERR:',res
            group = []
    # sanity check
    if group:
        print "WARN: unprocessed input lines:",group

# 1826
print 'Task B input file:',data,'Result:',ok
print
