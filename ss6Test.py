
'''Toolbar - 'App bar'    (L0, T49, R960, B106)
   |    |    |    |    |    | ['App barToolbar', 'Toolbar', 'App bar']
   |    |    |    |    |    | child_window(title="App bar", auto_id="view_1000", control_type="ToolBar")'''

'''Edit - 'https://www.google.co.in'    (L217, T58, R562, B97)
   |    |    |    |    |    |    |    |    | ['Edit', 'Edit0', 'Edit1']
   |    |    |    |    |    |    |    |    | child_window(title="https://www.google.co.in", auto_id="view_1022", control_type="Edit")'''

'''child_window(auto_id="view_1022", control_type="Edit")'''

'''Edit - ''    (L217, T58, R424, B97)
   |    |    |    |    |    |    |    |    | ['Edit', 'Edit0', 'Edit1']
   |    |    |    |    |    |    |    |    | child_window(auto_id="view_1022", control_type="Edit")'''

'''Microsoft\u200b Edge'''



import pygetwindow as gw
import pyautogui
from win32gui import GetForegroundWindow
from win32process import GetWindowThreadProcessId
from pywinauto.application import Application
import time

import wx
import pyscreenshot
import pygetwindow as pyg
import logging
import datetime
import psutil
import os
import pywinauto

# ob=psutil.process_iter()
# for i in ob:
#     if i.name == "chrome.exe":
#         print(i)

# log_config= logging.basicConfig(filename='log_files\demo_ss4.log',level=logging.DEBUG , format= " %(asctime)s - %(levelname)s - %(message)s")
# logging.info("hello world")

'''Creating root logger'''

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatting=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler=logging.FileHandler('log_files\demo_ss4.log')
file_handler.setFormatter(formatting)

logger.addHandler(file_handler)

'''Creating root logger Ends'''


logger.debug(f"################  Start of the program at - {datetime.datetime.now()} ############################")



i=1
def screenshot(event):
    global i
    im=pyscreenshot.grab()
    image_ss_name=f'screenshot_no.{i}'
    i+=1
    image_path=f'.\dummy_ss\{image_ss_name}.png'

    im.save(image_path)

    logger.info(f"screen shot {i-1} taken")
    # print(f"screen shot {i-1} taken")


def get_url_window(e):
    
    window = GetForegroundWindow()
    print("Window" , window)
    tid, pid = GetWindowThreadProcessId(window)
    print(pid)

    app = Application(backend="uia").connect(process=pid, time_out=10)

    # app.NewTabGoogleChrome.print_control_identifiers()
    app.NewTabBrave.print_control_identifiers()
    # app.NewtabProfile1MicrosoftEdge.print_control_identifiers()
    # app.GoogleProfile1MicrosoftEdge.print_control_identifiers()

    dlg = app.top_window()


    possible_titles = ["Search or enter address", "Address and search bar", "Address bar"]
    possible_control_types = ["Edit", "ComboBox"]
    url = None
    for title in possible_titles:
        for control_type in possible_control_types:
            try:
                url_control = dlg.child_window( control_type=control_type, auto_id = "view_1022")
                if url_control.exists():
                    url = url_control.get_value()
                    if url:
                        break
            except Exception as e:
                print(f"Error while trying to retrieve URL with title '{title}' and control type '{control_type}': {e}")
        if url:
            break

    # Check if URL was found
    if url:
        print("URL:", url)
    else:
        print("Failed to retrieve URL.")


    # window = GetForegroundWindow()
    # print("Window" , window)
    # tid, pid = GetWindowThreadProcessId(window)
    # print(pid)

    # app = Application(backend="uia").connect(process=pid, time_out=10)

    # # app.NewTabGoogleChrome.print_control_identifiers()
    # # app.NewtabProfile1MicrosoftEdge.print_control_identifiers()
    # # app.GoogleProfile1MicrosoftEdge.print_control_identifiers()

    # dlg = app.top_window()
    # title = "Address and search bar"
    # # title=u'Search or enter address'   # for firefox
    # # title="Search Google or type a URL"

    # try:
    #     # abs= app.
    #     url = dlg.child_window( title = title , control_type="Edit").get_value()
    #     print("URL================> ", url)
    #     logger.info(f"incoming URL------{url}")
    # except Exception as e:
    #     # print(e)
    #     print("Error: browser not found",)
    

def collect_activeWindows(event):
    window :str  =pyg.getActiveWindowTitle()

    # other1= pyg.getAllTitles()
    # other2= pyg.getActiveWindow()

    # print(other1)
    # print(other2)

    print(window)
    logger.info(f" active window of user - {window}")
    # lst=window.split(' - ')
    # print(lst)
    

class MyPanel(wx.Panel):
    def __init__(self,parent):

        super().__init__(parent)

        parent.CreateStatusBar()

        # self.timer_screenshot=wx.Timer(self)
        # print('21212v1h3v21h3bh')
        # self.Bind(wx.EVT_TIMER,screenshot,self.timer_screenshot)
        # # self.timer.Bind(wx.EVT_TIMER,screenshot)
        # print("dasvdjsa")
        # self.timer_screenshot.Start(5000)
        # print("dasbdsad")

        # self.take_ss=Timer_ss(self)

        # '''functionalities for taking titles of the active window on which the cursor is active'''
        # self.timer_activewindow=wx.Timer(self)
        # self.Bind(wx.EVT_TIMER,collect_activeWindows,self.timer_activewindow)
        # self.timer_activewindow.Start(5000)

        '''breaking down above thing to new component'''
        self.get_activeWindows=Timer_activeWindow(self)


        #fetching windows url
        # self.urlFetching=wx.Timer(self)
        # self.Bind(wx.EVT_TIMER,get_url_window,self.urlFetching)
        # self.urlFetching.Start(5000)
        self.take_ulr = Url_FetchingWindow(self)



class Url_FetchingWindow(wx.Timer):
    
    def __init__(self,parent:MyPanel):

        super().__init__(parent)
        parent.Bind(wx.EVT_TIMER,get_url_window,self)
        self.Start(5000)

class Timer_activeWindow(wx.Timer):

    def __init__(self,parent:MyPanel):
        
        super().__init__(parent)
        parent.Bind(wx.EVT_TIMER,collect_activeWindows,self)
        self.Start(5000)

class Timer_ss(wx.Timer):
    def __init__(self,parent : MyPanel):
        super().__init__(parent)

        parent.Bind(wx.EVT_TIMER,screenshot,self)
        self.Start(5000)        
        
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="Screen Shot", size=(200,200),style=wx.CAPTION)

        self.panel=MyPanel(self)


class MyAPP(wx.App):
    def __init__(self):
        super().__init__()
        self.frame=MyFrame()

        self.frame.Show()   

        self.MainLoop()


if __name__=="__main__":
    app=MyAPP()



