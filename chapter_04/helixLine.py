# -*- coding: utf-8 -*-

from turtle import *


class HexlixLine:
    myTurtle = Turtle()
    myWin = myTurtle.getscreen()

    def draw(self, lineLen):
        """
        递归绘制螺旋线
        """
        # 调整绘图的起点
        self.myTurtle.up()
        self.myTurtle.backward(int(lineLen/2))
        self.myTurtle.left(90)
        self.myTurtle.forward(int(lineLen/2))
        self.myTurtle.right(90)
        self.myTurtle.down()

        # 绘制螺旋线
        self.drwaSpiral(self.myTurtle, lineLen)
        # 点击屏幕退出
        self.myWin.exitonclick()

    def drwaSpiral(self, myTurtle, lineLen):
        """
        绘制螺旋线
        """
        if lineLen > 0:
            myTurtle.forward(lineLen)
            myTurtle.right(90)
            self.drwaSpiral(myTurtle, lineLen - 5)

    def tree(self, branchLen):
        """
        递归绘制分形树
        """
        t = self.myTurtle
        # 调整树的起点
        t.left(90)
        t.up()
        t.backward(360)
        t.down()
        t.color("green")
        # 绘制分形树
        self.drawTree(branchLen, t)
        # 点击退出
        self.myWin.exitonclick()

    def drawTree(self, branchLen, t):
        """
        绘制分形树
        """
        if branchLen > 5:
            t.forward(branchLen)
            t.right(20)
            self.drawTree(branchLen-15, t)
            t.left(40)
            self.drawTree(branchLen-15, t)
            t.right(20)
            t.backward(branchLen)


    def drawTriangle(self, degree):
        """
        递归绘制谢尔平斯基三角形
        """
        t = self.myTurtle
        # 三角形的3顶点坐标
        point = [(-300, -200), (0, 200), (300, -200)]
        # 绘制谢尔平斯基三角形
        self.sierpinski(point, degree, t)
        # 点击时退出
        self.myWin.exitonclick()


    def triangle(self, point, color, t):
        """
        绘制三角形并填充
        """
        t.fillcolor(color)
        t.up()
        t.goto(point[0])
        t.down()
        t.begin_fill()
        t.goto(point[1])
        t.goto(point[2])
        t.goto(point[0])
        t.end_fill()
    
    def getMid(self, p1, p2):
        """
        获取两点的中点
        """
        return ((p1[0]+p2[0])/2, (p1[1] + p2[1])/2)

    def sierpinski(self, points, degree, t):
        """
        绘制谢尔平斯基三角形
        """
        # 谢尔平斯基三角形 色阶
        colorMap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange', 'black', 'pink']

        self.triangle(points, colorMap[degree], t)
        if degree > 0:
            self.sierpinski([points[0], self.getMid(points[0], points[1]), self.getMid(points[0], points[2])], degree - 1, t)
            self.sierpinski([points[1], self.getMid(points[0], points[1]), self.getMid(points[1], points[2])], degree - 1, t)
            self.sierpinski([points[2], self.getMid(points[0], points[2]), self.getMid(points[1], points[2])], degree - 1, t)


if __name__ == "__main__":
    hexlixLine = HexlixLine()
    # hexlixLine.draw(320)
    # hexlixLine.tree(120)
    hexlixLine.drawTriangle(5)

