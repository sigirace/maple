import random
import keysettings as ks
import pyautogui
import time


mc = ks.Macro()

# 좌 2번 우 2번
def basic_pattern():
    mc.multi_attack(num=2)
    mc.basic("right")
    mc.multi_attack(num=2)
    mc.basic("left")

# 좌 여러번 우 2번
def pattern1():
    left_num = random.randrange(6, 12, 2)
    mc.multi_attack(num=left_num)
    mc.basic("right")
    right_num = random.randrange(2, 6, 2)
    mc.multi_attack(num=right_num)
    mc.basic("left")

# 좌 점샷 점샷 우 1번
def pattern2():
    left_num = random.randrange(4, 8, 2)
    mc.jump_attack(num=left_num)
    mc.basic("right")
    right_num = random.randrange(2, 6, 2)
    mc.multi_attack(num=right_num)
    mc.basic("left")

# 좌 여러번 우 점샷 1번

def pattern3():
    num1 = random.randrange(2, 4, 2)
    num2 = random.randrange(0, 1, 1)
    mc.youtube_random(num1, num2)
    mc.basic("right")
    mc.youtube_random(0, 1)
    mc.basic("left")

# 좌 점샷 1번 우 점샷 점샷




try:
    counter = 0

    while True:
        counter +=1
        mc.left_many_macro()
        # mc.jump_macro2()
        # mc.real_macro()
        if counter == 100:
            pyautogui.keyDown('a')
            pyautogui.keyUp('a')
            counter=0
        
    # while True:
    #     counter +=1
    #     mc.lecture_random()
    #     if counter == 100:
    #         pyautogui.keyDown('a')
    #         pyautogui.keyUp('a')
    #         counter=0


# Ctrl+C를 누르면 루프에서 빠져나옴
except KeyboardInterrupt:
    print("Program exited")

