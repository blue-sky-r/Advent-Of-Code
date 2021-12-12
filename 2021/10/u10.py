#!/usr/bin/env python3

__day__  = 10

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 1


class Navigation:

    def __init__(self):
        self.pairs = [ '()', '[]', '{}', '<>' ]
        self.points = {
            ')': 3,
            ']': 57,
            '}': 1197,
            '>': 25137
        }
        #
        self.bra_open   = [ br[0] for br in self.pairs ]
        self.bra_close  = [ br[1] for br in self.pairs ]
        self.bra_expect = dict([(br[0], br[1]) for br in self.pairs])

    def syntax_check_line(self, linenum1:int, line: str):
        # empty stack
        stack = []
        for pos0,char in enumerate(line):
            # on each openning char pust closing char to the stack
            if char in self.bra_open:
                expect = self.bra_expect[char]
                stack.append(expect)
            elif char in self.bra_close:
                # empty stack
                if len(stack) == 0:
                    if verbose: print('line %d - unexpected closing %s at pos %d' % (linenum1, char, pos0+1))
                    return char
                expect = stack.pop()
                if char != expect:
                    if verbose: print('line %d - expected %s got %s at pos %d' % (linenum1, expect, char, pos0+1))
                    return char
            else:
                if verbose: print('line %d - invalid char %s at pos %d' % (linenum1, char, pos0+1))
                return char
                # non empty stack
        if len(stack) > 0:
            if verbose: print('line %d - incomplete, missing %d closing chars' % (linenum1, len(stack)))
        #
        return None

    def calc_score(self, errors: list):
        score = 0
        for char in errors:
            score += self.points[char]
        return score

    def syntax_check(self, input: list):
        errors = []
        for linenum0,line in enumerate(input):
            errchar = self.syntax_check_line(linenum0+1, line)
            if errchar: errors.append(errchar)
        return errors

    def task_a(self, input: list):
        """ task A """
        errors = self.syntax_check(input)
        return self.calc_score(errors)

    def task_b(self, input: list):
        """ task B """
        return None


def testcase_a(sut, input, result):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ line.strip() for line in f ]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ line.strip() for line in input.splitlines() ]
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
            input = [ line.strip() for line in f ]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ line.strip() for line in input.splitlines() ]
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
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Navigation(), testdata,  26397)

# 345441
testcase_a(Navigation(),   None,   345441)

