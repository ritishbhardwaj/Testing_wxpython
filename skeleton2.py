import wx

class myFrame(wx.Frame):

    def __init__(self):
        super(myFrame,self).__init__(None,title="HELLO WORLD",size=(600,600))
        self.Show()


if __name__=="__main__":
    app=wx.App()
    frame=myFrame()
    app.MainLoop()
