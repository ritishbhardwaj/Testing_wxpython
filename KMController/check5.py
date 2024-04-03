# import time
# import psutil

# def is_screen_locked():
#     for session in psutil.win_service_iter():
#         if session.status() == 'stopped' and 'LogonUI.exe' in session.name():
#             return True
#     return False

# # Example usage

# while True:
#     time.sleep(5)
#     if is_screen_locked():
#         print("Screen is locked")
#     else:
#         print("Screen is unlocked")

'''======================================================'''
# from win32gui import GetWindowText, GetForegroundWindow
# import time
# # time.sleep(5)
# # lock the system or open the application for a check
# i=0
# while True:
#     time.sleep(2)
#     if "Lock" in GetWindowText(GetForegroundWindow()):
#         print(f"No.{i}  : Lock Screen")
#     else:
#         print(f"No.{i}  : Unlocked Screen")
#     i+=1


'''======================================================'''

# import time
# import pygetwindow as gw

# def is_screen_locked():
#     active_window = gw.getActiveWindow()
#     print(active_window)
#     return active_window is None or active_window.title == 'Program Manager' or active_window.title=="Windows Default Lock Screen"

# i=0
# while True:
#     time.sleep(1)
#     if is_screen_locked():
#         print(f"{i}   : Screen is locked")
#     else:
#         print(f"{i}   :Screen is unlocked")
#     i+=1


'''=========================================================================='''

# import ctypes 
# import time
# import pygetwindow as gw
# while (1):
#     w=ctypes.windll.user32.GetForegroundWindow()
#     print(w)
#     active_window = gw.getActiveWindow()
#     print("<<**",active_window)
#     time.sleep(2)

'''================================================================================'''

# import time
# import ctypes

# user32 = ctypes.windll.User32
# OpenDesktop = user32.OpenDesktopA
# SwitchDesktop = user32.SwitchDesktop
# DESKTOP_SWITCHDESKTOP = 0x0100

# while 1:
#   hDesktop = OpenDesktop ("default", 0, False, DESKTOP_SWITCHDESKTOP)
#   result = SwitchDesktop (hDesktop)
#   if result:
#     print ("Unlocked")
#     time.sleep (1.0)
#   else:
#     print (time.asctime (), "still locked")
#     time.sleep (2)


'''=================================================================================='''
import time
import ctypes

user32 = ctypes.windll.User32
OpenDesktop = user32.OpenDesktopA
SwitchDesktop = user32.SwitchDesktop
CloseDesktop = user32.CloseDesktop
DESKTOP_SWITCHDESKTOP = 0x0100

while True:
    hDesktop = OpenDesktop("default", 0, False, DESKTOP_SWITCHDESKTOP)
    print(hDesktop)
    if hDesktop:
        result = SwitchDesktop(hDesktop)
        CloseDesktop(hDesktop)
        
        if result:
            print("Unlocked")
        else:
            print(time.asctime(), "still locked")
    else:
        print("Error opening desktop")
    
    time.sleep(1.0)