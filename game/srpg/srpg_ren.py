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