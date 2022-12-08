#!/usr/bin/env python3

__day__  = 5

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class SupplyStacks:

    def __init__(self):
        pass

    def print_stacks(self, msg):
        """ visualize stacks """
        if not verbose: return
        s = []
        # index line
        s.append([ " %d " % (idx+1) for idx,stack in enumerate(self.stacks)])
        # find max depth
        depth = max([len(stack) for stack in self.stacks])
        for d in range(depth):
            items = ["[%s]" % stack[d] if len(stack) > d else ' - ' for stack in self.stacks]
            s.append(items)
        # print msg
        print('-', msg, '-')
        # print reversed
        for line in s[::-1]:
            print(' '.join(line))
        print()

    def init_empty_stacks(self, n):
        """ init N empty stacks """
        self.stacks = [ [] for i in range(n) ]

    def init_stacks(self, input):
        """ init stacks from string list """
        n = None
        # iterate backwards
        for line in input[::-1]:
            # detect number of stacks: 1   2   3
            if n is None:
                idx = [ int(i) for i in line.split() ]
                n = max(idx)
                self.init_empty_stacks(n)
                continue
            # push items to stacks: [Z] [M]     [P]
            for stack in range(n):
                if len(line) < 4*stack: break
                crate = line[4*stack:4*stack+3]
                item = crate[1]
                if item != ' ':
                    self.stacks[stack].append(item)

    def move_N_from_A_to_B(self, n, a, b, keeporder=False):
        """ move N items from top of A to top of B """
        stack_a, stack_b = self.stacks[a-1], self.stacks[b-1]
        if keeporder:
            # pop N items
            items = [ stack_a.pop() for i in range(n) ]
            # push in reverse order
            stack_b.extend(items[::-1])
        else:
            # Nx a.pop -> b.push
            for i in range(n):
                item = stack_a.pop()
                stack_b.append(item)

    def move_N_from_A_to_B_str(self, s, keeporder=False):
        """ instruction as a string move n from A to B """
        _move_, n, _from_, a, _to_, b = s.split()
        self.move_N_from_A_to_B(int(n), int(a), int(b), keeporder)

    def get_msg(self):
        """ get message from stack tops """
        msg = [ stack.pop() for stack in self.stacks ]
        return ''.join(msg)

    def init_and_move(self, input: list, keeporder=False):
        """ init stacks and move items based on instructions """
        init_state, init_done = [], False
        for line in input:
            # init ?
            if not init_done:
                # empty line marks end of init state
                if not line:
                    self.init_stacks(init_state)
                    init_done = True
                    self.print_stacks('inistial state')
                    continue
                init_state.append(line)
                continue
            # move instruction
            self.move_N_from_A_to_B_str(line, keeporder)
            self.print_stacks(line)
        #

    def task_a(self, input: list):
        """ task A """
        self.init_and_move(input)
        return self.get_msg()

    def task_b(self, input: list):
        """ task B """
        self.init_and_move(input, keeporder=True)
        return self.get_msg()


def testcase_a(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.rstrip() for line in f ]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ line.rstrip() for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()

def testcase_b(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.rstrip() for line in f ]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ line.rstrip() for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_b(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()


# ======
#  MAIN
# ======

print()
print(__motd__, __url__)
print()

testdata = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

# ========
#  Task A
# ========

# test cases
testcase_a(SupplyStacks(), testdata,  'CMZ')

# WCZTHTMPS
testcase_a(SupplyStacks(),   None, 'WCZTHTMPS')

# ========
#  Task B
# ========

# test cases
testcase_b(SupplyStacks(), testdata, 'MCD')

# BLSGJSDTS
testcase_b(SupplyStacks(),   None, 'BLSGJSDTS')
