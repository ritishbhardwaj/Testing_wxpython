# import winreg

# def get_number_of_desktops():
#     key_path = r"Control Panel\Desktop"
#     value_name = "MultipleDesktops"
    
#     try:
#         with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as key:
#             value, _ = winreg.QueryValueEx(key, value_name)
#             return int(value)
#     except FileNotFoundError:
#         # Handle the case where the registry key doesn't exist
#         return 1  # Default to 1 desktop if not found

# # Example usage
# num_desktops = get_number_of_desktops()
# print("Number of desktops:", num_desktops)


# import socket

# def check_internet_connection():
#     try:
#         # Attempt to connect to a known remote host (in this case, Google's DNS server)
#         socket.create_connection(("8.8.8.8", 53), timeout=5)
#         return True
#     except OSError:
#         return False

# if check_internet_connection():
#     print("Internet connection is active.")
# else:
#     print("No internet connection.")

'''  ------------------------------------------------------------------------------------------'''
import time
import requests

def CheckConnection(api_url):
    try:
        start_time = time.time()
        response = requests.get(api_url, timeout=5)
        # print(response.text)
        end_time = time.time()
        # Check if the response status code is in the 2xx range
        if response.status_code // 100 == 2:
            print(end_time - start_time)
            print(f"{response.status_code}")
            return True
        else:
            print(f"{response.status_code}")
            print(response.text)
            print(response.json)
            return False
    except (requests.ConnectionError, requests.Timeout) as e:
        print(e)
        return False

# Example usage:
api_url = "https://www.instagram.com/"
api_url="https://localhost:8000/"
# api_url='https://user1709552498085.requestly.tech/testingConn/1?'
if CheckConnection(api_url):
    print("Connection with the server is successful.")
else:
    print("Unable to connect to the server.")

'''  ------------------------------------------------------------------------------------------'''


import httpx
import asyncio

async def CheckConnection(api_url):
    try:
        async with httpx.AsyncClient() as client:
            start_time = time.time()
            response = await client.get(api_url, timeout=5)
            end_time = time.time()
            return response.status_code == 200, end_time - start_time
    except httpx.HTTPError:
        return False, None

# Example usage:
api_url = "https://loclhost:8000/"

result, time_taken = asyncio.run(CheckConnection(api_url))

if result:
    print("Connection with the server is successful.")
    print(f"Time taken: {time_taken:.2f} seconds")
else:
    print("Unable to connect to the server.")

'''-------------------------------------------------------------------'''


import netifaces

def get_wifi_name():
    # Get a list of all network interfaces
    interfaces = netifaces.interfaces()

    # Iterate through each interface to find the one with 'wlan' in its name
    for interface in interfaces:
        if 'wlan' in interface:
            # Get the addresses for this interface
            addresses = netifaces.ifaddresses(interface)
            # Check if the interface has an IPv4 address (indicating it's connected to a network)
            if netifaces.AF_INET in addresses:
                # Return the SSID of the connected WiFi network
                return addresses[netifaces.AF_INET][0]['addr']

    # If no WiFi interface is found, return None
    return None

# Example usage:
wifi_name = get_wifi_name()
if wifi_name:
    print("Connected to WiFi network:", wifi_name)
else:
    print("Not connected to any WiFi network.")


