# -*- coding: utf-8 -*-

class BinaryTree:
    """
    利用节点与引用创建二叉树
    """
    
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None


    def insertLeft(self, newNode):
        """
        插入左节点
        """
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        """
        插入右节点
        """
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        """
        返回当前节点的右节点和对应的二叉树
        """
        return self.rightChild

    def getLeftChild(self):
        """
        返回当前节点的左节点和对应的二叉树
        """
        return self.leftChild

    def getRootVal(self):
        """
        获取当前节点的数值
        """
        return self.key

    def setRootVal(self, obj):
        """
        存储当前节点的数值
        """
        self.key = obj

