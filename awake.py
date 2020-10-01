#!/usr/bin/env python3
import datetime
import random
import time

import pyautogui

from tkinter import Tk


CHECK_STATUS_ONCE_IN = 60
WAIT_FOR_POSITION_CHANGE = 30


def current_position():
    tkinter = Tk()
    return [tkinter.winfo_pointerx(), tkinter.winfo_pointery()]


def mouse_is_moving():
    pos1 = current_position()
    time.sleep(WAIT_FOR_POSITION_CHANGE)
    pos2 = current_position()
    return not pos1 == pos2


def keep_awake():
    # Shake the mouse a lil bit
    try:
        for execution in range(random.randint(1, 10)):
            pyautogui.moveTo(random.randint(1, 1000), random.randint(1, 1000))
    except pyautogui.FailSafeException as e:
        print(e)

def inspect_activity_until(hour: int):
    while datetime.datetime.now().hour < hour:
        if not mouse_is_moving():
            keep_awake()
        time.sleep(CHECK_STATUS_ONCE_IN)

    print(f"Stopping at {datetime.datetime.now()}")


if __name__ == "__main__":
    inspect_activity_until(22)
