import ctypes
from ctypes import wintypes
from ctypes import WINFUNCTYPE

user32 = ctypes.windll.user32

def switchingDesktop():
    
    prototype = WINFUNCTYPE(wintypes.BOOL , wintypes.HDESK)
    paramflags = ((1,'hDesktop'),)
    c_SwitchDesktop= prototype(('SwitchDesktop', user32),paramflags)

    hDesktop = openDesktopA()

    res = c_SwitchDesktop(hDesktop)

    print(res)



def openDesktopA():
    DESKTOP_SWITCHDESKTOP = 0x0100
    desktop_name = u"default"
    desktop_name_pointer = ctypes.c_char_p(desktop_name.encode("utf-8"))
    prototype= WINFUNCTYPE(wintypes.HDESK , wintypes.LPCSTR , wintypes.DWORD,wintypes.BOOL, wintypes.DWORD)
    paramflags = ((1,"lpszDesktop"), (2,"dwFlags"),(3,"fInherit"),(4, "dwDesiredAccess"),)
    c_OpenDesktopA = prototype(('OpenDesktopA', user32),paramflags)
    dwFlag= wintypes.DWORD(0)
    res=c_OpenDesktopA(desktop_name_pointer,ctypes.byref(dwFlag), False, DESKTOP_SWITCHDESKTOP)

    return res


if __name__ == '__main__':
    switchingDesktop()