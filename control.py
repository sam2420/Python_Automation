import ctypes
import time
from pynput.keyboard import Controller, Key

SendInput = ctypes.windll.user32.SendInput

asa = Controller()


def PressKey(hexKeyCode):
    asa.press(hexKeyCode)


def ReleaseKey(hexKeyCode):
    asa.release(hexKeyCode)


if __name__ == '__main__':
    while (True):
        PressKey(0x11)
        time.sleep(1)
        ReleaseKey(0x11)
        time.sleep(1)
