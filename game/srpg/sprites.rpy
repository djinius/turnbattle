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

################################################################################
#
# 이 프로젝트에서 사용한 스프라이트의 저작권은 Robert Pinero에게 있습니다.
# 스프라이트를 다른 프로젝트에 사용할 경우 원작자인 Robert Pinero를 크레딧에 명시해야 합니다.
# Sprites from https://robertpinero.itch.io/free-animated-enemy-sprites
#
################################################################################

image skeletonSpriteSheet = "images/sprites/skeleton.png"

image skeleton idleOriginal:
    Crop((350 * 0, 210 * 0, 350, 210), "skeletonSpriteSheet")
    pause .25
    Crop((350 * 1, 210 * 0, 350, 210), "skeletonSpriteSheet")
    pause .25
    Crop((350 * 2, 210 * 0, 350, 210), "skeletonSpriteSheet")
    pause .25
    Crop((350 * 1, 210 * 0, 350, 210), "skeletonSpriteSheet")
    pause .25
    repeat

image skeleton idle:
    Transform("skeleton idleOriginal", xzoom=-1)

image skeleton walk:
    Crop((350 * 6, 210 * 0, 350, 210), "skeletonSpriteSheet")
    pause .25
    Crop((350 * 7, 210 * 0, 350, 210), "skeletonSpriteSheet")
    pause .25
    Crop((350 * 8, 210 * 0, 350, 210), "skeletonSpriteSheet")
    pause .25
    Crop((350 * 7, 210 * 0, 350, 210), "skeletonSpriteSheet")
    pause .25
    repeat

image skeleton attackOriginal:
    Crop((350 * 3, 210 * 0, 350, 210), "skeletonSpriteSheet")
    pause .25
    Crop((350 * 4, 210 * 0, 350, 210), "skeletonSpriteSheet")
    pause .25
    Crop((350 * 5, 210 * 0, 350, 210), "skeletonSpriteSheet")

image skeleton attack:
    Transform("skeleton attackOriginal", xzoom=-1)

