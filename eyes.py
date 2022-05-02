#code by THGGDX
#version:v1.0
import tkinter as tk
from time import sleep
import winsound
def main():
    while True:
        sleep(1800)
        win=tk.Tk()
        win.wm_attributes("-topmost",1)
        winsound.PlaySound("preview.mp3",winsound.SND_ASYNC)
        win.title('护眼助手')
        win.main=tk.Label(win,text="你已经使用电脑30分钟了,休息一下吧",font=("微软雅黑",15,"bold"))
        win.main.pack()
        B = tk.Button(win,text="我知道了",command=win.destroy)
        B.pack()
        win.mainloop()
if __name__=='__main__':
    main()
