import ctypes
from ctypes import POINTER, byref, c_ulong
from comtypes import CoInitialize, CoUninitialize
from comtypes import GUID
from comtypes.client import CreateObject
import win32com
from comtypes.gen.Netlistmgr import INetworkListManager

# Define GUID for INetworkListManager interface
NLM_GUID = GUID('{DCB00000-570F-4A9B-8D69-199FDBA5723B}')

# Define NLM_CONNECTIVITY constants
NLM_CONNECTIVITY_DISCONNECTED = 0
NLM_CONNECTIVITY_IPV4_NOTRAFFIC = 0x1
NLM_CONNECTIVITY_IPV6_NOTRAFFIC = 0x2
NLM_CONNECTIVITY_IPV4_SUBNET = 0x10
NLM_CONNECTIVITY_IPV4_LOCALNETWORK = 0x20
NLM_CONNECTIVITY_IPV4_INTERNET = 0x40
NLM_CONNECTIVITY_IPV6_SUBNET = 0x100
NLM_CONNECTIVITY_IPV6_LOCALNETWORK = 0x200
NLM_CONNECTIVITY_IPV6_INTERNET = 0x400


def IsConnected():
    CoInitialize(None)
    try:
        # Create an instance of INetworkListManager
        pNLM = CreateObject(NLM_GUID, interface=INetworkListManager)
        con = c_ulong()
        hr = pNLM.GetConnectivity(byref(con))
        if hr == 0:  # Check if the HRESULT is S_OK (success)
            if con.value & NLM_CONNECTIVITY_IPV4_INTERNET:
                return True
            elif con.value & NLM_CONNECTIVITY_IPV6_INTERNET:
                return True
            else:
                return False
        else:
            print("GetConnectivity failed with HRESULT:", hex(hr))
            return False
    except Exception as e:
        print("Error:", e)
        return False
    finally:
        CoUninitialize()

if __name__ == "__main__":
    if IsConnected():
        print("Internet is connected.")
    else:
        print("Internet is not connected.")


# class NLM_CONNECTIVITY(wintypes.DWORD):
#     NLM_CONNECTIVITY_DISCONNECTED = 0
#     NLM_CONNECTIVITY_IPV4_NOTRAFFIC = 0x1
#     NLM_CONNECTIVITY_IPV6_NOTRAFFIC = 0x2
#     NLM_CONNECTIVITY_IPV4_SUBNET = 0x10
#     NLM_CONNECTIVITY_IPV4_LOCALNETWORK = 0x20
#     NLM_CONNECTIVITY_IPV4_INTERNET = 0x40
#     NLM_CONNECTIVITY_IPV6_SUBNET = 0x100
#     NLM_CONNECTIVITY_IPV6_LOCALNETWORK = 0x200
#     NLM_CONNECTIVITY_IPV6_INTERNET = 0x400
        

from ctypes import wintypes
import ctypes




'''
I am building the windows application in wxpython and it is sending the ping to the particular API 
to the backend and suppose in between the internet has gone off
in that case i want to save the collected data to some database
tell me some methodologies or ways to do it 
'''