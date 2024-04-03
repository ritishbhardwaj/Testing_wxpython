'''   NOT USEFUL LIKE IN CASE I HAVE NOT LOGIN TO SOPHOS AND IT SHOWS THAT I AM CONNECTED'''

import ctypes
from ctypes import wintypes

user = ctypes.windll.sensapi

prototype = user.IsNetworkAlive
prototype.argtypes = [ctypes.POINTER(wintypes.DWORD)]
# prototype.restype =wintypes.BOOL

def fun():

    flag = ctypes.c_ulong()
    ans= prototype(ctypes.byref(flag))

    print(ans)

fun()