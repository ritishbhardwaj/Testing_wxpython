# import wx

# class MainFrame(wx.Frame):
#     def __init__(self):
#         super(MainFrame, self).__init__(None, title='Main Window')
#         self.panel = wx.Panel(self)
        
#         self.child_frame = wx.Frame(self, title='Child Frame')  # Child frame with main window as parent
#         self.child_frame.Show()

#         self.move_child_frame_button = wx.Button(self.panel, label='Move Child Frame')
#         self.move_child_frame_button.Bind(wx.EVT_BUTTON, self.on_move_child_frame)
        
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(self.move_child_frame_button, 0, wx.ALL, 10)
#         self.panel.SetSizer(sizer)
#         self.Show()

#     def on_move_child_frame(self, event):
#         # Reparent the child frame to None (no parent)
#         self.child_frame.Reparent(None)
#         self.child_frame.SetTitle('Detached Child Frame')  # Optional: Change title to indicate detachment

# if __name__ == '__main__':
#     app = wx.App()
#     MainFrame()
#     app.MainLoop()


import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super(MainFrame, self).__init__(None, title='Main Window')
        self.panel = wx.Panel(self)
        
        self.child_frame = wx.Frame(None, title='Child Frame')  # Child frame with no parent
        self.child_frame.Show()

        self.move_child_frame_button = wx.Button(self.panel, label='Move Child Frame')
        self.move_child_frame_button.Bind(wx.EVT_BUTTON, self.on_move_child_frame)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.move_child_frame_button, 0, wx.ALL, 10)
        self.panel.SetSizer(sizer)
        self.Show()

    def on_move_child_frame(self, event):
        # Reparent the child frame to this main frame
        self.child_frame.Reparent(self)
        self.child_frame.SetTitle('Attached Child Frame')  # Optional: Change title to indicate attachment

if __name__ == '__main__':
    app = wx.App()
    MainFrame()
    app.MainLoop()



import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super(MainFrame, self).__init__(None, title='Main Window')
        self.panel = wx.Panel(self)
        
        # Create the child frame with no parent
        self.child_frame = wx.Frame(None, title='Child Frame', style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.CLOSE_BOX))
        self.child_frame.Show()

        self.move_child_frame_button = wx.Button(self.panel, label='Move Child Frame')
        self.move_child_frame_button.Bind(wx.EVT_BUTTON, self.on_move_child_frame)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.move_child_frame_button, 0, wx.ALL, 10)
        self.panel.SetSizer(sizer)
        self.Show()

    def on_move_child_frame(self, event):
        # Reparent the child frame to this main frame
        self.child_frame.Reparent(self)
        self.child_frame.SetTitle('Attached Child Frame')  # Optional: Change title to indicate attachment

if __name__ == '__main__':
    app = wx.App()
    MainFrame()
    app.MainLoop()
