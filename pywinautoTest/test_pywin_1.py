# import win32gui
# import win32process
# import psutil

# def get_active_window_url():
#     # Get the handle of the active window
#     hwnd = win32gui.GetForegroundWindow()

#     # Get the process ID (PID) of the active window
#     _, pid = win32process.GetWindowThreadProcessId(hwnd)

#     # Get the process associated with the PID
#     process = psutil.Process(pid)

#     # Get the executable path of the process
#     exe_path = process.exe()

#     # Check if the process is a web browser
#     if "chrome" in exe_path.lower():
#         # For Chrome, use psutil to get the command line arguments
#         cmdline = process.cmdline()
#         # Find the argument that starts with "--app=" (contains the URL)
#         url_arg = next((arg for arg in cmdline if arg.startswith("--app=")), None)
#         # Extract the URL from the argument
#         if url_arg:
#             return url_arg.split("=")[1]
#     elif "firefox" in exe_path.lower():
#         # For Firefox, use psutil to get the command line arguments
#         cmdline = process.cmdline()
#         # Find the argument that starts with "-url" (contains the URL)
#         url_arg = next((arg for arg in cmdline if arg.startswith("-url")), None)
#         # Extract the URL from the argument
#         if url_arg:
#             return url_arg.split("=")[1]
#     # Add conditions for other browsers if needed

#     # If the active window is not a browser or the URL cannot be retrieved, return None
#     return None

# # Example usage:
# active_window_url = get_active_window_url()
# if active_window_url:
#     print("URL of the active window:", active_window_url)
# else:
#     print("No browser window is active or URL couldn't be retrieved.")






import time
import win32gui
import win32process
import psutil

# print(win32gui)
def get_active_browser_url():
    # Get handle of the active window
    hwnd = win32gui.GetForegroundWindow()

    # Get process ID (PID) of the active window
    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    print(hwnd,_,pid)

    # Get process information using psutil
    try:
        process = psutil.Process(pid)
        exe_path = process.exe()
        print('process',process, "  ", exe_path.lower())

    except psutil.NoSuchProcess:
        return None

    # Check if the process belongs to a browser
    if "chrome" in exe_path.lower():
        # For Chrome, retrieve URL from command line arguments
        cmdline = process.cmdline()
        print(cmdline)
        for arg in cmdline:
            if arg.startswith("--app="):
                return arg.split("=", 1)[1]
    elif "firefox" in exe_path.lower():
        # For Firefox, retrieve URL from command line arguments
        cmdline = process.cmdline()
        for arg in cmdline:
            if arg.startswith("-url"):
                return arg.split("=", 1)[1]

    # Add conditions for other browsers if needed

    # If the active window is not a browser or the URL cannot be retrieved, return None
    return None

# Example usage:
time.sleep(2)
active_browser_url = get_active_browser_url()
if active_browser_url:
    print("URL of the active browser window:", active_browser_url)
else:
    print("No active browser window found or URL couldn't be retrieved.")


# print("hello")