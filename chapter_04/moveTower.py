# -*- coding: utf-8 -*-

class MoveTower:

    def moveTower(self, height, fromPole, toPole, withPole):
        if height >=1:
            self.moveTower(height - 1, fromPole, withPole, toPole)
            self.moveDisk(fromPole, toPole)
            self.moveTower(height - 1, withPole, toPole, fromPole)

    def moveDisk(self, fromPole, toPole):
        print("Moving disk form %d to %d" % (fromPole, toPole))