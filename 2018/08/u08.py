#!/usr/bin/env python

__motd__ = '--- Day 8: Memory Maneuver ---'

__url__ = 'http://adventofcode.com/2018/day/8'


verbose = 0


class License:

    def __init__(self):
        pass

    def show(self, tree):
        """ visualize tree structure """
        pass

    def build_tree(self, lst):
        """ [2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2]
             2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
             A----------------------------------
                 B----------- C-----------
                                  D-----
        """
        # node = { header: [], child: [node, node], meta: [metadata]}
        header, data = lst[:2], lst[2:]
        numchld, nummeta = int(header[0]), int(header[1])
        if verbose: print "build_tree(",' '.join(lst),") child#:",numchld,"meta#:",nummeta
        # children
        children = []
        for i in range(numchld):
            subtree, data = self.build_tree(data)
            children.append(subtree)
        metadata, data = data[:nummeta], data[nummeta:]
        # construct node
        node = {
            'header': header,
            'child': children,
            'meta': metadata
        }
        return node, data

    def get_metadata(self, tree):
        """ get all metadata as a flat list """
        return tree['meta'] + [ x for child in tree['child'] for x in self.get_metadata(child) ]

    def get_rootval(self, tree):
        """ get the root node value (children depndent) """
        # no children = return sum of meta
        if tree['child'] == []:
            return sum([ int(x) for x in tree['meta'] ])
        # with children = meta is the 1-index
        r = []
        for m in tree['meta']:
            idx = int(m) - 1
            if 0 <= idx < len(tree['child']):
                child = tree['child'][idx]
                r.append( self.get_rootval(child) )
        return sum(r)

    def input_line(self, str):
        """ 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2 """
        tree, data = self.build_tree(str.split())
        if data != []: return tree, "ERR: not all data have been processed data: %s" % data
        return tree, ''

    def task_a(self, input):
        """ task A """
        for line in input:
            tree, err = self.input_line(line)
            if err: print err
        #
        r = sum([ int(i) for i in self.get_metadata(tree) ])
        return r

    def task_b(self, input):
        """ task B """
        for line in input:
            tree, err = self.input_line(line)
            if err: print err
        #
        r = self.get_rootval(tree)
        return r


def testcase(sut, input, result, task_b=False):
    " testcase verifies if input returns result "
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [line.rstrip() for line in f]
    #
    print "TestCase", "B" if task_b else "A", "for input:", data if 'data' in vars() else input, "\t expected result:", result,
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    #r = f.find_duplo(input) if task_b else f.change_seq(input)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    print

# ========
#  Task A
# ========

# test cases
testcase(License(), ['2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'],          138)
# 45210
testcase(License(), None, 45210)

# ========
#  Task B
# ========

# test cases
testcase(License(), ['2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'],           66, task_b=True)

# 22793
testcase(License(), None, 22793, task_b=True)
