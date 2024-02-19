import wx
import os
import PIL
import time
import pyscreenshot as ImageGrab

j=1
def takeSS(event):
    global j
    print(event)

    # for i in range(50):
    #     img_saving_name=f'screenshot_no.-{str(i)}'
    #     im=ImageGrab.grab()
    #     file_path= f'./dummy_ss/{img_saving_name}.png'
    #     im.save(file_path)
    #     time.sleep(5)
    
    
    while True:
        img_saving_name=f'screenshot_no.-{str(j)}'
        j+=1
        im=ImageGrab.grab()
        file_path= f'./dummy_ss/{img_saving_name}.png'
        im.save(file_path)
        time.sleep(5)

    
    return True



class MyPanel(wx.Panel):
    def __init__(self,parent):

        super().__init__(parent)

        parent.CreateStatusBar()

        
        btn=wx.Button(self,label="ScreenShot",pos=(150,100))
        btn2=wx.Button(self,label="Stop",pos=(150,150))
        btn.Bind(wx.EVT_BUTTON,takeSS)




class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="Screen Shot", size=(400,400))

        self.panel=MyPanel(self)


class MyAPP(wx.App):
    def __init__(self):
        super().__init__()
        self.frame=MyFrame()

        self.frame.Show()   

        self.MainLoop()


if __name__=="__main__":
    app=MyAPP()
