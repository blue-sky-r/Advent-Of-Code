#!/usr/bin/env python3

__day__  = 4

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-04'

verbose = 0


class Scratchboard:

    def __init__(self):
        pass

    def card_worth(self, card: dict) -> int:
        """ calc single card worth """
        match = [ win for win in card['win'] for num in card['num'] if win == num ]
        worth = 2 ** (len(match) - 1)
        return worth if len(match) > 0 else 0

    def cards_worth(self, cards: dict) -> list:
        """ calc cards worth """
        worth = []
        for cardid,card in cards.items():
            w = self.card_worth(card)
            worth.append(w)
        return worth

    def parse_card(self, card: str) -> tuple:
        """ parse single card Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53 """
        cardtxt, numbers = card.split(':')
        cardid = int(cardtxt.replace('Card ', ''))
        winstr, numstr = numbers.split('|')
        return cardid, {
                'win': winstr.split(),
                'num': numstr.split()
        }

    def parse_cards(self, cards: list) -> dict:
        """ cards { id: {win: [], num: []} } """
        cardsdict = {}
        for card in cards:
            id, winnum = self.parse_card(card)
            cardsdict[id] = winnum
        return cardsdict

    def task_a(self, input: list):
        """ task A """
        cards = self.parse_cards(input)
        worth = self.cards_worth(cards)
        return sum(worth)

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
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Scratchboard(), testdata,  13)

# 22897
testcase_a(Scratchboard(),   None,  22897)

# ========
#  Task B
# ========

# test cases
#testcase_b(C(), testdata,  2)

# 2
#testcase_b(C(),   None,    2)
