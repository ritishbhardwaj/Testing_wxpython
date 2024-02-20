'''Edit - 'Search with Google or enter address'    (L0, T0, R0, B0)
   |    |    | ['Edit2']
   |    |    | child_window(title="Search with Google or enter address", auto_id="urlbar-input", control_type="Edit")'''

from win32gui import GetForegroundWindow , GetWindowText
from win32process import GetWindowThreadProcessId
from pywinauto.application import Application

import wx
import pyscreenshot
import pygetwindow as pyg
import logging
import datetime

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
    Text= GetWindowText(window)
    # print(Text)

    l1=Text.split(' - ')
    l2=Text.split(' — ')
    print("l1===========",l1)
    print("=========l2",l2)

    final_lst = l1 if len(l1) > len(l2) else l2

    tid, pid = GetWindowThreadProcessId(window)
    # print(pid)

    try:
        app = Application(backend="uia").connect(process=pid, time_out=10)
        dlg = app.top_window()
    except Exception as e:
        pass

    # app.NewTabGoogleChrome.print_control_identifiers()
    # app.NewtabProfile1MicrosoftEdge.print_control_identifiers()
    # app.GoogleProfile1MicrosoftEdge.print_control_identifiers()
    # app.MozillaFirefoxPrivateBrowsing.print_control_identifiers()
    # app.MozillaFirefox.print_control_identifiers()
    # app.NewTabBrave.print_control_identifiers()
    # app.NewIncognitotabGoogleChrome.print_control_identifiers()

    
    url=None
    title = "Address and search bar"
    if 'Microsoft\u200b Edge' in final_lst:
        try: # Microsoft Browser Specific
            url = dlg.child_window(  auto_id = "view_1022",control_type="Edit" ).get_value()
            print("URL================> ", url)
            # logger.info(f"incoming URL------{url}")
        except Exception as e:
            pass

    elif ('Brave' in final_lst)  or ('Google Chrome' in final_lst) :
        try:  # for Chrome and Brave Specific
            url = dlg.child_window(title=title, control_type = "Edit").get_value()
            print("URL================> ",url)
            logger.info(f"incoming URL------{url}")
        except Exception as e:
            pass

    elif 'Mozilla Firefox' in final_lst or 'Mozilla Firefox Private Browsing' in final_lst:
        try:    # for Firefox specific
            url= dlg.child_window( auto_id="urlbar-input", control_type="Edit").get_value()
            print("URL==============>",url)
    
        except Exception as e:
            pass

    if url==None:
        print("No url Found")        
    print()
    

def collect_activeWindows(event):
    window :str  =pyg.getActiveWindowTitle()

    aa= pyg.getActiveWindow()
    print(dir(aa),"<----------------------------------")

    # aawnd = pyg.getWindowsWithTitle(window)
    # print(aawnd[0]._hWnd,'-=-=-=-=-=-=-=-=-=-=-=')
    # print(window,'-----=-=-=-=-=-=-=-=-=-=-=')
    logger.info(f" active window of user - {window}")
    

class MyPanel(wx.Panel):
    def __init__(self,parent):

        super().__init__(parent)

        parent.CreateStatusBar()

        '''taking ScreenShots'''
        # self.take_ss=Timer_ss(self)
        
        '''Colleccting Active windows'''
        self.get_activeWindows=Timer_activeWindow(self)

        '''Collecting Urls'''
        # self.take_ulr = Url_FetchingWindow(self)



class Url_FetchingWindow(wx.Timer):
    
    def __init__(self,parent:MyPanel):

        super().__init__(parent)
        parent.Bind(wx.EVT_TIMER,get_url_window,self)
        self.Start(3000)

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