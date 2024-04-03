# import ctypes
# from ctypes import wintypes
# import time
# import pygetwindow as pyg

# def is_screen_locked():
#     try:
#         active_window = pyg.getActiveWindow()
#     except pyg.PyGetWindowException:
#         active_window = None

#     user32 = ctypes.windll.User32
#     SystemParametersInfoW = user32.SystemParametersInfoW
#     SystemParametersInfoW.argtypes = [wintypes.UINT, wintypes.UINT,ctypes.POINTER(wintypes.BOOL), wintypes.UINT]
#     SystemParametersInfoW.restype = wintypes.BOOL
#     SPI_GETSCREENSAVEACTIVE = 0x0010

#     screensaver_running = ctypes.c_int()
#     # screensaver_running= ctypes.c_bool()
#     # screensaver_running=ctypes.c_void_p()
#     screen_saver_enabled = wintypes.BOOL()
#     # screen_saver_enabled = ctypes.c_bool()
#     # ptr1 =ctypes.pointer(screensaver_running)
#     ptr2 = ctypes.pointer(screen_saver_enabled)
    
#     # print(ptr1)
#     print(ptr2.contents.value)

#     SystemParametersInfoW(SPI_GETSCREENSAVEACTIVE, 0,  ctypes.byref(screen_saver_enabled), 0)
    
#     print(active_window,"  ",screen_saver_enabled)

#     return active_window==None

# # Example usage
# i = 0
# while True:
#     time.sleep(2)
#     if is_screen_locked():
#         print(f"{i}  Screen is locked")
#     else:
#         print(f"{i}  Screen is unlocked")
#     i += 1
#     print()


'''========================================================================================================================================'''

import ctypes
from ctypes import wintypes
import time
import pygetwindow as pyg

def is_screen_locked():
    try:
        active_window = pyg.getActiveWindow()
    except pyg.PyGetWindowException:
        active_window = None

    user32 = ctypes.windll.User32
    SystemParametersInfoW = user32.SystemParametersInfoW
    SystemParametersInfoW.argtypes = [wintypes.UINT, wintypes.UINT, ctypes.POINTER(wintypes.BOOL), wintypes.UINT]
    SystemParametersInfoW.restype = wintypes.BOOL
    SPI_GETSCREENSAVEACTIVE = 0x0010

    screen_saver_enabled = wintypes.BOOL()
    
    SystemParametersInfoW(SPI_GETSCREENSAVEACTIVE, 0, ctypes.byref(screen_saver_enabled), 0)
    
    print(active_window, "  Screen saver enabled:", bool(screen_saver_enabled))

    return active_window == None

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