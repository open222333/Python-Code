import pyautogui


def keep_press():
    pyautogui.press('caps_lock')


flag = input("Q")

# while True:
#     x = input("輸入Q或q離開:")
#     print(pyautogui.position())
#     if x == 'q' or x == 'Q':
#         break
#     else:
#         pyautogui.press('caps_lock')
