#functional_coding_custom_keys.py

import tkinter as tk
import os
import random
import webbrowser
from tkinter import Frame
#custom_keys_building


""" https://chrome.google.com/webstore/detail/open-in-spotify-desktop-c/okkdbmdhpgmajopdpmflkldkemcldnjd
#for Spotify links to open (from Chrome based) in app directly """

""" button_list = [
['Evernote: Love','evernote:///view/21614375/s192/10b4247b-5f09-4b66-953d-02e5f27aac3c/10b4247b-5f09-4b66-953d-02e5f27aac3c/'],
['Trello: עכשיו', 'trello://trello.com/b/kGXNJK3x/עכשיו'],
['Trello: Web','https://trello.com/c/Ljfh6gZq'],
['Trello: Specfic','trello://trello.com/c/Ljfh6gZq'],
['Spotify: Shabbat','https://open.spotify.com/track/2gI9RfuSwulsBujm7hbOFv?si=891addaca9524eaf']
] """

#####CREATING A ROW OF BUTTONS

##############################

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_frame(self):
        self.frame_name = input("what is the frame name? ")
        self.frame_name = Frame(root)
        return frame_name
    
    def button_assigner(self):
        self.create_frame()
        self.second_button = tk.Button(frame_name, text = "test", fg = "red")
        second_button.pack(side = LEFT)

    def create_widgets(self):
        self.button_assigner()
        #first button
        self.first_button = tk.Button(self)
        self.first_button["text"] = "FIRST_BUTTON"
        self.first_button["command"] = self.lets_go
        self.first_button.pack()

        #Hello World Button
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello! World!\nHAKADOSH BARUCH HU\n\
            OHEV OTCHA\n\
            HAKOL MA D'AVID RACHMANA, L'TAV AVID"
        self.hi_there["command"] = self.say_shalom
        self.hi_there.pack()

        ##QUIT BUTTON
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    #For Hello World Button
    def say_shalom(self):
        print("הקדש ברוך הוא")
    
    #for First Button
    def lets_go(self):
        evernote_inspiration = ["https://www.evernote.com/l/AMAEQnYwmhJHhKGyUfGGhZkjECHugdb2REke"]
        webbrowser.open("evernote:///view/21614375/s192/10b4247b-5f09-4b66-953d-02e5f27aac3c/10b4247b-5f09-4b66-953d-02e5f27aac3c/")   #, new = 0 )


#root = tk.Tk()
#app = Application(master = root)
#app.mainloop()     



root = tk.Tk()
this_frame = Frame(root)
that_frame = Frame(root)
that_frame.pack(side = "bottom")
this_frame.pack()

def say_shalom():
    print("הקדש ברוך הוא")

hi_there = tk.Button(this_frame)
hi_there["text"] = "Hello! World!\nHAKADOSH BARUCH HU\n OHEV OTCHA\n HAKOL MA D'AVID RACHMANA, L'TAV AVID"
hi_there["command"] = say_shalom
hi_there.pack(side = "right")

hi_t = tk.Button(that_frame)
hi_t["text"] = "Hi - sending my very best"
hi_t["command"] = say_shalom
hi_t.pack()#side = "right")

        ##QUIT BUTTON
quitt = tk.Button(this_frame, text="QUIT", fg="red")#, #command= destroy)
quitt.pack(side="bottom")

root.mainloop()