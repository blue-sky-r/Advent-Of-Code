#!/usr/bin/env python

__motd__ = '--- Day 9: Marble Mania ---'

__url__ = 'http://adventofcode.com/2018/day/9'


verbose = 0


class Marbles:

    def __init__(self, players=9):
        self.players = players
        self.board = [ 0 ]
        self.current = 0
        self.score = dict([ (x,[]) for x in range(self.players) ])

    def show(self, player=None):
        """ visualize """
        if player is None:
            print "[ - ]",
        else:
            print "[%3d ]" % player,
        print ' '.join([ "(%2d)" % m if i==self.current else "%3d " % m for i,m in enumerate(self.board) ])

    def place_cw(self, ball, offset=2):
        """ place ball clockwise
        [-] (0)
        [1]  0 (1)
        [2]  0 (2) 1
        [3]  0  2  1 (3)
        [4]  0 (4) 2  1  3
        """
        # special case if current is last_by_one -> append
        if self.current+1 == len(self.board)-1:
            idx = len(self.board)
        else:
            idx = (self.current + offset) % len(self.board)
        self.board.insert(idx, ball)
        self.current = idx

    def remove_ccw(self, offset=7):
        """ remove ball located ccw """
        # add redundant board length to make sure index>0
        idx = (self.current + len(self.board) - offset) % len(self.board)
        ball = self.board.pop(idx)
        self.current = idx
        return ball

    def next_player(self):
        """ next player number """
        pn = 0
        while True:
            pn = (pn + 1) % self.players
            yield pn

    def game(self, lastball):
        """ play game until the last ball is played """
        # player number generator
        pgen = self.next_player()
        # starting board
        if verbose: self.show()
        # play until ball value reach the lastball value
        for ball in range(1, lastball+1):
            # next player
            player = next(pgen)
            # check divisibility by 23
            if (ball % 23) == 0:
                # special rule - take ball
                self.score[player].append(ball)
                # remove another ball from board
                removedball = self.remove_ccw()
                # take also removed ball
                self.score[player].append(removedball)
            else:
                # place a new ball on board
                self.place_cw(ball)
            # display the board
            if verbose: self.show(player)

    def winner(self):
        """ winner and winning score """
        # count marbles
        agg = dict([ (player, sum(marbles)) for player, marbles in self.score.items()])
        win = max(agg, key=agg.get)
        return agg[win]

    def input_line(self, lst):
        """ highest marble """
        return lst[0]

    def task_a(self, input):
        """ task A """
        ballmax = self.input_line(input)
        self.game(ballmax)
        r = self.winner()
        return r

    def task_b(self, input):
        """ task B """
        return self.task_a(input)


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
testcase(Marbles(players=9),    [25],   32)
# 10 players; last marble is worth 1618 points: high score is 8317
testcase(Marbles(players=10), [1618],   8317)
# 13 players; last marble is worth 7999 points: high score is 146373
testcase(Marbles(players=13), [7999],   146373)
# 17 players; last marble is worth 1104 points: high score is 2764
testcase(Marbles(players=17), [1104],   2764)
# 21 players; last marble is worth 6111 points: high score is 54718
testcase(Marbles(players=21), [6111],   54718)
# 30 players; last marble is worth 5807 points: high score is 37305
testcase(Marbles(players=30), [5807],   37305)

# 446 players; last marble is worth 71522 points 390592
testcase(Marbles(players=446), [71522], 390592)

# ========
#  Task B
# ========

# last marble * 180
#
testcase(Marbles(players=446), [71522 * 180], 390592, task_b=True)

