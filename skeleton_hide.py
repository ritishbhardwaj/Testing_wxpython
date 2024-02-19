import locale
try:    # wxPython
    import wx
    import wx.adv
except ImportError as err:
    print(str(err))
    print("Requires wxPython (www.wxpython.org)")
    print("\tpython -m pip install wxpython")
app = wx.App(False)
locale.setlocale(locale.LC_ALL, 'C')

class MainFrame(wx.Frame):
    def __init__(self, parent=None, title="", size=wx.DefaultSize):
        wx.Frame.__init__(self, parent=parent, title=title, size=size)
        # Create task bar icon, but exit program if not available.
        self.taskBarIcon = wx.adv.TaskBarIcon()
        if self.taskBarIcon.IsAvailable() is False:
            raise SystemExit("Cannot access system tray")
        bitmap = wx.ArtProvider.GetBitmap(wx.ART_TIP, wx.ART_CMN_DIALOG, (32,32))
        self.taskBarIcon.SetIcon(wx.Icon(bitmap), "Tooltip")
        # Create timer and bind events
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_ICONIZE, self.OnMinimize)
        self.taskBarIcon.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.OnShowFrame)

    def OnMinimize(self, event):
        if self.IsIconized() is True:
            self.Hide()

    def OnShowFrame(self, event):
        # Restore Frame if it is minimized.
        if self.IsIconized() is True:
            self.Restore()
        # Show MainFrame if it is not shown already.
        if self.IsShown() is True:
            # Frame is already visible. Flash it.
            self.RequestUserAttention()
            self.SetFocus()
        else:
            self.Show()

    def OnClose(self, event):
        # Frame closed. Destroy taskbar icon and stop timer.
        event.Skip(True)
        self.taskBarIcon.Destroy()
        if self.timer.IsRunning() is True:
            self.timer.Stop()
        

# Instantiate and show frame and run event pump until user exits.
frame = MainFrame(parent=None, title="Tray Test", size=(600, 500))
frame.Show()
app.MainLoop()