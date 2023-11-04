# Sprites from https://robertpinero.itch.io/free-animated-enemy-sprites

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

