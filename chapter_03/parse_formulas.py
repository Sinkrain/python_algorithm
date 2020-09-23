# -*- coding: utf-8 -*-

from chapter_03.stack import Stack


class ParseFormulas:

    def parseChecker(self, symbolStr):
        s = Stack()
        balanced = True
        index = 0
        while index < len(symbolStr) and balanced:
            symbol = symbolStr[index]
            if symbol in "{[(":
                s.push(symbol)
            elif s.isEmpty():
                balanced = False
            else:
                topSym = s.pop()
                if not self.matches(topSym, symbol):
                    balanced = False
            index += 1
        if balanced and s.isEmpty():
            return True
        else:
            return False

    def matches(self, open, close):
        opens = "{[("
        closers = "}])"
        return opens.index(open) == closers.index(close)