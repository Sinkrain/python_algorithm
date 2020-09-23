# -*- coding: utf-8 -*-
import sys
from chapter_03.stack import Stack


class RStack:

    rStack = Stack()
    convertString = "0123456789ABCDEF"
        
    def formatHex(self, n, base):
        self.toStr(n, base)
        hexNum = ""
        while not self.rStack.isEmpty():
            hexNum += self.rStack.pop()
        return hexNum
        

    def toStr(self, n , base):
        assert isinstance(n , int)
        assert isinstance(base, int)
        assert base <= len(self.convertString) 
        if n < base:
            self.rStack.push(self.convertString[n])
        else:
            self.rStack.push(self.convertString[n % base])
            self.toStr(n//base, base)


if __name__ == "__main__":
    number = 1231323124125412
    rStack = RStack()
    print(rStack.formatHex(number, 2))
    print(rStack.formatHex(number, 3))
    print(rStack.formatHex(number, 5))
    print(rStack.formatHex(number, 7))