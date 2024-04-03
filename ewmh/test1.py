from ewmh import EWMH
import ewmh
import time

time.sleep(6)
ewmh = EWMH()


# Get the active window
active_window = ewmh.getActiveWindow()

# Get the window class name
window_class = ewmh.getWmClass(active_window)
print(window_class,'-----------------------------------')

# Check if the window belongs to Chrome
if window_class[1] == "Google-chrome":
    # Get window properties
    properties = ewmh.getWmVisibleName(active_window)

    # Print window properties
    print(properties)
else:
    print("Active window does not belong to Chrome.")

# Close the connection
ewmh.display.close()
