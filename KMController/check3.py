import time
import wx
import threading
from win32gui import GetForegroundWindow, GetWindowText
from win32process import GetWindowThreadProcessId
from pywinauto.application import Application

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 300))
        
        panel = wx.Panel(self)
        btn = wx.Button(panel, label="Extract URL", pos=(150, 100))
        btn.Bind(wx.EVT_BUTTON, self.on_extract_button)
        
        self.Show()

    def extract_url_from_window(self):
        window = GetForegroundWindow()
        text = GetWindowText(window)
        app_name = text.split(' - ')[-1]
        print(app_name)

        tid, pid = GetWindowThreadProcessId(window)
        
        try:
            app = Application(backend="uia").connect(process=pid, timeout=10)
            dlg = app.top_window()
            
            url = None
            title = "Address and search bar"

            if 'Microsoft\u200b Edge' in app_name or 'Microsoft Edge' in app_name:
                url = dlg.child_window(auto_id="view_1022", control_type="Edit").get_value()
            
            elif 'Brave' in app_name or 'Google Chrome' in app_name:
                url = dlg.child_window(title=title, control_type="Edit").get_value()

            elif 'Mozilla Firefox' in app_name or 'Mozilla Firefox Private Browsing' in app_name:
                url = dlg.child_window(auto_id="urlbar-input", control_type="Edit").get_value()

            if url is None:
                print("No URL found")
            else:
                print("URL:", url)

        except Exception as e:
            print("Error occurred:", e)

    def on_extract_button(self, event):
        time.sleep(8)
        threading.Thread(target=self.extract_url_from_window).start()

app = wx.App()
frame = MyFrame(None, "URL Extractor")
app.MainLoop()