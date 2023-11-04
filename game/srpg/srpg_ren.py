"""renpy
init -1 python:
"""

class srpgUnit:
    def __init__(self, name, hp, mp, beginx, beginy, idleImage, walkImage, attackImage):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.curx = beginx
        self.cury = beginy
        self.skills = []

        self.idleImage = idleImage
        self.walkImage = walkImage
        self.attackImage = attackImage

    def getPos(self):
        return srpgBoardPos(self.curx, self.cury)

class srpgSkeleton(srpgUnit):
    def __init__(self, beginx, beginy):
        print(beginx, beginy)
        super(srpgSkeleton, self).__init__("해골기사님",
                                            100, 100,
                                            beginx, beginy,
                                            "skeleton idle",
                                            "skeleton walk",
                                            "skeleton attack")

def srpgBoardPos(x, y):
    centerx = 1920 // 2
    centery = 1080 // 2

    xpos = centerx + (x - 3) * 200
    ypos = centery + (y - 2) * 200

    return (xpos, ypos)