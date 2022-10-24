##EverNote regular link to Desktop Link converter

def evernoteConverter(evernote_link):
    #this is converting a standard internet evernote link
    #to a desktop compatible link
    parts = evernote_link.split("/")
    first_number = parts[6]
    second_number = parts[4]
    third_number = parts[7]
    desktop_link = "evernote:///view/" +first_number+"/"\
+ second_number+"/" + third_number+"/" + third_number+"/"
    return desktop_link

print(evernoteConverter("https://www.evernote.com/shard/s192/nl/21614375/10b4247b-5f09-4b66-953d-02e5f27aac3c/"))