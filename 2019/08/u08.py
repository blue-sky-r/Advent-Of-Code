#!/usr/bin/env python

__motd__ = '--- Day 8: Space Image Format ---'

__url__ = 'http://adventofcode.com/2019/day/8'

import math

verbose = 0


class SpaImaFor:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = []

    def show(self):
        """ print image """
        for idx,layer in enumerate(self.image):
            print 'layer:',idx+1
            print '\t','\n\t'.join(layer)

    def decode_str(self, str):
        """ decode string data to image """
        size = self.width * self.height
        for p in range(0, len(str)-1, size):
            layerstr = str[p:p+size]
            layer = []
            for row in range(self.height):
                p2 = row * self.width
                rowstr = layerstr[p2:p2+self.width]
                layer.append(rowstr)
            self.image.append(layer)

    def layer_count(self, layer, char):
        """ count character char in layer 1..n"""
        return ''.join(self.image[layer-1]).count(char)

    def min_zero_layer(self):
        """ find layer with minimum zeros """
        count0 = {}
        for idx in range(len(self.image)):
            zeros = self.layer_count(idx+1, '0')
            count0[idx+1] = zeros
        if verbose: print'layer -> zero_count:', count0
        min0 = min(count0.values())
        min0layer = [ k for k,v in count0.items() if v == min0 ]
        return min0layer[0]

    def task_a(self, input):
        """ task A """
        self.decode_str(input)
        if verbose: self.show()
        min0layer = self.min_zero_layer()
        c1c2 = self.layer_count(min0layer, '1') * self.layer_count(min0layer, '2')
        return c1c2

    def task_b(self, input):
        """ task B """
        return


def testcase(sut, input, result, task_b=False):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = f.readline()
    #
    print "TestCase", "B" if task_b else "A",
    print "for input:", data if 'data' in vars() else input,
    print "\t expected result:", result,
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    print 'got:',r,'\t','[ OK ]' if r == result else '[ ERR ]'
    print

# ========
#  Task A
# ========

# test cases
testcase(SpaImaFor(3,2), '123456789012',  1)

# 2500
testcase(SpaImaFor(25, 6), None, 2500)

# ========
#  Task B
# ========


