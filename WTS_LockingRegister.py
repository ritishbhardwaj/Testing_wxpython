import ctypes
from ctypes import wintypes

def register(handle: wintypes.HWND) -> bool:
    SYNCHRONIZE = 0x00100000
    NOTIFY_FOR_THIS_SESSION = 0
    RPC_S_INVALID_BINDING = 1702

    eventObjectHandle = ctypes.windll.kernel32.OpenEventW(SYNCHRONIZE, False, "Global\\TermSrvReadyEvent")
    
    if not eventObjectHandle:
        return False

    registrationSuccess = ctypes.windll.wtsapi32.WTSRegisterSessionNotification(handle, NOTIFY_FOR_THIS_SESSION)
    ctypes.windll.kernel32.CloseHandle(eventObjectHandle)

    if registrationSuccess:
        return True
    else:
        error = ctypes.WinError()
        if error.errno == RPC_S_INVALID_BINDING:
            return False
        else:
            return False

def unregister(handle: wintypes.HWND) -> None:
    if not ctypes.windll.wtsapi32.WTSUnRegisterSessionNotification(handle):
        pass


if __name__ =="__main__":
    import pygetwindow
    awindow = pygetwindow.getActiveWindow()
    hwnd = awindow._hWnd
    print(register(hwnd))
    print(unregister(hwnd))