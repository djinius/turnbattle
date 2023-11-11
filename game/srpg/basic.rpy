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

default forcesList = [srpgSkeleton(0, 1), srpgSkeleton(0, 3), srpgTrainingDummy(5, 2)]

default selectedFriend = None
default selectedFoe = None

default moveState = False

screen srpgBasic(setFriend = False):
    for x in range(0, 7):
        for y in range(0, 5):
            add Solid("#888"):
                xysize (198, 198)
                pos srpgBoardPos(x, y)
                anchor (.5, .5)

    for u in forcesList:
        imagebutton:
            idle u.idleImage

            if u.isFriendly():
                if setFriend:
                    action SetVariable("selectedFriend", u)
                else:
                    action NullAction()
            else:
                action SetVariable("selectedFoe", u)

            pos u.getPos()
            anchor (.5, .5)

            at srpgUnitTransform

    if selectedFriend is not None:
        vbox:
            pos (0, 0)
            anchor (0, 0)

            add selectedFriend.idleImage xalign .5 zoom .75
            text selectedFriend.name xalign .5
            text "%d, %d" % (selectedFriend.curx, selectedFriend.cury) xalign .5

    if selectedFoe is not None:
        vbox:
            pos (1., 0)
            anchor (1., 0)

            add selectedFoe.idleImage xalign .5 zoom .75
            text selectedFoe.name xalign .5
            text "%d, %d" % (selectedFoe.curx, selectedFoe.cury) xalign .5

    transclude

screen srpgSelectUnit():
    use srpgBasic(setFriend = True):
        if selectedFriend is not None:
            textbutton "이동":
                pos selectedFriend.getPos()
                anchor (1., .0)
                offset (-100, -15)
                action [SetVariable("moveState", True), Return()]


screen srpgSelectDestination(movableCoordinates):
    use srpgBasic():
        for x in range(0, 7):
            for y in range(0, 5):
                if movableCoordinates[x][y]:
                    imagebutton:
                        idle Solid("#00F")
                        hover Solid("#88F")
                        xysize (198, 198)
                        pos srpgBoardPos(x, y)
                        anchor (.5, .5)
                        action [Function(selectedFriend.moveto, x=x, y=y), Return()]


transform srpgUnitTransform:
    on idle:
        linear .25 zoom 1.
    on hover:
        linear .25 zoom 1.2
    on selected_idle:
        linear .05 zoom 1.25
    on selected_hover:
        linear .05 zoom 1.3
