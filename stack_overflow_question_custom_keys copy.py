import tkinter as tk
import os
import random
import webbrowser
from tkinter import Frame
class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        self.link_list = ['evernote:///view/21614375/s192/10b4247b-5f09-4b66-953d-02e5f27aac3c/10b4247b-5f09-4b66-953d-02e5f27aac3c/',
                        'Anaconda-Navigator://', 'zoom.us://', 'Evernote://', 'Messages://',
                        'https://open.spotify.com/track/2gI9RfuSwulsBujm7hbOFv?si=891addaca9524eaf',
                        'spotify://', 'workflowy://', 'Brave-Browser://']

    def create_widgets(self):

        self.button_number = 0
        #for loop button creation
        for i in range(3):
            for j in range(3):
                #first button
                self.first_button = tk.Button(self, state = 'normal', padx =50, pady = 50)
                self.first_button["text"] = "BUTTON",self.button_number
                self.first_button["command"] = lambda: webbrowser.open(self.link_list[self.button_number])
                #self.first_button["command"] = self.lets_go
                self.first_button.grid(row = i, column = j)
                self.button_number += 1

        ##QUIT BUTTON
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid()

    #for First Button
    def lets_go(self):
        webbrowser.open(self.link_list[self.button_number])   #, new = 0 )


root = tk.Tk()
app = Application(master = root)
app.mainloop()