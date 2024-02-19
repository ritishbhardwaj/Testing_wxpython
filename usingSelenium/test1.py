# import selenium
# from selenium.webdriver.common.by import By
# from selenium import webdriver

# driver = webdriver.Firefox()

# print(driver.current_url)



# from splinter import browser
# import requests


# ## go to original page 
# browser.visit(url)

# ## Loop through the page associated with each headline
# for headline in titles:
#     print(headline.text)
#     browser.click_link_by_partial_text(headline.text)
# ## Now that I'm on the new page, I need to grab the url
#     new_url = browser.url
#     print(new_url)
# ## Go back to original page
#     browser.visit(url)



from win32gui import GetForegroundWindow
from win32process import GetWindowThreadProcessId
from pywinauto.application import Application
import time


time.sleep(5)
window = GetForegroundWindow()
tid, pid = GetWindowThreadProcessId(window)
app = Application(backend="uia").connect(process=pid, time_out=10)
dlg = app.top_window()
title = "Address and search bar"
url = dlg.child_window(title=title, control_type="Edit").get_value()
print(url)