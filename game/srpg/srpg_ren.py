################################################################################
#
# SPDX-FileCopyrightText: © 2023 Shin Jin <djinius.shin@gmail.com>
#
# Turn Based Battle with Ren'Py
# https://blog.naver.com/djinius
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
# 2. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this source without specific prior written permission.
# 3. The name 'Atremius' must be credited in a commercial project.
#
# 렌파이로 턴제 전투를 만들어 보자
# https://blog.naver.com/djinius
#
# 이 소스코드는 아래 조건을 만족하는 한 자유롭게 변경하여 사용 및 배포 가능합니다.
# 1. 소스코드 상단에 이 저작권 문구와 아래 면책 조항을 유지해야 합니다.
# 2. 사전 서면 합의 없이 소스코드 저작자와 기여자의 이름을 이용하여 이 소스코드를 사용한 프로젝트를 보증하거나 홍보할 수 없습니다.
# 3. 상업용 프로젝트에 사용할 경우 '달납줄개'를 크레딧에 명시해야 합니다.
#
################################################################################

"""renpy
init -1 python:
"""

class srpgUnit:
    def __init__(self, name, hp, mp, beginx, beginy, idleImage, walkImage, attackImage, hitImage):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.curx = beginx
        self.cury = beginy
        self.skills = []

        self.idleImage = idleImage
        self.walkImage = walkImage
        self.attackImage = attackImage
        self.hitImage = hitImage

    def getPos(self):
        return srpgBoardPos(self.curx, self.cury)

    # pure virtual functions - 상속받는 클래스들은 이 함수를 반드시 구현해야 함
    def isFriendly(self): pass
    def getMoveRange(self): pass

    # 유닛 이동 함수
    def moveto(self, x, y):
        self.curx = x
        self.cury = y

class srpgSkeleton(srpgUnit):
    def __init__(self, beginx, beginy):
        super(srpgSkeleton, self).__init__("해골기사님",
                                            100, 100,
                                            beginx, beginy,
                                            "skeleton idle",
                                            "skeleton walk",
                                            "skeleton attack",
                                            "skeleton hit")

    def isFriendly(self):
        return True
    
    def getMoveRange(self):
        return 4

class srpgTrainingDummy(srpgUnit):
    def __init__(self, beginx, beginy):
        super(srpgTrainingDummy, self).__init__("훈련용 허수아비",
                                            100, 100,
                                            beginx, beginy,
                                            "trainingDummy idle",
                                            None,
                                            None,
                                            "trainingDummy hit")

    def isFriendly(self):
        return False

    def getMoveRange(self):
        return 0


def srpgBoardPos(x, y):
    centerx = 1920 // 2
    centery = 1080 // 2

    xpos = centerx + (x - 3) * 200
    ypos = centery + (y - 2) * 200

    return (xpos, ypos)

# 인접 좌표 얻기
def getAdjacentCoordinates(c):
    (x, y) = c
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

# 좌표 사용 가능 여부
def isCoordinateInMap(c):
    (x, y) = c
    if (x < 0) or (x >= 7):
        return False
    if (y < 0) or (y >= 5):
        return False
    return True

def getMovableCoordinates(unit):

    movableCoordinates = []
    visited = []

    for x in range(0, 7):
        movableCoordinates += [[False] * 5]
        visited += [[False] * 5]

    for u in forcesList:
        visited[u.curx][u.cury] = True

    visitedDistance = 0
    visitCoordinates = [(unit.curx, unit.cury)]
    nextCoordinates = []

    while visitedDistance < unit.getMoveRange():
        while visitCoordinates:
            # 인접 좌표를 얻어와서
            ncList = getAdjacentCoordinates(visitCoordinates.pop(0))

            for nc in ncList:
                if isCoordinateInMap(nc):
                    (x, y) = nc
                    # 해당 위치로 이동이 가능하면
                    if not visited[x][y]:
                        nextCoordinates.append(nc)
                        # 그 위치를 True로 설정한다.
                        movableCoordinates[x][y] = True
                        visited[x][y] = True

        visitCoordinates = nextCoordinates
        nextCoordinates = []

        # 유닛 이동 거리까지 반복하면 완료
        visitedDistance += 1

    return movableCoordinates