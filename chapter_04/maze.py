# -*- coding: utf-8 -*-

from turtle import *


class Maze:
    def __init__(self, mazeFileName):
        self.loadingMaze(mazeFileName)
        self.t = Turtle(shape='turtle')
        # 设置迷宫视图的大小
        setup(width=700, height=700)
        # 根据迷宫视图的大小初始化坐标轴(以视图的大小缩放迷宫，原始的墙体为1毫米厚)
        setworldcoordinates(-(self.columnsInMaze-1)/2-0.5, -(self.rowsInMaze-1)/2-0.5, (self.columnsInMaze-1)/2+0.5, (self.rowsInMaze-1)/2+0.5)

        self.drawMaze()

    def loadingMaze(self, mazeFileName):
        """
        载入迷宫文件， 并获取迷宫的初始信息：
        行数、列数、迷宫二维列表、起点位置
        迷宫文件：+ 墙，" " 路，S 起点
        """
        rowsInMaze = 0
        columnsInMaze = 0

        # 生成迷宫二维列表
        self.mazeList = list()
        with open(mazeFileName, 'r') as fMaze:
            for line in fMaze.readlines():
                for i, ch in enumerate(line):
                    if ch  == "S":
                        # 迷宫的起点位置
                        self.startRow = rowsInMaze
                        self.startCol = i
                rowsInMaze += 1
                self.mazeList.append(list(line))
                columnsInMaze = len(line)
        # 迷宫的总行数
        self.rowsInMaze = rowsInMaze
        # 迷宫的总列数
        self.columnsInMaze = columnsInMaze
        # 迷宫的xy轴转换，将迷宫由第一象限转换至坐标中心
        self.xTranslate = - columnsInMaze / 2
        self.yTranslate = - rowsInMaze / 2


    def drawMaze(self):
        """
        绘制迷宫
        """
        tracer(0)
        # 迷宫二维列表的第一层代表y周， 第二层表示x轴
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazeList[y][x] == "+":
                    self.drawCenterBox(x + self.xTranslate, y + self.yTranslate, 'tan')
                    self.t.color('black', 'blue')
        self.updatePosition(self.startCol, self.startRow)
        tracer(1)
 
    def drawCenterBox(self, x, y, color):
        """
        绘制墙体
        """
        self.t.up()
        self.t.goto(x-0.5,y-0.5)
        self.t.color('black', color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self, x, y):
        """
        根据坐标移动乌龟的位置
        """
        self.t.up()
        self.t.setheading(self.t.towards(x + self.xTranslate, y + self.yTranslate))
        self.t.goto(x + self.xTranslate, y + self.yTranslate)

    def dropBreadcrymb(self, color):
        """
        标记走过的路径
        """
        self.t.down()
        self.t.dot(color)
        self.t.up()

    def updatePosition(self, x, y, value=None):
        """
        刷新乌龟的位置
        " ": 路
        "+": 墙
        ".": 走过的路
        "-": 死胡同
        """
        if value:
            self.mazeList[y][x] = value
        self.moveTurtle(x, y)
        if value == " ":
            color = 'green'
        elif value == "+":
            color = 'red'
        elif value == ".":
            color = 'black'
        elif value == "-":
            color = 'red'
        else:
            color = None
        if color:
            self.dropBreadcrymb(color)

    def isExit(self, row, col):
        """
        判断是否找到出口
        """
        return (row == 0 or row == self.rowsInMaze -1 or col == 0 or col == self.columnsInMaze)

    def __getitem__(self, index):
        return self.mazeList[index]


    def searchFrom(self, startCol, startRow):
        """
        探索迷宫
        """
        # self.updatePosition(startCol, startRow)
        if self.mazeList[startRow][startCol] == "+":
            return False
        if self.mazeList[startRow][startCol] == ".":
            return False
        if self.isExit(startRow, startCol):
            self.updatePosition(startCol, startRow, "-")
            return True
        self.updatePosition(startCol,startRow, ".")

        found = self.searchFrom(startCol, startRow-1) or self.searchFrom(startCol-1, startRow) or self.searchFrom(startCol, startRow+1) or self.searchFrom(startCol+1, startRow)

        if found:
            self.updatePosition(startCol, startRow, "$")
        else:
            self.updatePosition(startCol, startRow, '-')
        return found
            

if __name__ == "__main__":
    maze = Maze("./maze_file.txt")
    maze.searchFrom(maze.startCol, maze.startRow)