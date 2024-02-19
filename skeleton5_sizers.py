import wx
from typing import *


class MyFrame(wx.Frame):

    def __init__(self,parent,size:Tuple[int],title:str):
        super().__init__(parent=parent,title=title,size=size,)

        self.panel=Mypanel(self)

        

class Mypanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)

        self.label=wx.StaticText(self,label="Hello World",pos=(200,200))
        parent.CreateStatusBar()

        sizer=wx.GridBagSizer(4,3)

        sizer.Add(wx.Button(self,label="1"),pos=(0,0))
        sizer.Add(wx.Button(self,label="2"),pos=(0,1))
        sizer.Add(wx.Button(self,label="3"),pos=(0,2))
        sizer.Add(wx.Button(self,label="4"),pos=(1,0))
        sizer.Add(wx.Button(self,label="5"),pos=(1,1))
        sizer.Add(wx.Button(self,label="6"),pos=(1,2))
        sizer.Add(wx.Button(self,label="7"),pos=(2,0))
        sizer.Add(wx.Button(self,label="8"),pos=(2,1))

        self.SetSizer(sizer)



class MyApp(wx.App):
    def __init__(self,parent, size:tuple, title:str):
        super().__init__()
        self.frame=MyFrame(parent,size,title)

        self.frame.Center()
        self.frame.Show()



if __name__=="__main__":
    app=MyApp(None,(400,400),"Box Sizer",)
    app.MainLoop()