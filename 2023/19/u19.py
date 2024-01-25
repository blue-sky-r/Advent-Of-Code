#!/usr/bin/env python3

__day__  = 19

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-19'

verbose = 0


class Workflow:

    def __init__(self):
        pass

    def ratings(self, parts: list) -> int:
        """ calc rations """
        values = [ val for part in parts for key,val in part.items() ]
        return sum(values)

    def part_path(self, rules: dict, part: dict) -> str:
        """ validate part by the rules """
        rule = 'in'
        path = [rule]
        # repeat until Accepted or rejected
        while rule not in ['A','R']:
            for condition, label in rules[rule]:
                boolresult = eval(condition, {}, part)
                if boolresult:
                    rule = label
                    path.append(rule)
                    break
        return path

    def accepted(self, rules: dict, parts: list) -> list:
        """ get accepted parts """
        ok = []
        for part in parts:
            path = self.part_path(rules, part)
            if verbose:
                print('Part:',part,'\t workflow:',path)
            # accepted ?
            if path[-1] == 'A':
                ok.append(part)
        return ok

    def parse_csr(self, csr: str) -> list:
        """ a<2006:qkq,m>2090:A,rfg """
        rules = []
        for condrule in csr.split(','):
            if ':' in condrule:
                condition, label = condrule.split(':')
            else:
                condition, label = 'True', condrule
            rules.append( (condition, label) )
        return rules

    def parse_csa(self, csa: str) -> dict:
        """ comma separated assignments x=787,m=2655,a=1222,s=2876 """
        vars = {}
        for a in csa.split(','):
            name, value = a.split('=')
            vars[name] = int(value)
        return vars

    def parse_parts(self, input: list) -> dict:
        """ {x=787,m=2655,a=1222,s=2876} """
        parts, skip = [], True
        for line in input:
            if skip:
                if not line:
                    skip = False
                continue
            part = self.parse_csa(line[1:-1])
            parts.append(part)
        return parts

    def parse_rules(self, input: list) -> dict:
        """ px{a<2006:qkq,m>2090:A,rfg} """
        rules = {}
        for line in input:
            if not line: break
            name, csr = line[:-1].split('{')
            rules[name] = self.parse_csr(csr)
        return rules

    def task_a(self, input: list):
        """ task A """
        rules = self.parse_rules(input)
        parts = self.parse_parts(input)
        accepted = self.accepted(rules, parts)
        r = self.ratings(accepted)
        return r

    def task_b(self, input: list):
        """ task B """
        return None


def testcase_a(sut, input, result, trim=str.rstrip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase A using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
        # optional delete the first empty line
        if len(input[0]) == 0:
            input = input[1:]
    #
    print("\t expected result:", result)
    r = sut.task_a(input)
    print('\t got:',r,'\t','[ OK ]' if r == result else '[ ERR ]')
    print()

def testcase_b(sut, input, result, trim=str.rstrip):
    """ testcase verifies if input returns result """
    # read default input file
    if input is None:
        data = __file__.replace('.py', '.input')
        with open(data) as f:
            input = [ trim(line) for line in f ]
            # file is single line only
            if len(input) == 1:
                input = input[0]
    #
    print("TestCase B using input:", data if 'data' in vars() else input)
    # read multiline string as input
    if input.count('\n') > 2:
        input = [ trim(line) for line in input.splitlines() ]
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
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Workflow(), testdata, 19114)

# 373302
testcase_a(Workflow(),   None,  373302)

