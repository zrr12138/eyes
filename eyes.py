import subprocess
import tkinter as tk
from time import sleep

import logging
import logging.handlers
import winsound
from pynput import mouse, keyboard

SLEEP_TIME = 5
REMIND_TITLE = "eyes"
REMIND_STRING = "You've been using the computer for 60 minutes, it's time to take a break"
ANSWER_STRING = "I got it"
DELAY_TIME = 5.0
CHECK_TEST_INTERVAL = 60  # Should not be too large, otherwise it will consume too much cpu resources
LOG_FILE_NAME = "eyes.log"
MAX_LOG_FILE_SIZE = 1024*1024*1024  # bytes
logger = logging.getLogger(__name__)


def is_windows_locked():
    if 'LogonUI.exe' in str(subprocess.check_output('TASKLIST')):
        return True
    else:
        return False


def remind():
    logger.info("remind")
    win = tk.Tk()
    win.wm_attributes("-topmost", 1)  # means "Yes, do draw the window on top of all the others."
    winsound.PlaySound("preview.mp3", winsound.SND_ASYNC)
    win.title(REMIND_TITLE)
    win.main = tk.Label(win, text=REMIND_STRING, font=("微软雅黑", 15, "bold"))
    win.main.pack()
    answer_button = tk.Button(win, text=ANSWER_STRING, command=win.destroy)
    answer_button.pack()
    win.mainloop()
    logger.info("remain over")


def delay_to_remind():
    while True:
        with keyboard.Events() as events:
            # Block at most 5 second
            event = events.get(DELAY_TIME)
            if event is not None:
                logger.debug('there is a keyboard event,delay {} s'.format(DELAY_TIME))
                continue
        with mouse.Events() as events:
            event = events.get(DELAY_TIME)
            if isinstance(event, mouse.Events.Click):
                logger.debug('there is a mouse click event,delay {} s'.format(DELAY_TIME))
                continue
        logger.info("delay_to_remind finish")
        break


def sleep_loop(total_time: int):
    logger.info("start sleep loop , total time = {}".format(total_time))
    while total_time > CHECK_TEST_INTERVAL:  # Check if windows is locked every 20 seconds
        sleep(CHECK_TEST_INTERVAL)
        if is_windows_locked():
            logger.debug("windows is locked")
            continue
        else:
            total_time -= CHECK_TEST_INTERVAL
    sleep(total_time)
    logger.info("end sleep loop")


def main():
    logger.info("eyes start")
    while True:
        sleep_loop(SLEEP_TIME)
        delay_to_remind()
        remind()


def log_init():
    logger.setLevel(logging.DEBUG)
    rfh = logging.handlers.RotatingFileHandler(LOG_FILE_NAME, maxBytes=MAX_LOG_FILE_SIZE, backupCount=1,
                                               encoding="utf-8")
    rfh.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s")
    rfh.setFormatter(formatter)
    logger.addHandler(rfh)


if __name__ == '__main__':
    log_init()
    main()
