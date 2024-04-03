import click

# @click.option

# import ctypes
# from ctypes import wintypes
# import time
# import pygetwindow as pyg
# # time.sleep(7)

# # Load necessary Windows API functions
# user32 = ctypes.windll.User32

# # Define the required types
# BOOL = wintypes.BOOL

# # Define the function prototypes

# def is_screen_locked():
#     active_window = pyg.getActiveWindow()
#     SystemParametersInfoW = user32.SystemParametersInfoW
#     SystemParametersInfoW.argtypes = [wintypes.UINT, wintypes.UINT, ctypes.POINTER(wintypes.BOOL), wintypes.UINT]
#     SystemParametersInfoW.restype = BOOL

#     # Constants for SystemParametersInfoW function
#     SPI_GETSCREENSAVERRUNNING = 17
#     screensaver_running = wintypes.BOOL()
#     # Call SystemParametersInfoW to check if the screensaver is running
#     result = SystemParametersInfoW(SPI_GETSCREENSAVERRUNNING, 0, ctypes.byref(screensaver_running), 0)
#     print(result)
#     print(active_window)
#     if result==0 or active_window==None:
#         #  retrieve screensaver status
#         return True
#     return False

# # Example usage
# i=0
# while True:
#     time.sleep(2)
#     if is_screen_locked():
#         print(f"{i}  "+"Screen is locked")
#     else:
#         print(f"{i}  "+"Screen is unlocked")
    
#     i+=1
#     print()

'''===================================================================================================='''

import ctypes
from ctypes import wintypes
import time
import pygetwindow as pyg
from urllib.parse import urlparse

def is_screen_locked():
    try:
        active_window = pyg.getActiveWindow()
    except pyg.PyGetWindowException:
        active_window = None

    user32 = ctypes.windll.User32
    SystemParametersInfoW = user32.SystemParametersInfoW
    SystemParametersInfoW.argtypes = [wintypes.UINT, wintypes.UINT, ctypes.POINTER(wintypes.BOOL), wintypes.UINT]
    SystemParametersInfoW.restype = wintypes.BOOL
    SPI_GETSCREENSAVERRUNNING = 0x0072

    tetet=ctypes.windll.user32.GetSystemMetrics(16)
    

    screensaver_running = wintypes.BOOL()

    result = SystemParametersInfoW(SPI_GETSCREENSAVERRUNNING, 0, ctypes.byref(screensaver_running), 0)
    
    print(result,"    ", active_window, "    ",tetet)

    return result == 0 or active_window ==None

# Example usage
i = 0
while True:
    time.sleep(2)
    if is_screen_locked():
        print(f"{i}  Screen is locked")
    else:
        print(f"{i}  Screen is unlocked")
    i += 1
    print()
