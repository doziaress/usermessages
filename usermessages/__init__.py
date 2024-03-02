#  ______     __  ____  ______ _______        __    __    __  
# |  _ \ \   / / |  _ \|  ____|__   __|/\    / /   / /   / /  
# | |_) \ \_/ /  | |_) | |__     | |  /  \  / /_  / /_  / /_  
# |  _ < \   /   |  _ <|  __|    | | / /\ \| '_ \| '_ \| '_ \ 
# | |_) | | |    | |_) | |____   | |/ ____ \ (_) | (_) | (_) |
# |____/  |_|    |____/|______|  |_/_/    \_\___/ \___/ \___/ 

from tkinter import *
import tkinter.messagebox

def popup(title, text, type):  
    window = Tk()
    window.wm_withdraw()

    if type == "error":
        # message at x:200,y:200
        window.geometry("1x1+200+200")  # remember its.geometry("WidthxHeight(+or-)X(+or-)Y")
        tkinter.messagebox.showerror(title=title, message=text, parent=window)
    if type == "info":
        # center screen message
        window.geometry(f"1x1+{round(window.winfo_screenwidth() / 2)}+{round(window.winfo_screenheight() / 2)}")
        tkinter.messagebox.showinfo(title=title, message=text)
    if type == "warning":
        window.geometry(f"1x1+{round(window.winfo_screenwidth() / 2)}+{round(window.winfo_screenheight() / 2)}")
        tkinter.messagebox.showwarning(title=title, message=text)
    else:
        print("[usermessages.ERROR] WRONG MESSAGE TYPE!")
        print("[usermessages.WARN] Valid message types: error info warning")

def textpopup(title, head, line2):
    print(rf'''
██████████████████████████████████████████████████████████████
█ {title}                                                   █
██████████████████████████████████████████████████████████████
█{head}                                                     █
█{line2}                                                     █
█                                                            █
█                                                ██████████  █
█                                                █   OK   █  █
█                                                ██████████  █
█                                                            █
██████████████████████████████████████████████████████████████
''')