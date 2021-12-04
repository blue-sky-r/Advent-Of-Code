#!/usr/bin/env python3

__day__  = 2

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Submarine:

    def __init__(self):
        self.xy = { 'x': 0, 'y':0}
        # valid commands
        self.cmd = {
            'up':       self.go_up,
            'down':     self.go_down,
            'forward':  self.go_forward,
        }

    def go_up(self, val):
        self.xy['y'] -= val

    def go_down(self, val):
        self.xy['y'] += val

    def go_forward(self, val):
        self.xy['x'] += val

    def sub_cmd(self, cmd):
        """ parser for string 'command val' - returns false for unknown command """
        # string go_function and value
        go, val = cmd.split()
        # transform to fnc and numeric val
        go_fnc, val = self.cmd.get(go), int(val)
        # invalid command ?
        if not go_fnc: return False
        # valid command, just execute
        go_fnc(val)
        # ok
        return True

    def x_mult_y(self):
        """ result x * y """
        return self.xy['x'] * self.xy['y']

    def task_a(self, input):
        """ task A """
        for idx,cmd in enumerate(input):
            if not self.sub_cmd(cmd):
                print('ERROR: invalid command @ line ', idx+1, ' - ', cmd)
        return self.x_mult_y()


class Submarine_aim:

    def __init__(self):
        self.xy = { 'x':0, 'depth':0, 'aim': 0 }
        # valid commands
        self.cmd = {
            'up':       self.aim_up,
            'down':     self.aim_down,
            'forward':  self.aim_go_forward,
        }

    def aim_up(self, val):
        self.xy['aim'] -= val

    def aim_down(self, val):
        self.xy['aim'] += val

    def aim_go_forward(self, val):
        self.xy['x'] += val
        self.xy['depth'] += self.xy['aim'] * val

    def sub_cmd(self, cmd):
        """ parser for string 'command val' - returns false for unknown command """
        # string go_function and value
        go, val = cmd.split()
        # transform to fnc and numeric val
        go_fnc, val = self.cmd.get(go), int(val)
        # invalid command ?
        if not go_fnc: return False
        # valid command, just execute
        go_fnc(val)
        # ok
        return True

    def x_mult_y(self):
        """ result x * y """
        return self.xy['x'] * self.xy['depth']

    def task_b(self, input):
        """ task A """
        for idx,cmd in enumerate(input):
            if not self.sub_cmd(cmd):
                print('ERROR: invalid command @ line ', idx+1, ' - ', cmd)
        return self.x_mult_y()


def testcase_a(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
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
            input = [ line.strip() for line in f ]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
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

# ========
#  Task A
# ========

# test cases
testcase_a(Submarine(), ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'],  150)

# 1804520
testcase_a(Submarine(),   None,     1804520)

# ========
#  Task B
# ========

# test cases
testcase_b(Submarine_aim(), ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'],  900)

# 1971095320
testcase_b(Submarine_aim(),   None,    1971095320)
