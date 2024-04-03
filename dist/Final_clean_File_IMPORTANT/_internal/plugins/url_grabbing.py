from win32gui import GetForegroundWindow , GetWindowText
from win32process import GetWindowThreadProcessId
from pywinauto.application import Application

def get_url_window(event):

    window = GetForegroundWindow()
    print("Window" , window)
    Text= GetWindowText(window)
    print(Text)

    l1=Text.split(' - ')
    l2=Text.split(' — ')
    # print("l1===========",l1)
    # print("=========l2",l2)

    final_lst = l1 if len(l1) > len(l2) else l2
    
    appname = final_lst[-1]

    tid, pid = GetWindowThreadProcessId(window)
    # print(pid)

    try:
        app = Application(backend="uia").connect(process=pid, time_out=10)
        dlg = app.top_window()
    except Exception as e:
        pass

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