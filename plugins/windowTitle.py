import pygetwindow as pyg



def collect_activeWindows(event):
    window :str  =pyg.getActiveWindowTitle()

    # aa= pyg.getActiveWindow()
    # print(dir(aa),"<----------------------------------")

    # aawnd = pyg.getWindowsWithTitle(window)
    # print(aawnd[0]._hWnd,'-=-=-=-=-=-=-=-=-=-=-=')
    # print(window,'-----=-=-=-=-=-=-=-=-=-=-=')
    print('window==========>',window)
    # logger.info(f" active window of user - {window}")