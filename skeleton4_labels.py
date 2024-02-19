import wx
from typing import *


class MyFrame(wx.Frame):

    def __init__(self,parent,size:Tuple[int],title:str):
        super().__init__(parent=parent,title=title,size=size)

        self.panel=Mypanel(self)

        

class Mypanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)

        self.label=wx.StaticText(self,label="Hello World",pos=(200,200))



class MyApp(wx.App):
    def __init__(self,parent, size:tuple, title:str):
        super().__init__()
        self.frame=MyFrame(parent,size,title)
        self.frame.Show()



if __name__=="__main__":
    app=MyApp(None,(600,500),"label",)
    app.MainLoop()