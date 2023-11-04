default forcesList = [srpgSkeleton(0, 2)]

screen srpgBasic():
    for x in range(0, 7):
        for y in range(0, 5):
            add Solid("#888"):
                xysize (198, 198)
                pos srpgBoardPos(x, y)
                anchor (.5, .5)

    for u in forcesList:
        add u.idleImage:
            pos u.getPos()
            anchor (.5, .5)

