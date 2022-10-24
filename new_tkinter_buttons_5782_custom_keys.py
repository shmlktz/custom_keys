from tkinter import Tk, Button
import webbrowser
from functools import partial

link = 'evernote:///view/21614375/s192/10b4247b-5f09-4b66-953d-02e5f27aac3c/10b4247b-5f09-4b66-953d-02e5f27aac3c/'
root = Tk()

#this = Button(root, text=f'Button', padx = 50, pady = 50, command=partial(webbrowser.open, link)).grid()
root.bind('l', partial(webbrowser.open, link))

root.mainloop()