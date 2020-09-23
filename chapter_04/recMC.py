# -*- coding: utf-8 -*-
# 动态规划
# 贪婪算法

class RecMC:
    """
    实现找零时使用最少的硬币
    """

    def __init__(self, coinValueList):
        # 硬币数额列表
        self.coinValueList = coinValueList

    def recMc(self, change):
        # 默认初始硬币的数量=数值（拥有1毛的硬币）
        minCoins = change
        if change in self.coinValueList:
            # 如果数额刚好=硬币的数额， 仅需一次
            return 1
        else:
            # 找零的硬币数值必须小于找零数值
            # 如果存在可以找零的大额硬币，优先使用大额硬币，1毛硬币兜底
            for i in [c for c in self.coinValueList if c <= change]:
                print(change-i, "|".center(6, " "), i)
                numCoins = 1 + self.recMc(change - i)
                if numCoins < minCoins:
                    minCoins = numCoins
        return minCoins

    def recDc(self, change, knownResults):
        minCoins = change
        if change in self.coinValueList:
            knownResults[change] = 1
            return 1
        elif knownResults[change] > 0:
            return knownResults[change]
        else:
            for i in [c for c in self.coinValueList if c <= change]:
                numCoins = 1 + self.recDc(change - i, knownResults)
                if numCoins < minCoins:
                    minCoins = numCoins
                    knownResults[change] = minCoins
            return minCoins



if __name__ == "__main__":
    recMC = RecMC([1, 5, 10])
    print(recMC.recMc(32))
    print("main".center(32, "="))
    print(recMC.recDc(63, [0]*64))