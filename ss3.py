import wx
import pyscreenshot
import os
import PIL
import pygetwindow as pyg


i=1
def screenshot(event):
    global i
    im=pyscreenshot.grab()
    image_ss_name=f'screenshot_no.{i}'
    i+=1
    image_path=f'.\dummy_ss\{image_ss_name}.png'

    im.save(image_path)

    print(f"screen shot {i-1} taken")


def collect_activeWindows(event):
    window=pyg.getActiveWindowTitle()

    print(window)

    

class MyPanel(wx.Panel):
    def __init__(self,parent):

        super().__init__(parent)

        parent.CreateStatusBar()

        # self.timer_screenshot=wx.Timer(self)
        # print('21212v1h3v21h3bh')
        # self.Bind(wx.EVT_TIMER,screenshot,self.timer_screenshot)
        # # self.timer.Bind(wx.EVT_TIMER,screenshot)
        # print("dasvdjsa")
        # self.timer_screenshot.Start(5000)
        # print("dasbdsad")

        self.take_ss=Timer_ss(self)

        # '''functionalities for taking titles of the active window on which the cursor is active'''
        # self.timer_activewindow=wx.Timer(self)
        # self.Bind(wx.EVT_TIMER,collect_activeWindows,self.timer_activewindow)
        # self.timer_activewindow.Start(5000)

        '''breaking down above thing to new component'''
        self.get_activeWindows=Timer_activeWindow(self)
        


class Timer_activeWindow(wx.Timer):

    def __init__(self,parent:MyPanel):
        
        super().__init__(parent)
        parent.Bind(wx.EVT_TIMER,collect_activeWindows,self)
        self.Start(5000)

class Timer_ss(wx.Timer):
    def __init__(self,parent : MyPanel):
        super().__init__(parent)

        parent.Bind(wx.EVT_TIMER,screenshot,self)
        self.Start(5000)        
        
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


# import wx

# class MyTimer(wx.Timer):
#     def __init__(self, owner):
#         super().__init__()
#         self.SetOwner(owner)

#     def Notify(self):
#         print("Timer expired!")
#         # Additional processing code if needed

# # Example usage:
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = wx.Frame(None, title="Timer Example")
#     timer = MyTimer(frame)  # Create an instance of MyTimer with the frame as the owner
#     timer.Start(1000)  # Start the timer with a 1-second interval
#     frame.Show()
#     app.MainLoop()
