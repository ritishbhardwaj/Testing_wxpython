import time
import pygetwindow  as pyg


windows=pyg.getAllTitles()

for w in windows:
    print(w.title)


# for i in range(10):
#     time.sleep(1)
#     window= pyg.getAllWindows()
#     # urll= pyg.Win32Window.
#     print(window)


'''[Win32Window(hWnd=6423348), Win32Window(hWnd=2885496), Win32Window(hWnd=1116244), Win32Window(hWnd=198556), Win32Window(hWnd=196664), Win32Window(hWnd=67086), Win32Window(hWnd=1114612), Win32Window(hWnd=263168), Win32Window(hWnd=197114), Win32Window(hWnd=3801952), Win32Window(hWnd=3147004), Win32Window(hWnd=2557086), Win32Window(hWnd=394994), Win32Window(hWnd=132242), Win32Window(hWnd=132496), Win32Window(hWnd=132494), Win32Window(hWnd=66870), Win32Window(hWnd=66834), Win32Window(hWnd=196906), Win32Window(hWnd=131912), Win32Window(hWnd=2491622), Win32Window(hWnd=458802), Win32Window(hWnd=459646), Win32Window(hWnd=197096), Win32Window(hWnd=262220), Win32Window(hWnd=66748), Win32Window(hWnd=1378266), Win32Window(hWnd=2688650), Win32Window(hWnd=264050), Win32Window(hWnd=657152)]'''