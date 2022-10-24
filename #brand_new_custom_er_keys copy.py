#brand_new_custom_er_keys.py

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




##Building a link manager to create a list of dictionaries. Each new dictionary is a new row.
##Navigating starts from (0,0) out to limits

def create_link_dictionary():
    row_count = input("How many rows?")
    link_dictionary = []
    
    for i in range(int(row_count)):
        row_link_dictionary = {}
        key_count = input("How many keys on the wall?")
        for j in range(int(key_count)):
            row_link_dictionary[i][j] = input("Which link would you like to set to space"+str(i)+","+str(j))
            print(row_link_dictionary[i][j])
        link_dictionary.append(row_link_dictionary)
    #print(link_dictionary)
    return(link_dictionary)

def runLink(link):
    #link = input("What is the link/direction?")
    global run_link_dictionary
    run_link_dictionary = create_link_dictionary()
    #print(run_link_dictionary)
    #run_link_dictionary[2][2] = link

    #webbrowser.open(link, new = 0 )

## This systematic workhorse takes you through each space and square
## and sets it's contents

def link_layer():
    row = input("how many rows?")
    for i in range(int(row)):
        column = input("how many columns?")
        for j in range(int(column)):    
            linking_item = input("Which link to lay in space " + str(i)+","+str(j)+" ")
            #print(run_link_dictionary[0][0])
            run_link_dictionary[i][j] = linking_item
    # print(run_link_dictionary)
    set_link_dictionary = run_link_dictionary
    return(set_link_dictionary)
def main_buttons():
    window = tk.Tk()
    topFrame = tk.Frame(master = window, relief = "sunken", borderwidth = 10)
    topFrame.pack(side = "right")
    bottomFrame = tk.Frame(master = window, relief = "raised", borderwidth = 10)
    bottomFrame.pack()
    durations = input("How many rounds of buttons?")
    for i in range(int(row)):
        for i in range(int(column)):
            b = tk.Button(text ="[A Key]", master = topFrame, width = 16, height = 5, command = lambda: runLink(set_link_dictionary[row][column]))
            b.pack(side = "left")
                                        # 
        ##Taking a jump at binding keys
        #b.bind('a', lambda event: runLink())   
        

                                        # b = tk.Button(text ="[B Key]", master = bottomFrame, width = 16, height = 5, command = lambda: runLink("evernote:///view/21614375/s192/10b4247b-5f09-4b66-953d-02e5f27aac3c/10b4247b-5f09-4b66-953d-02e5f27aac3c")) #command = helloCallBack)
                                        # b.pack(side = "left")
                                        
                                        # b = tk.Button(text ="[A Key]", master = topFrame, width = 16, height = 5, command = lambda: runLink("evernote:///view/21614375/s192/10b4247b-5f09-4b66-953d-02e5f27aac3c/10b4247b-5f09-4b66-953d-02e5f27aac3c")) #command = helloCallBack)
                                        # b.pack(side = "left")
                                        
                                        # b = tk.Button(text ="[B Key]", master = bottomFrame, width = 16, height = 5, command = lambda: runLink("evernote:///view/21614375/s192/10b4247b-5f09-4b66-953d-02e5f27aac3c/10b4247b-5f09-4b66-953d-02e5f27aac3c")) #command = helloCallBack)
                                        # b.pack(side = "left")
    window.mainloop()  

###################################################
###################################################
########## NEW EVERNOTE BUTTON ADDITION ###########
###################################################
###################################################

#https://www.evernote.com/l/AMDbQLyGevtLBqglRXc15pqU8dZ87uYjLd0

def evernote_button_creator():
    #this function will turn an evernote web link into a desktop link
    #for use by a button
    new_evernote_web_link = input("Please paste the Evenote link (the 'Copy Note Link' option from a right-click on the desktop app): \n")
    the_evernote_web_link_parts = new_evernote_web_link.split("/")
    for i,item in enumerate(the_evernote_web_link_parts):
        if item == "":
            the_evernote_web_link_parts.remove(item)
        #i is here for fun, because I thought I might have needed it

    #building an evernote link to open the desktop a
    new_desktop_evernote_link = "evernote:///view/"+the_evernote_web_link_parts[5]+"/"+the_evernote_web_link_parts[3]+"/"+the_evernote_web_link_parts[6]+"/"+the_evernote_web_link_parts[6]+"/"
    webbrowser.open(new_desktop_evernote_link)

###################################################
###################################################

keepGoing = True
while keepGoing is True:

    #Previous Save Point#
    # runLink("")
    # link_layer()
    # main_buttons()
    
    keepGoing = False
