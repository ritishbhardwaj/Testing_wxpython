import wx
from typing import Tuple


class MyFrame(wx.Frame):

    def __init__(self, parent, size: Tuple[int], title: str):
        super().__init__(parent=parent, title=title, size=size,style = wx.DEFAULT_FRAME_STYLE & ~(wx.MAXIMIZE_BOX | wx.CLOSE_BOX))

        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        parent.CreateStatusBar()

        sizer = wx.GridBagSizer()

        self.toggleBTN = wx.ToggleButton(self, label="Toggle Button")
        sizer.Add(self.toggleBTN, pos=(0, 0), flag=wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, border=5)

        self.label = wx.StaticText(self, label="Hello World",pos=(100,100))

        self.toggleBTN.Bind(wx.EVT_TOGGLEBUTTON,self.onClickToggle)

        self.SetSizer(sizer)
    
    def onClickToggle(self, event):
        state = self.toggleBTN.GetValue()  # Get the value of the toggle button
        sssss=self.toggleBTN
        print(state)
        print(sssss.GetLabel)
        if state == True:
            self.label.SetLabelText("Off")
            self.toggleBTN.SetLabel("Click to on")
        else:
            self.label.SetLabelText("On")
            self.toggleBTN.SetLabel("Click to off")




class MyApp(wx.App):
    def __init__(self, parent, size: Tuple[int], title: str):
        super().__init__()
        self.frame = MyFrame(parent, size, title)

        self.frame.Center()
        self.frame.Show()


if __name__ == "__main__":
    app = MyApp(None, (400, 400), "Box Sizer")
    app.MainLoop()
