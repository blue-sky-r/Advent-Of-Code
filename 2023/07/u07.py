#!/usr/bin/env python3

__day__  = 7

__year__ = 2023

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

__version__ = '2023-12-01'

verbose = 0


class Cards:

    def __init__(self):
        self.cards = 'A K Q J T 9 8 7 6 5 4 3 2'.replace(' ','')
        self.strength = { i:idx for idx,i in enumerate(self.cards[::-1]) }

    def cards_key(self, cards: str) -> str:
        """ encode cards symbols to ASCII values for comparision """
        findreplace = [('A','E'), ('K','D'), ('Q','C'), ('J','B'), ('T','A')]
        key = cards
        for fnd,rplc in findreplace:
            key = key.replace(fnd, rplc)
        return key

    def counts(self, hand:str) -> list:
        """ reverse sorted (starting from max) count card occurences in a hand """
        cnt = [ (card,hand.count(card)) for card in self.cards ]
        return cnt

    def is_five_of_a_kind(self, cards_cnt: list) -> bool:
        """ is hand Five of a kind ? AAAAA """
        return cards_cnt[0][1] == 5

    def is_four_of_a_kind(self, cards_cnt: list) -> bool:
        """ is hand Four of a kind ? AABAA """
        return cards_cnt[0][1] == 4

    def is_full_house(self, cards_cnt: list) -> bool:
        """ is hand a full-house ? 23332 """
        return cards_cnt[0][1] == 3 and cards_cnt[1][1] == 2

    def is_three_of_a_kind(self, cards_cnt: list) -> bool:
        """ is hand three of a kind ? TTT98 """
        return cards_cnt[0][1] == 3

    def is_two_pair(self, cards_cnt: list) -> bool:
        """ is hand two pair ? 23432 """
        return cards_cnt[0][1] == 2 and cards_cnt[1][1] == 2

    def is_one_pair(self, cards_cnt: list) -> bool:
        """ is hand one pair ? A23A4 """
        return cards_cnt[0][1] == 2

    def is_high_card(self, cards_cnt: list) -> bool:
        """ is hand high card ? 23456 """
        return all(cnt == 1 for card,cnt in cards_cnt)

    def hand_key(self, hand: str) -> str:
        """ compose key from hand for comparision/sorting """
        rank_fnc = [
            ( 7, self.is_five_of_a_kind),
            ( 6, self.is_four_of_a_kind),
            ( 5, self.is_full_house),
            ( 4, self.is_three_of_a_kind),
            ( 3, self.is_two_pair),
            ( 2, self.is_one_pair),
            ( 1, self.is_high_card)
        ]
        counts = self.counts(hand)
        sorted_counts = sorted(counts, key=lambda card_count: card_count[1], reverse=True)
        #
        rank = max([0] + [ rank for rank, fnc in rank_fnc if fnc(sorted_counts) ])
        key = '%d-%s' % (rank, self.cards_key(hand))
        return key

    def order_hands(self, hand_bids: list) -> list:
        """ order hands_bids by adding hey """
        enriched = [ (hand,bid,self.hand_key(hand)) for hand,bid in hand_bids ]
        enriched_sorted = sorted(enriched, key=lambda hbk: hbk[2])
        return [ (hand, bid) for hand,bid,key in enriched_sorted ]

    def wins(self, hands_bids: list) -> list:
        """ calc winning for each hand """
        ordered_hands = self.order_hands(hands_bids)
        r = []
        for idx, hand_bid in enumerate(ordered_hands):
            hand, bid = hand_bid[0], hand_bid[1]
            win = bid * (idx+1)
            r.append(win)
        return r

    def parse_hands_bids(self, input: list) -> list:
        """ hand bid """
        r = []
        for line in input:
            hand, bidtxt = line.split()
            r.append( (hand, int(bidtxt)) )
        return r

    def task_a(self, input: list):
        """ task A """
        hands_bids = self.parse_hands_bids(input)
        wins = self.wins(hands_bids)
        return sum(wins)

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
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Cards(), testdata,  6440)

# 250474325
testcase_a(Cards(), None, 250474325)

