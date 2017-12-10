#!/usr/bin/env python

__motd__ = '--- Day 7: Recursive Circus ---'

__url__ = 'http://adventofcode.com/2017/day/7'


verbose = 0


class Node:

    def __init__(self, name, weight, children=[], ok=True):
        self.name = name
        self.weight = int(weight)
        self.children = children
        self.ok = ok

    def is_leaf(self):
        return not self.children

    def is_ok(self):
        return self.ok

    def weight_recurs(self):
        w = self.weight
        for child in self.children:
            w += child.weight_recurs()
        return w

    def balancing(self, diff=0):
        # leaf is balanced
        if self.is_leaf(): return 0
        # recurs weight for each child
        wc = [ c.weight_recurs() for c in self.children ]
        # debug
        if verbose: print 'node:',self.name,"weight_recurs:",wc
        # all childen match = balanced
        maxwc, minwc = max(wc), min(wc)
        if maxwc == minwc: return self.weight - diff
        #
        min_cnt, max_cnt = wc.count(minwc), wc.count(maxwc)
        if min_cnt < max_cnt:
            # look for min_cnt
            idx = wc.index(minwc)
        if max_cnt < min_cnt:
            # look for max_cnt
            idx = wc.index(maxwc)
        #
        if verbose: print 'node:',self.name,'unbalanced child idx:',idx
        #
        #return self.weight - (maxwc-minwc) - self.children[idx].balancing()
        return self.children[idx].balancing(maxwc - minwc)


class Parser:

    def __init__(self):
        self.sep = ' -> '
        self.csv_sep = ', '

    def build_tree(self, lines):
        node_dict = self.node_dict(lines)
        # iterate
        while len(node_dict) > 1:
            anything_reduced = False
            for name,node in node_dict.items():
                if verbose:
                    print
                    print "processing:",name,"w:",node.weight,'ok:',node.ok,"ch:",len(node.children),node.children if not node.ok else '-'
                    print "still to go:",len(node_dict),[name for name,val in node_dict.items()]
                # connect children if all are already known
                if not node.is_leaf() and all([node_dict.get(name) and node_dict[name].ok for name in node.children]):
                    links = [ node_dict[name] for name in node.children]
                    # release from node_dict
                    for name in node.children:
                        del node_dict[name]
                    # setup links
                    node.children = links
                    # mark ok
                    node.ok = True
                    # marker
                    anything_reduced = True
            if not anything_reduced:
                print "DEADLOCL detected"
                break
        # root node
        return node_dict

    def node_dict(self, lines):
        node_dict = {}
        for line in lines:
            name = self.get_name(line)
            node_dict[name] = Node(name, self.get_weight(line), self.get_children(line), ok=self.is_leaf(line))
        return node_dict

    def is_leaf(self, line):
        # fwft (72) -> ktlj, cntj, xhth
        # ktlj (57)
        return self.sep not in line

    def get_name(self, line):
        # ktlj (57)
        name, _ = line.split(' ', 1)
        return name

    def get_weight(self, line):
        # ktlj (57)
        if not self.is_leaf(line):
            line, _, _ = line.partition(self.sep)
        _,weight = line.split(' ', 1)
        return weight.strip('()')

    def get_children(self, line):
        # fwft (72) -> ktlj, cntj, xhth
        if self.is_leaf(line): return []
        _, _, csv = line.partition(self.sep)
        return csv.split(self.csv_sep)


def testcase(input, result, task_b=False):
    " testcase verifies if input returns result "
    print "TestCase",'B' if task_b else 'A',
    print "for input:",input,"\t expected result:",result,
    p = Parser()
    tree = p.build_tree(input)
    k = tree.keys()[0]
    r = tree[k].balancing() if task_b else k
    print 'got:',r,'\t','OK' if r == result else 'ERR'
    print

# ========
#  Task A
# ========

str = [
'pbga (66)',
'xhth (57)',
'ebii (61)',
'havc (66)',
'ktlj (57)',
'fwft (72) -> ktlj, cntj, xhth',
'qoyq (66)',
'padx (45) -> pbga, havc, qoyq',
'tknk (41) -> ugml, padx, fwft',
'jptl (61)',
'ugml (68) -> gyxo, ebii, jptl',
'gyxo (61)',
'cntj (57)',
]

testcase(str,  'tknk')

data = __file__.replace('.py', '.input')
p = Parser()
with open(data) as f:
    root = p.build_tree(f.read().splitlines())
k = root.keys()[0]
# vmpywg
print 'Task A input file:',data,'Result:',k
print

# ========
#  Task B
# ========

testcase(str,  60, task_b=True)

r = root[k].balancing()
# 1674
print 'Task B input file:',data,'Result:',r
print

