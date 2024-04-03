import wx
import time

from pynput import keyboard, mouse

# Custom event to track mouse, keyboard activity, and screen lock
EVT_ACTIVITY = wx.PyEventBinder(wx.NewEventType(), 1)
print('kk')

class ActivityEvent(wx.PyCommandEvent):
    def __init__(self, eventType, id):
        wx.PyCommandEvent.__init__(self, eventType, id)
        self.SetEventType(eventType)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        self.timer = wx.Timer(self)
        # self.delay_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.check_activity, self.timer)
        # self.Bind(wx.EVT_TIMER, self.reset_status, self.delay_timer)

        self.last_activity_time = time.time()
        self.screen_locked = False
        self.locked_status_flag = False

        # Create UI components
        self.label = wx.StaticText(self, label="Status:")
        self.status_text = wx.StaticText(self, label="Working")


        # Bind keyboard event for Windows + L
        # self.Bind(wx.EVT_HOTKEY, self.on_hotkey)
        # self.RegisterHotKey(1, wx.MOD_WIN, ord('L'))

        # Create pynput keyboard listener
        self.keyboard_listener = keyboard.Listener(on_press=self.on_keyboard_press)
        self.keyboard_listener.start()

        # Create pynput mouse listener
        self.mouse_listener = mouse.Listener(on_move=self.on_mouse_move)
        self.mouse_listener.start()

        self.timer.Start(2000)  # Timer interval in ms (1 second)
        
        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.label, 0, wx.ALL, 5)
        sizer.Add(self.status_text, 0, wx.ALL, 5)
        self.SetSizer(sizer)

    def on_mouse_move(self, x, y):
        # Update last activity time whenever there's mouse movement
        self.last_activity_time = time.time()
        print('mouse moved')
        # self.status_text.SetLabel("Working")

    def on_keyboard_press(self, key):
        # Update last activity time whenever there's keyboard activity
        self.last_activity_time = time.time()
        print('keyboard pressed')
        # self.status_text.SetLabel("Working")

    def check_activity(self, event):
        if self.screen_locked:
            self.status_text.SetLabel("Locked and Not Working")
            self.locked_status_flag = True
            self.delay_timer.Start(3000)  # Delay for 3 seconds (3000 ms)
        else:
            current_time = time.time()
            if current_time - self.last_activity_time > 5:  # 5 seconds of inactivity
                self.status_text.SetLabel("Not Working")
            else:
                self.status_text.SetLabel("Working")

    def reset_status(self, event):
        self.screen_locked = False
        self.locked_status_flag = False
        self.status_text.SetLabel("Idle")
        self.delay_timer.Stop()


class MyFrame(wx.Frame):
    def __init__(self):
        super(MyFrame, self).__init__(None, title="Keyboard Mouse Tracking App", size=(400, 200))
        panel = MyPanel(self)
        self.Show()

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame()
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()


# import time
# import wx
# class MyForm(wx.Frame):
#  def __init__(self):
#     wx.Frame.__init__(self, None, title="Timer Tutorial 1",
#     size=(500,500))
#     panel = wx.Panel(self, wx.ID_ANY)
#     self.timer = wx.Timer(self)
#     self.Bind(wx.EVT_TIMER, self.update, self.timer)
#     self.toggleBtn = wx.Button(panel, wx.ID_ANY, "Start")
#     self.toggleBtn.Bind(wx.EVT_BUTTON, self.onToggle)
#  def onToggle(self, event):
#     btnLabel = self.toggleBtn.GetLabel()
#     if btnLabel == "Start":
#         print("starting timer...")
#         self.timer.Start(1000)
#         self.toggleBtn.SetLabel("Stop")
#     else:
#         print("timer stopped!")
#         self.timer.Stop()
#         self.toggleBtn.SetLabel("Start")
#  def update(self, event):
#     print("\nupdated: ", time.ctime())
# # Run the program
# if __name__ == "__main__":
#  app = wx.App(True)
#  frame = MyForm().Show()
#  app.MainLoop()