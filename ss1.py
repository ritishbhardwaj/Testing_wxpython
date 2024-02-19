import wx

class ScreenshotFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Screenshot Capture")
        panel = wx.Panel(self)
        button = wx.Button(panel, label="&Close",)
        button.Bind(wx.EVT_BUTTON, self.on_capture)
        self.Bind(wx.EVT_BUTTON, self.on_capture,button)
        # sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, 10)
        # panel.SetSizer(sizer)
        self.Show()

    def on_capture(self, event):
        screen = wx.ScreenDC()
        print(screen)
        size = screen.GetSize()
        print(size)
        bmp = wx.Bitmap(size.width, size.height)
        mem = wx.MemoryDC(bmp)
        mem.Blit(0, 0, size.width, size.height, screen, 0, 0)
        del mem  # release bitmap
        bmp.SaveFile("screenshot.png", wx.BITMAP_TYPE_PNG)
        print("Screenshot captured and saved as 'screenshot.png'")

if __name__ == "__main__":
    app = wx.App(False)
    frame = ScreenshotFrame()
    app.MainLoop()
