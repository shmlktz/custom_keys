# Custom Keys

## A project to improve workflows
This application is a workstation creator & operates by deploying multiple items (could be any number of applications, webpages, or both) from a single click of a button.
These multiple items grouped together form a workstation.

## Organization of the application
The data is organized in a Python list, which has in it lists of links (each list of links being the components of a workstation).
Each list of links (nested in the main list), is represented on the application as a button created by the GUI.
When the button is pressed, all of the links associated with the button will open.
*(I created this with the intention of opening 
URL scheme links to open desktop applications as well as web links.
I presume there are many other use cases for this program, and I would love to hear your use cases & ideas)*

## The concept:
Group items together in a logical manner, so when they are
all opened at once would create a workstation
to save precious time. For example, one could open
all of their communication channels (multiple email accounts, slack,
messaging platforms, etc) or financial platforms (banks, investment accounts,
payment apps, etc) in one click on the custom_keys application.

## Requirements:
1. Python  
  
2. Python libraries:
  - tkinter
  - webbrowser
  - functools
  - os
  - string
