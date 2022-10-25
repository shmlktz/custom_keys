from tkinter import Tk, Button
#from tkinter.tix import WINDOW
import webbrowser
from functools import partial
import os
import string 
#from path.lib import Path
from os import path

#######################
## Next Up Priorities #
# 
# simple (as possible) on the fly add a button from an inputted link
##

# run a shortcut 'shortcuts://run-shortcut?name=[name]'
file_data =\
[
        ##WORKSTATIONS or WKSTNS##
    ['https://mail.google.com/mail/u/1/#inbox', 'voice.google.com',\
    'https://mail.google.com/mail/u/0/#inbox','https://mail.google.com/mail/u/2/#inbox',\
    'https://mail.google.com/mail/u/3/#inbox', 'https://mail.google.com/mail/u/4/#inbox',\
    'whatsapp://','Messages://','Telegram://'], #Communication

    ['authy://','evernote://','workflowy://','','','ical://'], #General HQ

    ['keybank.com','https://client.schwab.com/clientapps/accounts/summary/', 'bankofamerica.com', 'bankhapoalim.co.il',\
    'kucoin.com','coinbase.com','',\
    'https://wise.com/activity/',\
    '','',\
    'paypal.com','cashapp.com','','','','','','','','','',''], #Financial

    ['shortcuts://run-shortcut?name=ka_echsof'], #Good Music

    ['www.Calendly.com','https://app.clockify.me/tracker','www.bit.ly','https://prezi.com/'], #Independent Business Tools

    ['https://www.evernote.com/shard/s192/nl/21614375/3fff4f23-55bc-407a-87fa-6b1ffe2f70b8/'], #Noteboard, current quotes

    ['https://www.morfix.co.il/','http://www.kizur.co.il/home.php','https://forecast.israelinfo.co.il/kineret'\
    ,''\
    ,'https://www.myzmanim.com/day.aspx?askdefault=1&vars=27526341&q=jerusalem'\
    ,'https://www.myzmanim.com/day.aspx?askdefault=1&vars=72682081&q=indianapolis',\
    'https://www.halachipedia.com/index.php?title=Main_Page'], #Torah Tools

    ['https://www.educba.com/python-programming-beginners-tutorial/'\
    ,'https://towardsdatascience.com/how-to-read-and-understand-python-code-faster-180ba1ba9445'] #Continuing Education

]

    # ['https://www.youtube.com/watch?v=J1Nz-Sdah4k'\
    # ,'https://www.youtube.com/watch?v=fiHAVGjueac'\
    # ,'https://www.youtube.com/watch?v=aEsXmQXfQSM'],
    # ['GrandPerspective://','justWink://','shortcuts://run-shortcut?name=reveal_resume','ical://','workflowy://#/0b11ac922853','brave://','brave://flags','brave://local-state/'], #'brave://chrome-extension://chphlpgkkbolifaimnlloiipkdnihall/onetab.html'],
    # ['shortcuts://run-shortcut?name=Messages_Whatsapp','facetime://','https://mail.google.com/mail/u/1/#inbox','Telegram://','https://mail.google.com/mail/u/0/#inbox','zoommtg://'], #plus an additional many Google accounts, and even having buttons for different google suites of emails (various non for profit work related emails (sharing data and doing tasks)),
    # ['https://www.morfix.co.il/%D7%94%D7%9B%D7%A0%D7%A2%D7%94','http://www.kizur.co.il/home.php','https://doitinhebrew.com/','https://app.clockify.me/tracker','https://www.sefaria.org.il/texts'],
    # ['VSCode://'], #test
    # ['torah_anytime','educational_and\improvement_youtube', 'https://elevationproject.workplace.com/?medium=email&story_id=S%3A_I100033356432594%3A2822033558091011', 'R Carlebach Shiurim', 'https://www.torahdownloads.com/s-66-rabbi-noah-weinberg.html', 'overcast://','motivational youtube playlist',''], #media
    # [''], #financial [keybank, schwab, kucoin, cashapp, paypal, bank hapoalim, bank of america, ]
    # [''],
    # ['https://www.dropbox.com','https://www.drive.google.com'], #popup data mobile workstation (most likely not on desktop apps)
    # [''],
    # [''],
    # ]


    # ,'https://www.evernote.com/shard/s192/nl/21614375/3fff4f23-55bc-407a-87fa-6b1ffe2f70b8/', 'VISUAL STUDIO CODE', 'SYSTEM PREFERENCES', 'SHIFT', 'WHATSAPP', 'GMAIL', 'GDOCS','Hebrew_typing'\
    # ,'sefaria_n', 'havinenu', 'kinneret', 'work_gmail_suite', 'MyZmanim: Jerusalem', 'http://www.google.com','MyZmanim: Indianapolis', 'GVoice_Telephone'
    # ,'https://www.geeksforgeeks.org/enumerate-in-python/','GDRIVE', 'DROPBOX'\

    # ,'https://www.morfix.co.il/','http://www.kizur.co.il/home.php',''\
    # ,'https://www.educba.com/python-programming-beginners-tutorial/','https://towardsdatascience.com/how-to-read-and-understand-python-code-faster-180ba1ba9445','https://stackoverflow.com/questions/50752618/run-code-is-not-working-in-visual-studio-code'\
    # ,'','',''\
    # ]

#####
"""
turning this .py file into a desktop application

"""
#####
######
"""
making a directory of all the applications I find successful URL schemes to
for later user friendly use

Shazam: shazammac://
Overcast: overcast://
Zoom: zoommtg://
dictionary: dict://
calm: calm://
shortcuts: shortcuts://

"""
######
link_list_letters = []

for x in range(len(file_data)):
    link_list_letters.append(string.ascii_letters[x])


#Creating the GUI
root = Tk()


#drafting the code for the multiple link open (in one button press) attempt
#comments were used to debug to show how far along in the process we arrived to in the if then nestings
def link_opener(item):
    print('printing the item on the next line : ')
    print(item)
    print(type(item))
    if type(item) is list:
        print("made it to the 'if' section")  ##
        for thing in range(len(item)):
            print(item[thing]) ##
            webbrowser.open_new_tab(item[thing])
    else:
        print("made it to the 'else' section") ##
        print(item) ##
        webbrowser.open_new_tab(item)
        

#2 Creating the button layout
row = 0
col = 0
lll = len(file_data) #lll = length of link list

for index in range(lll):
    #print("printing through the index of the range in lll: " + str(file_data[index]))
    Button(root, text=f'Button {index + 1}', padx = 50, pady = 50, command = partial(link_opener, file_data[index]))\
        .grid(row=row, column=col) #   command=partial (link_opener, file_data[index]))\ #let us brainstorm what options we could **
    col += 1
    if col >= 5:
        col = 0
        row += 1

#binding keystrokes to a command
for i in range(len(link_list_letters)):
    root.bind(link_list_letters[i], partial(link_opener, file_data[i]))


#end of creation, running a mainloop to keep the GUI live
root.mainloop()

####WHY DOES THIS THROW AN ERROR? - very odd, but I'm probbaly just missing something small
# def main():
#     pass
# if __name__ == __main__:
#     main()

##Maybe the answer is here: https://stackoverflow.com/questions/21867009/nameerror-name-main-is-not-defined






###
#Notes on how the structure could look
# Aleph) open the GUI in the default state of ready
##Aleph Bet) open a new document and secure a strong understanding of 
##creating buttons and how to place them exactly where one intends to
##on a full blank GUI page. Understand how to segment buttons into sections
##this will be the creation of categories of buttons to group them

##Aleph Gimel) sync the size of the list to the letters to
## be bound to commands. See if there is an easy/smart way to 
## hold space for future letters and place a task there like 
## '"m" for messages or "w" for workflowy
## "e" for evernote
## "g" for gmail


# Bet) create an edit button where new buttons can be coded
    # For this round, the program will need to be reset for the
    # updated buttons to be live*. Adding buttons is as simple as
    # Adding a link to the list of links
    # *unless there is a way of resetting and rerunning
    # the mainloop w/o restart 
        # Bet Bet) for the link adder to convert web to desktop links
# Gimel) eventually allow for customization of the structure 
# of the buttons & organizing them by category
# (i.e. financial, social etc)
# refer to Aleph Bet above for how to improve skill to implement
###

#Creating the button layout#
# row = 0
# col = 0
# for index, link in enumerate(link_list[0]):
#     Button(root, text=f'Button {index + 1}', padx = 50, pady = 50, command=partial(webbrowser.open, link)).grid(row=row, column=col)
#     col += 1
#     if col >= 5:
#         col = 0
#         row += 1


###
##


###Additional list items for the file_data list

# https://www.yad2.co.il/products/furniture?category=2&info=%D7%A1%D7%A4%D7%AA%20%D7%A7%D7%98%D7%9F
# https://www.yad2.co.il/products/furniture?category=2&info=%D7%A4%D7%95%D7%98%D7%95%D7%9F&page=2
# https://www.facebook.com/marketplace/jerusalem/search?query=sofas
# https://www.facebook.com/marketplace/jerusalem/search?query=phone%20stand%20tripod

#     ,'','','','',''\
#     ,'','','','',''\
#     ,'','','','',''\
#     ,'','','','',''\

#     '', '', '', '', '', '', '', '', '', '', '', '', ''\
#     '', '', '', '', '', '', '', '', '', '', '', '', ''\
#     '', '', '', '', '', '', '', '', '', '', '', '', ''\
#     '', '', '', '', '', '', '', '', '', '', '', '', ''\
#     '', '', '', '', '', '', '', '', '', '', '', '', ''\

# ]




###THE ORIGINAL WRITE TO FILE:
###ckdata.write("link_list = ['evernote:///view/21614375/s192/10b4247b-5f09-4b66-953d-02e5f27aac3c/10b4247b-5f09-4b66-953d-02e5f27aac3c/',\
#### 'Anaconda-Navigator://', 'zoom.us://', 'Evernote://', 'Messages://',\
#### 'https://open.spotify.com/track/2gI9RfuSwulsBujm7hbOFv?si=891addaca9524eaf',\
#### 'spotify://', 'workflowy://', 'brave_browser://', 'https://www.evernote.com/l/AMBXt1MmUlhK6ojyRfy-smKu-InjsFwnoc0']\
#### \nlink_list_letters = ['a','b','c','d','e','f','g','h','i','j']")


#### Multiple URL List
# https://www.youtube.com/results?search_query=algorithms+overview+
# https://app.clockify.me/reports/summary?start=2022-05-16T00:00:00.000Z&end=2022-05-29T23:59:59.999Z&filterValuesData=%7B%22projects%22:%5B%226283aafeeee2025f761eeb10%22%5D%7D&filterOptions=%7B%22projects%22:%7B%22status%22:%22ACTIVE%22%7D%7D
# https://drive.google.com/drive/my-drive
# https://zapier.com/app/zaps
# https://duckduckgo.com/?q=al+haniach+dayti&t=brave&ia=web

###URL examples & info from first first draft
# https://open.spotify.com/track/2gI9RfuSwulsBujm7hbOFv?si=891addaca9524eaf & spotify://
# evernote:///view/21614375/s192/10b4247b-5f09-4b66-953d-02e5f27aac3c/10b4247b-5f09-4b66-953d-02e5f27aac3c/ & https://www.evernote.com/l/AMBXt1MmUlhK6ojyRfy-smKu-InjsFwnoc0
#
#
#

def evernoteConverter(evernote_link):
    #this is converting a standard internet evernote link
    #to a Mac desktop compatible link
    parts = evernote_link.split("/")
    first_number = parts[6]
    second_number = parts[4]
    third_number = parts[7]
    desktop_link = "evernote:///view/" +first_number+"/" + second_number+"/" + third_number+"/" + third_number+"/"
    #https://www.evernote.com/l/AMAM-FUeDG9HUar5qH_tvmw2tnvZBf_ct8Q
    #https://www.evernote.com/shard/s192/nl/21614375/0cf8551e-0c6f-4751-aaf9-a87fedbe6c36/
    return desktop_link


####################
"""Pseudo code on file_data
I'd simply like to be able to "pack away" "solutions" of applications and internet browser windows

solutions:
א. General Driver
Central: Daily Computer Tasks that are simple one application in nature
['Authy://', 'ical://','WorkFlowy://','LastPass://']

Flanks:
-Torah + Learning Tools(Sefaria, kitzur.co.il) & A Task Timer
['https://www.morfix.co.il/%D7%94%D7%9B%D7%A0%D7%A2%D7%94','http://www.kizur.co.il/home.php','https://doitinhebrew.com/','https://app.clockify.me/tracker','https://www.sefaria.org.il/texts']

-A Task Timer & Programming Window open
['https://app.clockify.me/tracker','Visual Studio Code://','','']

ב. 
ג. Communication Station: iMessage, Whatsapp, emails (s), Telegram
['Messages://','Whatsapp://','Telegram://','facetime://','https://mail.google.com/mail/u/1/#inbox','https://mail.google.com/mail/u/0/#inbox']

ד. 
good music for study/general:
['https://shevetachim.bandcamp.com/album/5-jewish-marriage-melodies', 'overcast://']

"""
####################