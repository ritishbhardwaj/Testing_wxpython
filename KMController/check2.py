import wx


class MyPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent=parent)


        # self.timer= wx.Timer(self)
        # self.Bind(wx.EVT_TIMER,self.onMove,self.timer)
        # self.timer.Start(1000)

        self.Bind(wx.EVT_MOTION,self.onMove)
        self.mouse_pos = wx.Point(0, 0)

    def onMove(self,event):
        # print("HELLO")
        # mouse_state = wx.GetMouseState()
        # self.mouse_pos = mouse_state.GetPosition()
        # frameeee= self.CaptureMouse()
        hehe=wx.GetMousePosition()
        # print(frameeee)
        print(hehe)
        # fr_pos = self.ClientToScreen(frameeee)
        # print(fr_pos)

        print("mouse Move",self.mouse_pos)






class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None,title="Screen Shot", size=(200,200),style=wx.CAPTION)
        self.mypanel = MyPanel(self)


class MyAPP(wx.App):
    def __init__(self):
        super().__init__()
        self.frame=MyFrame()

        self.frame.Show()   

        self.MainLoop()


if __name__=="__main__":
    app=MyAPP()