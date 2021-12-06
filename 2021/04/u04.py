#!/usr/bin/env python3

__day__  = 4

__year__ = 2021

__motd__ = '--- Year %s -- Day %s ---' % (__year__, __day__)

__url__ = 'http://adventofcode.com/%s/day/%s' % (__year__, __day__)

verbose = 0


class Field:

    def __init__(self, val):
        self.val = int(val)
        self.mark = False

    def set_mark(self):
        if self.is_marked(): return
        self.mark = True

    def is_marked(self):
        return self.mark

    def get_val(self):
        return self.val

    def visual(self):
        format = '[%3d]' if self.is_marked() else ' %3d '
        return format % self.get_val()


class Board:

    def __init__(self, idx, size=5):
        self.size = 5
        self.idx = idx
        self.data = []

    def print(self):
        print('=== board idx: ===',self.idx,'=== winning:',self.is_winning(),'===')
        for row in self.data:
            print(' '.join([f.visual() for f in row]))
        print()

    def add_row(self, row: list):
        assert len(row) == self.size, 'ERROR - row length %d does not match size %d !' % (len(row), self.size)
        self.data.append([Field(f) for f in row])

    def draw(self, num: int):
        for row in self.data:
            for f in row:
                if f.get_val() == num:
                    assert not f.is_marked(), 'ERROR - repeted draw of number %d' % num
                    f.set_mark()
                    return
        assert True, 'ERROR - drawn number %d not found on the board %d' % (num, self.idx)

    def is_winning(self):
        # check rows
        for row in self.data:
            if self.is_winning_row(row):
                return True
        # check columns
        for col in range(len(self.data[0])):
            # biuld virtual row from column
            vrow = [ self.data[row][col] for row in range(len(self.data))]
            if self.is_winning_row(vrow):
                return True
        return False

    def is_winning_row(self, row: list):
        return all([f.is_marked() for f in row])

    def sum_unmarked(self):
        unmarked = []
        for row in self.data:
            u = [f.get_val() for f in row if not f.is_marked()]
            unmarked.extend(u)
        return sum(unmarked)

    def score(self, drawn: int):
        su = self.sum_unmarked()
        return su * drawn


class Bingo:

    def __init__(self, size=5):
        self.drawn = None
        self.boards = []
        self.size = size

    def print(self):
        for board in self.boards:
            board.print()

    def winning_board(self):
        for board in self.boards:
            if board.is_winning():
                return board

    def draw(self, num: int):
        for board in self.boards:
            board.draw(num)

    def draw_until_win(self):
        # process all drawn nums
        for idx,num in enumerate(self.drawn):
            if verbose: print("# draw: %d # idx: %d #" % (num,idx))
            # draw
            self.draw(num)
            # optional visualize
            if verbose: self.print()
            # check winning
            board = self.winning_board()
            # exit if any boad has won
            if board is not None:
                return num, board
        return num, None

    def draw_until_win_all(self):
        not_winning_boards = self.boards[:]
        # process all drawn nums
        for idx,num in enumerate(self.drawn):
            if verbose: print("# draw: %d # idx: %d #" % (num,idx))
            # draw
            self.draw(num)
            # optional visualize
            if verbose: self.print()
            # check winning
            for board in not_winning_boards[:]:
                if board.is_winning():
                    not_winning_boards.remove(board)
            # exit if any boad has won
            if not_winning_boards == []:
                return num, board
        return num, None

    def process_input(self, input: list):
        """ list of strings """
        board_idx = 0
        for line in input:
            # drawn numbers
            if self.drawn is None:
                assert line.count(',') > 10, 'ERROR - invalid line with drawn numbers, expecting comma separated values'
                self.drawn = [ int(num) for num in line.split(',') ]
                continue
            # empty lines inc board idx
            if not line:
                board_idx += 1
                board = Board(idx=board_idx, size=self.size)
                self.boards.append(board)
                continue
            # add not empty line to the current board
            board.add_row(line.split())

    def task_a(self, input: list):
        """ task A """
        self.process_input(input)
        if verbose: self.print()
        drawn, board = self.draw_until_win()
        assert board is not None, "ERROR - no winning board found"
        return board.score(drawn)

    def task_b(self, input):
        """ task B """
        self.process_input(input)
        if verbose: self.print()
        drawn, board = self.draw_until_win_all()
        assert board is not None, "ERROR - all numbers has been drawn, but not all boards are winning"
        return board.score(drawn)


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
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

# ========
#  Task A
# ========

# test cases
testcase_a(Bingo(), testdata,  4512)

# 55770
testcase_a(Bingo(),   None,   55770)

# ========
#  Task B
# ========

# test cases
testcase_b(Bingo(), testdata,  1924)

# 2980
testcase_b(Bingo(),     None,  2980)
