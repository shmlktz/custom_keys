from tkinter import Tk, Button
import webbrowser
from functools import partial

link_list = ['evernote:///view/21614375/s192/10b4247b-5f09-4b66-953d-02e5f27aac3c/10b4247b-5f09-4b66-953d-02e5f27aac3c/',
             'Anaconda-Navigator://', 'zoom.us://', 'Evernote://', 'Messages://',
             'https://open.spotify.com/track/2gI9RfuSwulsBujm7hbOFv?si=891addaca9524eaf',
             'spotify://', 'workflowy://', 'brave_browser://', 'https://www.evernote.com/l/AMBXt1MmUlhK6ojyRfy-smKu-InjsFwnoc0']
link_list_letters = ['a','b','c','d','e','f',\
'g','h','i','j']


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

root = Tk()

row = 0
col = 0
for index, link in enumerate(link_list):
    Button(root, text=f'Button {index + 1}', padx = 50, pady = 50, command=partial(webbrowser.open, link)).grid(row=row, column=col)
    col += 1
    if col >= 3:
        col = 0
        row += 1

for i in range(len(link_list)):
    root.bind(link_list_letters[i], partial(webbrowser.open, link_list[i]))

root.mainloop()