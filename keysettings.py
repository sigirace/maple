import pyautogui
import time
import random


class Macro():

    def __init__(self):
        self.sleep = 0.4

    def basic(self, key):
        time.sleep(self.sleep)    
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)  

    def jump_attack(self):
        time.sleep(self.sleep)    
        pyautogui.keyDown("w")
        pyautogui.keyDown("q")
        pyautogui.keyUp("w")
        pyautogui.keyUp("q")

    def duration_key(self, key, duration):
        # time.sleep(self.sleep)
        pyautogui.keyDown(key)
        time.sleep(duration)
        pyautogui.keyUp(key)        
        time.sleep(self.sleep)


    def super_left_jump(self):
        time.sleep(self.sleep)
        pyautogui.keyDown('right')
        pyautogui.keyDown('w')
        pyautogui.keyUp('right')
        pyautogui.keyDown('left')
        pyautogui.keyDown('q')
        pyautogui.keyUp('w')
        pyautogui.keyUp('left')
        pyautogui.keyUp('q')

    def super_right_jump(self):
        time.sleep(self.sleep)
        pyautogui.keyDown('left')
        pyautogui.keyDown('w')
        pyautogui.keyUp('left')
        pyautogui.keyDown('right')
        pyautogui.keyDown('q')
        pyautogui.keyUp('w')
        pyautogui.keyUp('right')
        pyautogui.keyUp('q')

    def super_left_2_jump(self):
        time.sleep(self.sleep)
        pyautogui.keyDown('right')
        pyautogui.keyDown('w')
        pyautogui.keyUp('right')
        pyautogui.keyDown('q')
        pyautogui.keyUp('w')
        pyautogui.keyUp('q')
        pyautogui.keyDown('left')
        pyautogui.keyDown('w')
        pyautogui.keyUp('left')
        pyautogui.keyUp('w')

    def super_right_2_jump(self):
        time.sleep(self.sleep)
        pyautogui.keyDown('left')
        pyautogui.keyDown('w')
        pyautogui.keyUp('left')
        pyautogui.keyDown('q')
        pyautogui.keyUp('w')
        pyautogui.keyUp('q')

    def random_attack(self):
        attack_num = random.randint(0, 1)
        if attack_num == 0:
            self.basic('q')
        else:
            self.jump_attack()

    def random_jump_attack(self):
        attack_num = random.randint(0, 1)
        if attack_num == 0:
            self.super_left_jump()
            self.super_right_jump()
        else:
            self.super_left_2_jump()
            self.super_right_2_jump ()
        
    def time_attack(self):
        time.sleep(self.sleep) 
        pyautogui.keyDown('q')
        time.sleep(30)
        pyautogui.keyUp('q')

    def moving_attack(self):
        time.sleep(self.sleep) 
        pyautogui.keyDown('right')
        pyautogui.keyDown('q')
        pyautogui.keyUp('right')
        time.sleep(0.7) 
        pyautogui.keyUp('q')
        time.sleep(self.sleep) 
        pyautogui.keyDown('left')
        pyautogui.keyUp('left')        

    def left_many_macro(self):
        self.time_attack()
        self.moving_attack()

    def youtube_macro(self):
        for i in range(30):
            time.sleep(self.sleep) 
            pyautogui.keyDown('right')
            pyautogui.keyDown('q')
            time.sleep(self.sleep) 
            pyautogui.keyUp('right')
            pyautogui.keyUp('q')
            time.sleep(self.sleep) 
            pyautogui.keyDown('left')
            pyautogui.keyDown('q')
            time.sleep(self.sleep) 
            pyautogui.keyUp('left')
            pyautogui.keyUp('q')
    
    def jump_macro(self):
        self.sleep = 0.45
        self.super_left_jump()
        self.basic('q')
        self.super_right_jump()
        self.basic('q')
        self.super_left_2_jump()
        self.basic('q')
        self.super_right_2_jump()
        self.basic('q')
        
    def jump_macro2(self):
        self.sleep = 0.45
        self.super_left_2_jump()
        self.random_attack()
        self.super_right_jump()
        self.random_attack()
        self.super_left_jump()
        self.random_attack()
        self.super_right_2_jump()
        self.random_attack()
            
## left 