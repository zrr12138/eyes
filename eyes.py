import tkinter as tk
from time import sleep
import winsound, logging
from pynput import mouse, keyboard

SLEEP_TIME = 5
REMIND_TITLE = "eyes"
REMIND_STRING = "You've been using the computer for 60 minutes, it's time to take a break"
ANSWER_STRING = "I got it"
DELAY_TIME = 5.0


def remind():
    logging.info("remind")
    win = tk.Tk()
    win.wm_attributes("-topmost", 1)  # means "Yes, do draw the window on top of all the others."
    winsound.PlaySound("preview.mp3", winsound.SND_ASYNC)
    win.title(REMIND_TITLE)
    win.main = tk.Label(win, text=REMIND_STRING, font=("微软雅黑", 15, "bold"))
    win.main.pack()
    answer_button = tk.Button(win, text=ANSWER_STRING, command=win.destroy)
    answer_button.pack()
    win.mainloop()
    logging.info("remain over")


def delay_to_remind():
    while True:
        with keyboard.Events() as events:
            # Block at most 5 second
            event = events.get(DELAY_TIME)
            if event is not None:
                logging.debug('there is a keyboard event,delay {} s'.format(DELAY_TIME))
                continue
        with mouse.Events() as events:
            event = events.get(DELAY_TIME)
            if isinstance(event, mouse.Events.Click):
                logging.debug('there is a mouse click event,delay {} s'.format(DELAY_TIME))
                continue
        logging.info("delay_to_remind finish")
        break


def main():
    logging.info("eyes start")
    while True:
        logging.info("start sleep")
        sleep(SLEEP_TIME)
        logging.info("sleep finish")
        delay_to_remind()
        remind()


if __name__ == '__main__':
    logging.basicConfig(format="%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s", filename='eyes.log',
                        encoding='utf-8', level=logging.DEBUG)
    main()
