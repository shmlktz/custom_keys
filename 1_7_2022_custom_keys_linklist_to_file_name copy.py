from tkinter import Tk, Button
from tkinter.tix import WINDOW
import webbrowser
from functools import partial
import os
import string
#from path.lib import Path
from os import path

file_data = [['https://open.spotify.com/track/2gI9RfuSwulsBujm7hbOFv?si=891addaca9524eaf', 'evernote:///view/21614375/s192/10b4247b-5f09-4b66-953d-02e5f27aac3c/10b4247b-5f09-4b66-953d-02e5f27aac3c/'], 'Anaconda-Navigator://', 'zoom.us://', 'Evernote://','Whatsapp://' \
    ,'https://open.spotify.com/track/2gI9RfuSwulsBujm7hbOFv?si=891addaca9524eaf','spotify://', 'workflowy://','Messages://' , 'https://www.evernote.com/l/AMBXt1MmUlhK6ojyRfy-smKu-InjsFwnoc0'\

    ,'https://www.evernote.com/shard/s192/nl/21614375/3fff4f23-55bc-407a-87fa-6b1ffe2f70b8/', 'VISUAL STUDIO CODE', 'SYSTEM PREFERENCES', 'SHIFT', 'WHATSAPP', 'GMAIL', 'GDOCS','Hebrew_typing'\
    ,'sefaria_n', 'havinenu', 'kinneret', 'work_gmail_suite', 'MyZmanim: Jerusalem', 'http://www.google.com','MyZmanim: Indianapolis', 'GVoice_Telephone'
    ,'https://www.geeksforgeeks.org/enumerate-in-python/','GDRIVE', 'DROPBOX'\

    ,'https://www.morfix.co.il/','http://www.kizur.co.il/home.php',''\
    ,'https://www.educba.com/python-programming-beginners-tutorial/','https://towardsdatascience.com/how-to-read-and-understand-python-code-faster-180ba1ba9445','https://stackoverflow.com/questions/50752618/run-code-is-not-working-in-visual-studio-code'\
    ,'','',''\
    ]


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

#not currently in use but here
link_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'\
                ,'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg']


print('this is the file_data list:',file_data)


# link_list = []
# for i in range(len(file_data)):
#     link_list.append(file_data[i]) #.translate(str.maketrans({"'":None}))
# print('this is the link_list list:',link_list)

link_list_letters = []

for x in range(len(file_data)):
    link_list_letters.append(string.ascii_letters[x])

# print("link list:",type(link_list),"\n",link_list)

# print("link list letters:",type(link_list_letters),"\n",link_list_letters)

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

#Creating the GUI
root = Tk()

###
#Notes on how the structure will look
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
#drafting the code for the multiple link open (in one button press) attempt
def link_opener(item):
    if type(item) is list:
        for thing in range(len(item)):
            webbrowser.open(thing)
#
##
###


#2 Creating the button layout
row = 0
col = 0
lll = len(file_data) #lll = length of link list
print(lll)
for index in range(lll):
    Button(root, text=f'Button {index + 1}', padx = 50, pady = 50, command=partial(webbrowser.open, file_data[index]))\
        .grid(row=row, column=col)
    col += 1
    if col >= 5:
        col = 0
        row += 1


#binding keystrokes to a command
for i in range(len(link_list_letters)):
    root.bind(link_list_letters[i], partial(webbrowser.open, file_data[i]))


#end of creation, running a mainloop to keep the GUI live
root.mainloop()

def main():
    pass
if __name__ == __main__:
    main()



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