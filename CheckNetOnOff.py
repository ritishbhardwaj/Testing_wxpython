import ctypes
import math

prototype =  ctypes.windll.wininet.InternetGetConnectedState
prototype.argtypes=[ctypes.POINTER(ctypes.c_ulong), ctypes.c_ulong]

def function():
    flags =  ctypes.c_ulong(0)
    connected = prototype(ctypes.byref(flags),0)
    return flags.value

if __name__ == "__main__":
    import time
    stat = time.time()
    res= function()
    end =  time.time()
    print(end-stat)
    print(hex(res))
    if res:
        print("Yea")
    else:
        print("NOooo")

'''============================================================================================================'''

# import ctypes

# def is_internet_connected():
#     # Load the WinINet library
#     wininet = ctypes.WinDLL('wininet.dll')
    
#     # Define the InternetCheckConnection function prototype
#     InternetCheckConnection = wininet.InternetCheckConnectionW
#     InternetCheckConnection.argtypes = [ctypes.c_wchar_p, ctypes.c_int, ctypes.c_int]
#     InternetCheckConnection.restype = ctypes.c_bool
    
#     # Check internet connection by trying to connect to a well-known server (e.g., www.google.com)
#     result = InternetCheckConnection("http://www.google.com", 1, 0)
    
#     return result
# if __name__ =="__main__":
#     import time
#     stat= time.time()
#     res = is_internet_connected()
#     end= time.time()
#     if res:
#         print("Connected to the internet")
#     else:
#         print("Not connected to the internet")
    
#     print(str(end-stat))

'''====================================================================================================='''

# import ctypes
# import socket

# def is_internet_connected():
#     try:
#         # Create a socket to check network adapter status
#         socket.setdefaulttimeout(1)
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
#         # Try to connect to a well-known server (e.g., Google's DNS server)
#         s.connect(("8.8.8.8", 53))
#         s.close()
        
#         return True
#     except:
#         return False

# if __name__ =="__main__":
    # import time
    # stat= time.time()
    # res = is_internet_connected()
    # end= time.time()
    # if res:
    #     print("Connected to the internet")
    # else:
    #     print("Not connected to the internet")
    
    # print(str(end-stat))


import requests

def is_connected():
    try:
        # Send a lightweight HTTP GET request to a well-known website
        response = requests.get("http://www.google.com",timeout=0.04)
        # Check if the response status code indicates success (2xx)
        return response.status_code == requests.codes.ok
    except requests.RequestException:
        return False

stat = time.time()
res  = is_connected()
end = time.time()
if res:
    print("Connected to the internet")
else:
    print("Not connected to the internet")

print(end -stat)