# -*- coding: utf-8 -*-

"""
中序表达式转后序表达式, 并计算
"""
import re
import operator
import string
from chapter_03.stack import Stack


class PostOrderConversion:

    def conversionToPostOrder(self, inOrdErexpr):
        """
        后序转换
        """
        # 构建运算符优先级字典
        prec = {
            "*": 3,
            "/": 3,
            "+": 2,
            "-": 2,
            "(": 1,
            ")": 1
        }

        if not self.parseChecker(inOrdErexpr):
            raise ValueError

        opStack = Stack()
        postOrderList = list()
        exprList = inOrdErexpr.split()

        for ch in exprList:
            if ch.isdigit():
                postOrderList.append(ch)
            elif ch == "(":
                opStack.push(ch)
            elif ch == ")":
                topOper = opStack.pop()
                while topOper != "(":
                    postOrderList.append(topOper)
                    topOper = opStack.pop()
            else:
                # 比较运算符优先级，如果栈中运算符的优先级>当前运算符， 追加至转换列表中
                while (not opStack.isEmpty()) and (prec[opStack.peek()] > prec[ch]):
                    postOrderList.append(opStack.pop())
                opStack.push(ch)
        # 将栈中的运算符追加至转换列表中
        while not opStack.isEmpty():
            postOrderList.append(opStack.pop())
        return "".join(postOrderList)

    def calculatePostOrderFormulas(self, postOrderformulas):
        """
        计算后序表达式
        """
        operaDict = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        postStack = Stack()
        postOrderList = list(postOrderformulas)
        for ch in postOrderList:
            if ch.isdigit():
                postStack.push(eval(ch))
            else:
                opN1 = postStack.pop()
                opN2 = postStack.pop()
                postStack.push(operaDict[ch](opN2, opN1))
        return postStack.pop()

    def parseChecker(self, symbolStr):
        """
        判断括号是否完全匹配
        """
        symbolStr = self.extractBrackets(symbolStr)
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
                if self.matches(topSym, symbol):
                    balanced = False
            index += 1
        if balanced and s.isEmpty():
            return True
        else:
            return False

    def extractBrackets(self, formulas):
        regex = re.compile(r'[{\[()\]}]')
        return "".join(regex.findall(formulas))

    def matches(self, open, close):
        opens = "{[("
        closers = "}])"
        return opens.index(opens) == closers.index(close)

if __name__ == "__main__":
    formulas1 = "( 1 + 2 ) * 3"
    formulas2 = "5 + 6 * 7"
    postConversion = PostOrderConversion()
    cFormulas1 = postConversion.conversionToPostOrder(formulas1)
    cFormulas2 = postConversion.conversionToPostOrder(formulas2)
    print("formulas1: %s | formulas1: %s" % (cFormulas1, cFormulas1))
    print("formulas1: %s=" % formulas1, postConversion.calculatePostOrderFormulas(cFormulas1))
    print("formulas2: %s=" % formulas2, postConversion.calculatePostOrderFormulas(cFormulas2))

