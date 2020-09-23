# -*- coding: utf-8 -*-

import random
import time

class CalculateSum:
    # Simplate Sum

    def listSum(self, numList):
        assert isinstance(numList, (list, tuple, set))
        sumNum = 0
        for num in numList:
            sumNum += num
        return sumNum

    def recursiveNum(self, numList):
        if len(numList) != 1:
            return numList[0] + self.recursiveNum(numList[1:])
        else:
            return numList[0]


if __name__ == "__main__":
    simpleNumList = [random.randint(320, 1200) for _ in range(920)]
    reSum = CalculateSum()
    cur = time.time()
    print(reSum.listSum(simpleNumList))
    print("Normal CostTime: ", time.time() - cur)
    cur = time.time()
    print(reSum.recursiveNum(simpleNumList))
    print("Recursive CostTime: ", time.time() - cur)