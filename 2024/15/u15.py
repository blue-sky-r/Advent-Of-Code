#!/usr/bin/env python3

__motd__ = "--- Day 15: Warehouse Woes ---"

__url__ = "http://adventofcode.com/2024/day/15"

verbose = 0


class WarehouseRobot:

    def __init__(self):
        pass

    def display(self, warehousedim, robot, label=""):
        if verbose == 0:
            return
        warehouse, dim = warehousedim
        dimx, dimy = dim
        print(label)
        for y in range(dimy):
            for x in range(dimx):
                sym = warehouse.get((x, y), ".")
                if (x,y) == robot:
                    sym = '@' if sym == '.' else 'E'
                print(sym, end="")
            print()
        print()
        return

    def move(self, warehousedim, robot, dir):
        """ single move in direction dir <>^v """
        # unpack
        warehouse, dim = warehousedim
        dimx, dimy = dim
        # <
        if dir == '<':
            sym = warehouse.get((robot[0]-1, robot[1]), ".")
            # free, just move
            if sym == '.':
                robot = robot[0]-1, robot[1]
            # wall
            if sym == '#':
                pass
            # object
            if sym == 'O':
                # imduces of free '.' fields
                row = robot[1]
                #idx = [x for x in range(robot[0]-1, 0, -1) if warehouse.get((x,row),'.') == '.' and]
                idx = []
                for x in range(robot[0]-1, 0, -1):
                    s = warehouse.get((x,row),'.')
                    if s == '.':
                        idx.append(x)
                    if s == '#':
                        break
                if len(idx) > 0:
                    # move objects from index of rightmost '.' to the robotx-1 the left
                    for x in range(idx[0], robot[0]-1):
                        warehouse[(x, row)] = warehouse[(x+1, row)]
                    # move robot
                    robot = robot[0]-1, robot[1]
            #
        # >
        if dir == '>':
            sym = warehouse.get((robot[0]+1, robot[1]), ".")
            # free, just move
            if sym == '.':
                robot = robot[0]+1, robot[1]
            # wall
            if sym == '#':
                pass
            # object
            if sym == 'O':
                # closest left free '.' field idx
                row = robot[1]
                #idx = [x for x in range(robot[0]+1, dimx) if warehouse.get((x,row),'.') == '.']
                idx = []
                for x in range(robot[0]+1, dimx):
                    s = warehouse.get((x,row),'.')
                    if s == '.':
                        idx.append(x)
                    if s == '#':
                        break
                if len(idx) > 0:
                    # move objects from robotx to index of leftmost '.' to the right
                    for x in range(idx[0], robot[0]+1, -1):
                        warehouse[(x, row)] = warehouse[(x-1, row)]
                    # move robot
                    robot = robot[0]+1, robot[1]
            #
        # ^
        if dir == '^':
            sym = warehouse.get((robot[0], robot[1]-1), ".")
            # free, just move
            if sym == '.':
                robot = robot[0], robot[1]-1
            # wall
            if sym == '#':
                pass
            # object
            if sym == 'O':
                # idices of free '.' field idx (slosest first)
                col = robot[0]
                #idx = [y for y in range(robot[1]-1, 0, -1) if warehouse.get((col,y),'.') == '.']
                idx = []
                for y in range(robot[1]-1, 0, -1):
                    s = warehouse.get((col,y),'.')
                    if s == '.':
                        idx.append(y)
                    if s == '#':
                        break
                if len(idx) > 0:
                    # move objects from robotx to index of leftmost '.' to the right
                    for y in range(idx[0], robot[1]-1):
                        warehouse[(col, y)] = warehouse[(col, y+1)]
                    # move robot
                    robot = robot[0], robot[1]-1
            #
        # v
        if dir == 'v':
            sym = warehouse.get((robot[0], robot[1]+1), ".")
            # free, just move
            if sym == '.':
                robot = robot[0], robot[1]+1
            # wall
            if sym == '#':
                pass
            # object
            if sym == 'O':
                # idices of free '.' field idx (slosest first)
                col = robot[0]
                #idx = [y for y in range(robot[1]+1, dimy) if warehouse.get((col,y),'.') == '.']
                idx = []
                for y in range(robot[1]+1, dimy):
                    s = warehouse.get((col,y),'.')
                    if s == '.':
                        idx.append(y)
                    if s == '#':
                        break
                if len(idx) > 0:
                    # move objects from robotx to index of leftmost '.' to the right
                    for y in range(idx[0], robot[1]+1, -1):
                        warehouse[(col, y)] = warehouse[(col, y-1)]
                    warehouse[robot] = '.'
                    robot = robot[0], robot[1]+1
            #
        warehouse[robot] = '.'
        return warehousedim, robot

    def domoves(self, warehousedim, robot, moves):
        """ do moves """
        for step0, dir in enumerate(moves):
            warehousedim, robot = self.move(warehousedim, robot, dir)
            self.display(warehousedim, robot, f'= step {step0+1} dir {dir} =')
        return warehousedim, robot

    def gps(self, warehousedim):
        warehouse, dim = warehousedim
        l = [ xy[0] + 100 * xy[1] for xy,sym in warehouse.items() if sym == 'O' ]
        return l

    def parseinput(self, input):
        input = input if type(input) == list else input.strip().splitlines()
        warehouse, robot, moves = {}, (), []
        for y, line in enumerate(input):
            # warehouse map
            if "#" in line:
                for x, sym in enumerate(line):
                    # robot ?
                    if sym == '@':
                        robot = x,y
                        continue
                    warehouse[(x, y)] = sym
                dimx = x
                dimy = y
                continue
            if "^" in line or "v" in line:
                moves.append(line)
        return (warehouse, (dimx+1,dimy+1)), robot, ''.join(moves)

    def task_a(self, input):
        """task A"""
        warehousedim, robot, moves = self.parseinput(input)
        self.display(warehousedim, robot, "= initial state =")
        warehousedim, robot = self.domoves(warehousedim, robot, moves)
        gps = self.gps(warehousedim)
        return sum(gps)

    def task_b(self, input):
        """task B"""
        return


def testcase(sut, input, result, task_b=False):
    """testcase verifies if input returns result"""
    # read default input file
    if input is None:
        data = __file__.replace(".py", ".input")
        with open(data) as f:
            input = [line.strip() for line in f]
    #
    print(f"TestCase {"B" if task_b else "A"} ", end="")
    print(f"for input: {data if 'data' in vars() else input}", end="")
    print(f"\t expected result: {result} ", end="")
    r = sut.task_a(input) if not task_b else sut.task_b(input)
    print(f"got: {r} \t {'[ OK ]' if r == result else '[ ERR ]'}")
    print()


# ========
#  Task A
# ========

input = """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""
# test cases
testcase(WarehouseRobot(), input, 2028)

input = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""
# test cases
testcase(WarehouseRobot(), input, 10092)

# 1527563
testcase(WarehouseRobot(), None, 1527563)

