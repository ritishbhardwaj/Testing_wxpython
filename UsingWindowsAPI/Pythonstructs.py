'''Creating C Structures in Python'''



from ctypes import wintypes
from ctypes import windll
import ctypes


'''Defining Structure in Python'''
class MEMORYSTATUSEX(ctypes.Structure):
    _fields_=[
        ('dwlength',wintypes.DWORD),
        ('dwMemoryLoad',ctypes.c_ulonglong),
        ('ullTotalPhys', ctypes.c_ulonglong),
        ('ullAvailPhys', ctypes.c_ulonglong), 
        ('ullTotalPageFile', ctypes.c_ulonglong), 
        ('ullAvailPageFile', ctypes.c_ulonglong), 
        ('ullTotalVirtual', ctypes.c_ulonglong), 
        ('ullAvailVirtual', ctypes.c_ulonglong),
        ('ullAvailExtendedVirtual', ctypes.c_ulonglong),
    ]
    def __init__(self):
        self.dwlength=ctypes.sizeof(self)
        super(MEMORYSTATUSEX, self).__init__()


kernel32 = windll.kernel32

GlobalMemoryStatusEx = kernel32.GlobalMemoryStatusEx               # Creaating the function out of the kernel32
GlobalMemoryStatusEx.argtypes = [ctypes.POINTER(MEMORYSTATUSEX)]
GlobalMemoryStatusEx.restype=wintypes.BOOL



statex = MEMORYSTATUSEX()
GlobalMemoryStatusEx(ctypes.byref(statex))

print(f'[*] physical memory: {round(statex.dwMemoryLoad)}GB')