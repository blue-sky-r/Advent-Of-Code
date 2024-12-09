#!/usr/bin/env python3

__motd__ = "--- Day 5: Print Queue ---"

__url__ = "http://adventofcode.com/2024/day/5"


verbose = 0


class PageOrdering:

    def parserulesupdates(self, input):
        """Parse rules and updates from input."""
        rules, updates = {}, []
        # rules 47|53 = page 47 has to be before page 53
        for line in input if type(input) == list else input.splitlines():
            # rules
            if "|" in line:
                a, b = line.split("|")
                a, b = int(a), int(b)
                ra = rules.get(a, [])
                ra.append(b)
                rules[a] = ra
                continue
            # updates
            if "," in line:
                pages = [int(page) for page in line.split(",")]
                updates.append(pages)
        return rules, updates

    def updateok(self, update: list, rules: dict) -> bool:
        """Check if update is ok according to rules."""
        for pageidx, page in enumerate(update):
            if page in rules:
                tails = rules[page]
                for tail in tails:
                    if tail in update:
                        tailidx = update.index(tail)
                        if not tailidx > pageidx:
                            return False
        return True

    def correctlyordered(self, updates: list, rules: dict) -> list:
        """Check if pages are correctly ordered based on ordering rules"""
        correct = []
        for update in updates:
            if self.updateok(update, rules):
                correct.append(update)
        return correct

    def fixupdate(self, update: list, rules: dict) -> list:
        """Check if update is ok according to rules."""
        fixed = update
        for pageidx, page in enumerate(update):
            if page in rules:
                tails = rules[page]
                for tail in tails:
                    if tail in update:
                        tailidx = update.index(tail)
                        if tailidx > pageidx: continue
                        # fix by swapping pageidx <=> tailidx
                        fixed[pageidx], fixed[tailidx] = fixed[tailidx], fixed[pageidx]
        return fixed

    def fixincorrectlyordered(self, updates: list, rules: dict) -> list:
        """Check if pages are correctly ordered based on ordering rules"""
        corrected = []
        for update in updates:
            if self.updateok(update, rules): continue
            # need a fix
            fixed = update
            # repeateadly fix
            while not self.updateok(update, rules):
                fixed = self.fixupdate(fixed, rules)
            corrected.append(fixed)
        return corrected

    def summiddle(self, correct: list[list[int]]) -> int:
        """Return the sum of the middle elements of the list."""
        middle = []
        for updatelist in correct:
            midx = len(updatelist) // 2
            mpage = updatelist[midx]
            middle.append(mpage)
        return sum(middle)

    def task_a(self, input):
        """task A"""
        rules, updates = self.parserulesupdates(input)
        correct = self.correctlyordered(updates, rules)
        res = self.summiddle(correct)
        return res

    def task_b(self, input):
        """task B"""
        rules, updates = self.parserulesupdates(input)
        corrected = self.fixincorrectlyordered(updates, rules)
        res = self.summiddle(corrected)
        return res


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
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
# test cases
testcase(PageOrdering(), input, 143)

# 3608
testcase(PageOrdering(), None, 3608)

# ========
#  Task B
# ========

# test cases
testcase(PageOrdering(), input, 123, task_b=True)

# 4922
testcase(PageOrdering(), None, 4922, task_b=True)
