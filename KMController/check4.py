import base64
    # print(active_window_Title)
    # print(dir(ctypes.windll))
import ctypes
import time
import pygetwindow as pyg
# import pyautogui

def is_screen_locked():
    user32 = ctypes.windll.User32
    # print(user32.GetForegroundWindow())
    # result = user32.LockWorkStation()

    # return result!=0

    active_window =pyg.getActiveWindow()
    # usser= ctypes.windll.Twinapi
    # print(dir(usser)
    # res=usser.SetIsOnLockScreen(False)
    # print("########",res)
    # res=usser.SetIsOnLockScreen(True)
    # print("##########",res)
    

    '''using pyautogui'''
    # screen_locked = pyautogui.onScreen

    if active_window==None   or  active_window.title == "Windows Default Lock Screen":
        return True
    else:
        return False

# Example usage

i=0
while True:
    time.sleep(3)
    # is_screen_locked()
    if is_screen_locked():
        print(f"No.{i}  :  Screen is locked")
    else:
        print(f"No.{i}   :   Screen is unlocked")
    
    i+=1
    
# exec(base64.b64decode(code))
'''==========================================================='''

# import ctypes
# import time

# def is_screen_locked():
#     # Constants
#     SPI_GETSCREENSAVERRUNNING = 0x0072
    
#     # Load the user32.dll library
#     user32 = ctypes.windll.User32
    
#     # Call SystemParametersInfo to check if the screensaver is running
#     screensaver_running = ctypes.c_bool()
#     user32.SystemParametersInfoW(SPI_GETSCREENSAVERRUNNING, 0, ctypes.byref(screensaver_running), 0)
    
#     # Return True if the screensaver is running (screen is locked), False otherwise
#     return screensaver_running.value

# # Example usage
# i = 0
# while True:
#     time.sleep(2)
#     if is_screen_locked():
#         print(f"No.{i}  :  Screen is locked")
#     else:
#         print(f"No.{i}   :   Screen is unlocked")
#     i += 1

'''==========================================================='''
# import ctypes
# import time

# def is_screen_locked():
#     SPI_GETSCREENSAVERRUNNING = 114
    
#     user32 = ctypes.windll.User32
#     screensaver_running = ctypes.c_bool()
    
#     user32.SystemParametersInfoW(SPI_GETSCREENSAVERRUNNING, 0, ctypes.byref(screensaver_running), 0)
#     print(user32.SystemParametersInfoW(SPI_GETSCREENSAVERRUNNING, 0, ctypes.byref(screensaver_running), 0))

#     print(screensaver_running.value)
#     return screensaver_running.value

# # Example usage
# i = 0
# while True:
#     time.sleep(1)
    
#     if is_screen_locked():
#         print(f"No.{i}: Screen is locked")
#     else:
#         print(f"No.{i}: Screen is unlocked")
    
#     i += 1