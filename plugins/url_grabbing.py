from win32gui import GetForegroundWindow , GetWindowText
from win32process import GetWindowThreadProcessId
from pywinauto.application import Application
import threading

def getting_url_window():

    H_window = GetForegroundWindow()
    print("Window" , H_window)
    Text= GetWindowText(H_window)
    print(Text)
    Final = [] 
    l1 :list=Text.split(' - ')
    x:str
    for x in l1:
        temp=x.split(' — ')
        Final.extend(temp)
    print(Final)
        
    # l2=Text.split(' — ')
    # print("l1===========",l1)
    # print("=========l2",l2)

    # final_lst = l1 if len(l1) >= len(l2) else l2
    
    appname = Final[-1]
    print("Appname" , appname)

    tid, pid = GetWindowThreadProcessId(H_window)
    print(pid)

    try:
        app = Application(backend="uia").connect(process=pid, time_out=5)
        dlg = app.top_window()
    except Exception as e:
        return 

        # print(app)
    # app.NewTabGoogleChrome.print_control_identifiers()
    # app.NewtabProfile1MicrosoftEdge.print_control_identifiers()
    # app.GoogleProfile1MicrosoftEdge.print_control_identifiers()
    # app.MozillaFirefoxPrivateBrowsing.print_control_identifiers()
    # app.MozillaFirefox.print_control_identifiers() 
    # app.NewTabBrave.print_control_identifiers()
    # app.NewIncognitotabGoogleChrome.print_control_identifiers()
    # app.PluginBasepluginbaseGoogleChrome.print_control_identifiers()
    
    url=None
    title = "Address and search bar"
    # if 'Microsoft\u200b Edge' in final_lst:
    #     try: # Microsoft Browser Specific
    #         url = dlg.child_window(  auto_id = "view_1022",control_type="Edit" ).get_value()
    #         print("URL================> ", url)
    #         # logger.info(f"incoming URL------{url}")
    #     except Exception as e:
    #         pass

    # elif ('Brave' in final_lst)  or ('Google Chrome' in final_lst) :
    #     try:  # for Chrome and Brave Specific
    #         url = dlg.child_window(title=title, control_type = "Edit").get_value()
    #         print("URL================> ",url)
    #         # logger.info(f"incoming URL------{url}")
    #     except Exception as e:
    #         pass

    # elif 'Mozilla Firefox' in final_lst or 'Mozilla Firefox Private Browsing' in final_lst:
    #     try:    # for Firefox specific
    #         url= dlg.child_window( auto_id="urlbar-input", control_type="Edit").get_value()
    #         print("URL==============>",url)
    
    #     except Exception as e:
    #         pass



    '''implementing same using the switch cases'''
    match  appname:

        case 'Microsoft\u200b Edge'  :
            try: # Microsoft Browser Specific
                url = dlg.child_window(  auto_id = "view_1022",control_type="Edit" ).get_value()
                print("URL================> ", url)
                # logger.info(f"incoming URL------{url}")
            except Exception as e:
                pass
        
        case 'Microsoft Edge':
            try: # Microsoft Browser Specific
                url = dlg.child_window(  auto_id = "view_1022",control_type="Edit" ).get_value()
                print("URL================> ", url)
                # logger.info(f"incoming URL------{url}")
            except Exception as e:
                pass
        
        case 'Brave':
            try:  # for Chrome and Brave Specific
                url = dlg.child_window(title=title, control_type = "Edit").get_value()
                print("URL================> ",url)
                # logger.info(f"incoming URL------{url}")
            except Exception as e:
                pass

        case 'Google Chrome':
            try:  # for Chrome and Brave Specific
                url = dlg.child_window(title=title, control_type = "Edit").get_value()
                print("URL================> ",url)
                # logger.info(f"incoming URL------{url}")
            except Exception as e:
                pass
        
        case 'Mozilla Firefox':
                try:    # for Firefox specific
                    url= dlg.child_window( auto_id="urlbar-input", control_type="Edit").get_value()
                    print("URL==============>",url)
                except Exception as e:
                    pass
        
        case  'Mozilla Firefox Private Browsing' :
            try:    # for Firefox specific
                url= dlg.child_window( auto_id="urlbar-input", control_type="Edit").get_value()
                print("URL==============>",url)   
            except Exception as e:
                pass


    if url==None:
        print("No url Found")        
    print()


def get_url_window(event):
    # threading.Timer(5.0, get_url_window).start()
    # getting_url_window()
    # thread =threading.Thread(target=getting_url_window)
    # thread.start()
    getting_url_window()


'''----------------------------------------------------------------------------------------======================='''


# from win32gui import GetForegroundWindow, GetWindowText
# from win32process import GetWindowThreadProcessId
# from pywinauto.application import Application
# import threading

# def extract_url_from_window():
#     window = GetForegroundWindow()
#     text = GetWindowText(window)
#     app_name = text.split(' - ')[-1]
#     tid, pid = GetWindowThreadProcessId(window)
    
#     try:
#         app = Application(backend="uia").connect(process=pid, timeout=10)
#         dlg = app.top_window()
        
#         url = None
#         title = "Address and search bar"

#         if 'Microsoft\u200b Edge' in app_name or 'Microsoft Edge' in app_name:
#             url = dlg.child_window(auto_id="view_1022", control_type="Edit").get_value()
        
#         elif 'Brave' in app_name or 'Google Chrome' in app_name:
#             url = dlg.child_window(title=title, control_type="Edit").get_value()

#         elif 'Mozilla Firefox' in app_name or 'Mozilla Firefox Private Browsing' in app_name:
#             url = dlg.child_window(auto_id="urlbar-input", control_type="Edit").get_value()

#         if url is None:
#             print("No URL found")
#         else:
#             print("URL:", url)

#     except Exception as e:
#         print("Error occurred:", e)

# def url_extraction_thread():
#     threading.Timer(5.0, url_extraction_thread).start()
#     extract_url_from_window()

# # Start the thread for URL extraction
# url_extraction_thread()

# # Your existing code for calling plugins can remain unchanged