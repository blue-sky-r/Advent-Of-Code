#!/usr/bin/env python3

__day__  = 11

__year__ = 2022

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Monkey:

    def __init__(self):
        self.inspectcnt = 0

    def init_from_list(self, l: list):
        """ init Monkey from list of lines """
        # Monkey 0:
        _monkey_, id = l[0].split()
        self.id = int(id[:-1])
        #   Starting items: 79, 98
        _starting_, _items_, csl = l[1].split(maxsplit=2)
        self.items = [ int(i) for i in csl.split(', ')]
        #   Operation: new = old * 19
        _operation_, new_eq_old = l[2].split(maxsplit=1)
        _new_, _eq_, self.operation = new_eq_old.partition('=')
        #   Test: divisible by 23
        _test_, _div_, _by_, divider = l[3].split()
        self.divider = int(divider)
        self.throwto = {}
        #     If true: throw to monkey 2
        _if_, _truefalse_, _throw_, _to_, _monkey_, id = l[4].split()
        key = True if _truefalse_ == 'true:' else False
        self.throwto[key] = int(id)
        #     If false: throw to monkey 3
        _if_, _truefalse_, _throw_, _to_, _monkey_, id = l[5].split()
        key = False if _truefalse_ == 'false:' else False
        self.throwto[key] = int(id)
        #
        return 6

    def print(self, txt='', details=False):
        """ visualize """
        if not verbose: return
        if txt: print('-',txt,'-')
        print('Monkey:', self.id)
        print('\t items:', self.items)
        print('\t inspect cnt:', self.inspectcnt)
        if details:
            print('\t operation:', self.operation)
            print('\t divider:', self.divider)
            print('\t \t True :', self.throwto[True])
            print('\t \t False:', self.throwto[False])
        print()


class MiM:

    def __init__(self):
        self.monkeys = []
        pass

    def print_monkeys(self, txt):
        print('=', txt, '=')
        for m in self.monkeys:
            m.print()

    def parse_monkeys(self, input: list):
        """ parse list of strings and create monkeys """
        idx = 0
        while idx < len(input):
            line = input[idx]
            if line.startswith('Monkey'):
                m = Monkey()
                idx += m.init_from_list(input[idx:])
                self.monkeys.append(m)
                m.print('init')
            idx += 1
        return len(self.monkeys)

    def round(self, worrydiv=3, debug=False):
        """ """
        for idx, monkey in enumerate(self.monkeys):
            if debug: monkey.print('before round')
            for item in monkey.items:
                # init worry-level
                worrylevel = item
                # count inspections
                monkey.inspectcnt += 1
                # inspection impact on worry-level
                vars = { 'old': worrylevel }
                worrylevel = eval(monkey.operation, {}, vars)
                # monkey gets bored, worrylevel / 3
                if worrydiv:
                    worrylevel = int(worrylevel / worrydiv)
                # test / decision
                decision = (worrylevel % monkey.divider) == 0
                # throw to monkey
                targetid = monkey.throwto[decision]
                self.monkeys[targetid].items.append(worrylevel)
                # debug
                if debug: print('monkey:', monkey.id, 'throws', worrylevel, 'to monkey:', targetid)
            # all items thrown
            monkey.items = []
            # debug
            if debug: monkey.print('after round')

    def monkey_business(self):
        """ get monkey business """
        ins_cnt = [ m.inspectcnt for m in self.monkeys ]
        top2 = sorted(ins_cnt)[-2:]
        return top2[-2] * top2[-1]

    def task_a(self, input: list):
        """ task A """
        self.parse_monkeys(input)
        for rnd in range(20):
            self.round()
            if verbose: self.print_monkeys('after round %s' % (rnd+1))
        return self.monkey_business()

    def task_b(self, input: list):
        """ task B """
        self.parse_monkeys(input)
        for rnd in range(10000):
            if (rnd % 100) == 0: print(rnd, end=' ', flush=True)
            self.round(worrydiv=None)
            if verbose: self.print_monkeys('after round %s' % (rnd+1))
        return self.monkey_business()


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
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

# ========
#  Task A
# ========

# test cases
testcase_a(MiM(), testdata, 10605)

# 98280
testcase_a(MiM(),   None,   98280)

# ========
#  Task B
# ========

# test cases - takes too long
# TODO: much faster implementation required
testcase_b(MiM(), testdata,  2713310158)

# ?
testcase_b(MiM(),   None,   1)
