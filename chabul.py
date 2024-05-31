from keysettings import Macro
import pyautogui
import keyboard
import time

attack_key = False
left_key = False
right_key = False
macro = Macro()

def toggle_attack_key(e):
    global attack_key
    global left_key
    global right_key

    left_key = False
    right_key = False

    attack_key = not attack_key

def toggle_left_key(e):
    global attack_key
    global left_key
    global right_key
    
    attack_key = False
    right_key = False
    pyautogui.keyUp('right')

    if left_key:
        pyautogui.keyUp('left')
    else:
        pyautogui.keyDown('left')
    left_key = not left_key

def toggle_right_key(e):    
    global attack_key
    global left_key
    global right_key

    attack_key = False
    left_key = False
    pyautogui.keyUp('left')

    if right_key:
        pyautogui.keyUp('right')
    else:
        pyautogui.keyDown('right')
    right_key = not right_key

def toggle_buff_key(e):
    macro.buff()

def main():
    keyboard.on_press_key('1', toggle_attack_key)
    keyboard.on_press_key('2', toggle_left_key)
    keyboard.on_press_key('3', toggle_right_key)
    keyboard.on_press_key('`', toggle_buff_key)
    

    while True:
        if attack_key:
            macro.jump_attack()
        if left_key:
            macro.jump_attack()
        if right_key:
            macro.jump_attack()
        
if __name__ == "__main__":
    main()