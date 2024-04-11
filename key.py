import keyboard
import time

def basic():
    # 방향키 왼쪽을 누름
    keyboard.press_and_release('left')
    # 약간의 지연
    time.sleep(0.75)
    # 'q'를 누름
    keyboard.press_and_release('q')
    # 약간의 지연
    time.sleep(0.75)
    
    # 방향키 오른쪽을 누름
    keyboard.press_and_release('right')
    # 약간의 지연
    time.sleep(0.75)
    # 'q'를 누름
    keyboard.press_and_release('q')
    # 약간의 지연
    time.sleep(0.75)

def two():
    # 방향키 왼쪽을 누름
    keyboard.press_and_release('left')
    time.sleep(0.75)
    keyboard.press_and_release('left')
    time.sleep(0.75)
    keyboard.press_and_release('q')
    time.sleep(0.75)
    keyboard.press_and_release('q')
    time.sleep(0.75)
    keyboard.press_and_release('right')
    time.sleep(0.75)
    keyboard.press_and_release('right')
    time.sleep(0.75)
    keyboard.press_and_release('q')
    time.sleep(0.75)
    keyboard.press_and_release('q')
    time.sleep(0.75)
    


try:
    while True:
        two()

# Ctrl+C를 누르면 루프에서 빠져나옴
except KeyboardInterrupt:
    print("Program exited")
