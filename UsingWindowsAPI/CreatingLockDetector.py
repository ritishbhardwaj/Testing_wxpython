# import ctypes
# from ctypes import windll,wintypes

# user32= windll.user32
'''======================================================================================'''
# import ctypes

# def is_screen_locked():
#     Lib_LockStat = ctypes.windll.LoadLibrary("user32.dll")
#     Func_OpenInputDesktop = ctypes.windll.kernel32.GetProcAddress(Lib_LockStat, b"OpenInputDesktop")
    
#     dwFlags = 0
#     fInherit = False
#     dwDesiredAccess = 0x100
#     lockstat = ctypes.c_int()
    
#     hDesktopAccess = ctypes.windll.kernel32.CallFunctionFast(Func_OpenInputDesktop, dwFlags, fInherit, dwDesiredAccess, ctypes.byref(lockstat))
    
#     ctypes.windll.kernel32.FreeLibrary(Lib_LockStat)

#     return lockstat.value < 1

# # Example usage
# print("Screen is locked:", is_screen_locked())
'''============================================================================================='''
# import ctypes

# def is_locked():
#     # Load necessary Windows API functions
#     kernel32 = ctypes.WinDLL("kernel32")
#     WTSapi32 = ctypes.WinDLL("Wtsapi32")
    
#     # Define required types
#     DWORD = ctypes.c_ulong
#     LPDWORD = ctypes.POINTER(DWORD)
    
#     # Get the address of the ProcessIdToSessionId function
#     ProcessIdToSessionId = kernel32.GetProcAddress(kernel32.GetModuleHandleW("kernel32"), b"ProcessIdToSessionId")
    
#     # Declare the arguments and return types for the ProcessIdToSessionId function
#     ProcessIdToSessionIdPrototype = ctypes.WINFUNCTYPE(ctypes.c_bool, DWORD, LPDWORD)
#     ProcessIdToSessionIdParams = (1, "dwProcessId"), (2, "pSessionId")
#     ProcessIdToSessionIdFunction = ProcessIdToSessionIdPrototype(ProcessIdToSessionId, ProcessIdToSessionIdParams)
    
#     # Get the current process ID
#     dwProcessId = kernel32.GetCurrentProcessId()
    
#     # Call the ProcessIdToSessionId function to get the session ID
#     pSessionId = DWORD()
#     if not ProcessIdToSessionIdFunction(dwProcessId, ctypes.byref(pSessionId)):
#         return False
    
#     # Get the address of the WTSQuerySessionInformation function
#     WTSQuerySessionInformation = WTSapi32.GetProcAddress(WTSapi32, b"WTSQuerySessionInformationW")
    
#     # Declare the arguments and return types for the WTSQuerySessionInformation function
#     WTSQuerySessionInformationPrototype = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, DWORD, ctypes.c_void_p, LPDWORD)
#     WTSQuerySessionInformationParams = (1, "hServer"), (2, "SessionId"), (3, "WTSInfoClass"), (4, "ppBuffer"), (5, "pBytesReturned")
#     WTSQuerySessionInformationFunction = WTSQuerySessionInformationPrototype(WTSQuerySessionInformation, WTSQuerySessionInformationParams)
    
#     # Define constants
#     WTS_CURRENT_SERVER_HANDLE = 0
#     WTS_INFO_CLASS = 25
    
#     # Call the WTSQuerySessionInformation function to query session information
#     ppBuffer = ctypes.c_void_p()
#     pBytesReturned = DWORD()
#     if not WTSQuerySessionInformationFunction(WTS_CURRENT_SERVER_HANDLE, pSessionId, WTS_INFO_CLASS, ctypes.byref(ppBuffer), ctypes.byref(pBytesReturned)):
#         return False
    
#     # Extract the bytes from the returned buffer
#     bytes_value = ctypes.cast(ppBuffer, LPDWORD)[0]
    
#     # Free the memory allocated by WTSQuerySessionInformation
#     WTSapi32.WTSFreeMemory(ppBuffer)
    
#     # Determine if the system is locked based on the returned value
#     if bytes_value is not None:
#         if ctypes.windll.version.OSVersion() == 2:  # Windows 7 or Windows Server 2008 R2
#             return bytes_value
#         else:
#             return bytes_value == 0
#     else:
#         # Fallback method for older versions of Windows
#         hDesktop = kernel32.OpenDesktopW("Default", 0, False, 0x0010)  # DESKTOP_SWITCHDESKTOP
#         if hDesktop:
#             result = kernel32.SwitchDesktop(hDesktop)
#             kernel32.CloseDesktop(hDesktop)
#             return result is None
#         else:
#             return False

# # Example usage
# print("Screen is locked:", is_locked())
'''==================================================================================='''
import time
time.sleep(5)
import ctypes
from ctypes import windll
from ctypes import wintypes
from pygetwindow import getActiveWindow

LDWORD = ctypes.c_ulonglong

user32 = windll.Wtsapi32
window = getActiveWindow()
Hwnd = window._hWnd

# WTSSESSION_NOTIFICATION = ctypes.WINFUNCTYPE(None, a= wintypes.HANDLE, b= wintypes.DWORD)

# def session_notification_callback(session, event):
#     print(f"Session ID: {session}, Event: {event}")
#     return session

WTSRegisterSessionNotification = user32.WTSRegisterSessionNotification
WTSRegisterSessionNotification.argtypes = [wintypes.HANDLE, wintypes.DWORD]
WTSRegisterSessionNotification.restype = wintypes.BOOL

# callback = WTSSESSION_NOTIFICATION(a=Hwnd,b=1)

res = WTSRegisterSessionNotification(Hwnd, 1)

print(res)
