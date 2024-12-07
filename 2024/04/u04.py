#!/usr/bin/env python3

__motd__ = "--- Day 4: Ceres Search ---"

__url__ = "http://adventofcode.com/2024/day/4"


verbose = 0


class WordSearch:

    def __init__(self):
        pass

    def buildmap(self, input):
        """ """
        m = {}
        for y, line in enumerate(
            input if type(input) == list else input.strip().splitlines()
        ):
            for x, sym in enumerate(line):
                m[(x, y)] = sym
        return m, (x, y)

    def xystep(self, xy: tuple, dir: str) -> tuple:
        """
        NW N NE
        W  X  E
        SW S SE
        """
        # untuple
        x, y = xy
        # dir
        match dir:
            case "N":
                return (x, y - 1)
            case "S":
                return (x, y + 1)
            case "E":
                return (x + 1, y)
            case "W":
                return (x - 1, y)
            case "NW":
                return (x - 1, y - 1)
            case "NE":
                return (x + 1, y - 1)
            case "SW":
                return (x - 1, y + 1)
            case "SE":
                return (x + 1, y + 1)

    def xyvalid(self, xy: tuple, dim: tuple) -> bool:
        """validate xy is within map dimensions"""
        # untuple
        x, y = xy
        dimx, dimy = dim
        # check
        return 0 <= x <= dimx and 0 <= y <= dimy

    def walk(self, map: dict, dim: tuple, xy: tuple, limit: int) -> list[str]:
        """walk in all 8 directions from xy and return list of words"""
        words = []
        for dir in ["N", "E", "S", "W", "NW", "NE", "SW", "SE"]:
            newxy, symbols = xy, [map[xy]]
            while True:
                newxy = self.xystep(newxy, dir)
                # end if out of the map
                if not self.xyvalid(newxy, dim):
                    break
                # valid symbol
                symbols.append(map[newxy])
                # end if length limit reached
                if len(symbols) >= limit:
                    break
            if symbols:
                words.append("".join(symbols))
        return words

    def walkcross(self, map: dict, dim: tuple, xy: tuple) -> list[str]:
        """walk in X cross fashion arounf xy center
        NW   NE
           X
        SW   SE
        """
        words = []
        # untuple
        x, y = xy
        dimx, dimy = dim
        # valid xy ?
        if 0 < x < dimx and 0 < y < dimy:
            # xy
            nwse = [self.xystep(xy, "NW"), xy, self.xystep(xy, "SE")]
            nesw = [self.xystep(xy, "NE"), xy, self.xystep(xy, "SW")]
            senw = [self.xystep(xy, "SE"), xy, self.xystep(xy, "NW")]
            swne = [self.xystep(xy, "SW"), xy, self.xystep(xy, "NE")]
            # xy to symbols ans words
            for xy3 in [nwse, nesw, senw, swne]:
                word = "".join([map[xy] for xy in xy3])
                words.append(word)
        return words

    def findxyforsymbol(self, map: dict, symbol: chr) -> list[tuple]:
        """find all xy for a symbol"""
        return [xy for xy, sym in map.items() if sym == symbol]

    def wordcount(self, map, dim, word: str) -> int:
        """count all words word in map"""
        cnt = 0
        for xy in self.findxyforsymbol(map, word[0]):
            words = self.walk(map, dim, xy, len(word))
            match = [w for w in words if w.startswith(word) or w.startswith(word[::-1])]
            cnt += len(match)
            if verbose:
                print(f"cnt:{cnt} \t xy:{xy} \t match:{match} \t words:{words}")
        return cnt

    def crosscount(self, map, dim, word: str) -> int:
        """count all words word in map"""
        cnt = 0
        for xy in self.findxyforsymbol(map, word[1]):
            words = self.walkcross(map, dim, xy)
            if words.count(word) == 2:
                cnt += 1
            if verbose:
                print(f"cnt:{cnt} \t xy:{xy} \t words:{words}")
        return cnt

    def task_a(self, input):
        """task A"""
        map, dim = self.buildmap(input)
        cnt = self.wordcount(map, dim, "XMAS")
        return cnt

    def task_b(self, input):
        """task B"""
        map, dim = self.buildmap(input)
        cnt = self.crosscount(map, dim, "MAS")
        return cnt


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
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
# test cases
testcase(WordSearch(), input, 18)

# 2483
testcase(WordSearch(), None, 2483)

# ========
#  Task B
# ========

# test cases
testcase(WordSearch(), input, 9, task_b=True)

# 1925
testcase(WordSearch(), None, 1925, task_b=True)
