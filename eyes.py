import tkinter as tk
from time import sleep
import winsound
from pynput import mouse, keyboard

SLEEP_TIME = 5
REMIND_TITLE = "eyes"
REMIND_STRING = "You've been using the computer for 60 minutes, it's time to take a break"
ANSWER_STRING = "I got it"


def remind():
    win = tk.Tk()
    win.wm_attributes("-topmost", 1)  # means "Yes, do draw the window on top of all the others."
    winsound.PlaySound("preview.mp3", winsound.SND_ASYNC)
    win.title(REMIND_TITLE)
    win.main = tk.Label(win, text=REMIND_STRING, font=("微软雅黑", 15, "bold"))
    win.main.pack()
    answer_button = tk.Button(win, text=ANSWER_STRING, command=win.destroy)
    answer_button.pack()
    win.mainloop()


def delay_to_remind():
    while True:
        with keyboard.Events() as events:
            # Block at most 5 second
            event = events.get(5.0)
            if event is not None:
                continue
        with mouse.Events() as events:
            event = events.get(5.0)
            if isinstance(event, mouse.Events.Click):
                continue
        break


def main():
    while True:
        sleep(SLEEP_TIME)
        delay_to_remind()
        remind()


if __name__ == '__main__':
    main()
