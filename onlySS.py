
from datetime import datetime, timezone
# import platform
import wx
import io



def plugin_task():
    # @sender is the main App object in leap.py
    # Get the screen dimensions manually
        screen_width, screen_height = wx.GetDisplaySize()
        screenshot = wx.Bitmap(screen_width, screen_height)
        screen_dc = wx.ScreenDC()
        mem_dc = wx.MemoryDC()
        mem_dc.SelectObject(screenshot)
        mem_dc.Blit(0, 0, screen_width, screen_height, screen_dc, 0, 0)
        mem_dc.SelectObject(wx.NullBitmap)

        # Add timestamp to the screenshot filename
        dtnow = datetime.now(timezone.utc)
        timestamp = dtnow.strftime("%Y-%m-%d_%H-%M-%S")
        filename_dir = f"ss/ss_{timestamp}.png"
        
        # Save the screenshot as an image file
        screenshot.SaveFile(filename_dir, wx.BITMAP_TYPE_PNG)
        # print(f"Screenshot captured and saved as {filename}")
        
        filename = f"ss_{timestamp}.png"
        screenshot_image = wx.Image(screenshot.ConvertToImage())
        screenshot_bytes_io = io.BytesIO()
        screenshot_image.SaveFile(screenshot_bytes_io, wx.BITMAP_TYPE_PNG)



class MyPanel(wx.Panel):
    def __init__(self,parent):

        super().__init__(parent)

        plugin_task()


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

