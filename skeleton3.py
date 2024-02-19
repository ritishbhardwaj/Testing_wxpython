from typing import *
import wx


class MyFrame(wx.Frame):
    def __init__(self,parent,title:str,size:Tuple[int]):
        super().__init__(parent=parent,title=title,size=size)

        self.panel=MyPanel(self)



class MyPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent)


class MyApp(wx.App):
    
    def __init__(self,parent,title:str,size=Tuple[int]):
        super().__init__()
        self.frame=MyFrame(parent=parent,title=title,size=size)
        self.frame.Show()

        
if __name__=="__main__":

    app=MyApp(None,"skeleton3",(600,500))
    app.MainLoop()