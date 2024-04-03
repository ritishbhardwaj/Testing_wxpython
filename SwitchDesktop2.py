from ctypes import wintypes
import ctypes
from ctypes import WINFUNCTYPE
import win32api
import pygetwindow as pyg

user32 = ctypes.windll.user32

def switchDesktop():

    SwitchDesktop = user32.SwitchDesktop
    SwitchDesktop.argtypes =[wintypes.HDESK]
    SwitchDesktop.restype = wintypes.BOOL
    activewindow = pyg.getActiveWindow()

    hDesktop=openDsktopA()
    print(hDesktop,"<--------------hDsktop")
    print(activewindow,"--------------> active Window")

    call = SwitchDesktop(hDesktop)

    print(call)

def openDsktopA():
    OpenDesktopA = ctypes.windll.user32.OpenDesktopA
    OpenDesktopA.argtypes = [wintypes.LPCSTR, wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    OpenDesktopA.restype = wintypes.HDESK

    DESKTOP_SWITCHDESKTOP = 0x0100
    desktop_name = "default"
    desktop_name_pointer = ctypes.c_char_p(desktop_name.encode("utf-8"))

    res= OpenDesktopA(desktop_name_pointer,0,False,DESKTOP_SWITCHDESKTOP)
    return res

if __name__=="__main__":
    import time
    while True:
        time.sleep(2)
        switchDesktop()
        print()