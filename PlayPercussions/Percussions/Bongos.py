import threading
import time
import tkinter
from tkinter import *

import customtkinter
import pygame
from PlayPercussions.Sounds.SoundList import soundlist_bongos

from depthai_hand_tracker.demo import coord, close_depth_camera
from depthai_hand_tracker.mouse import handmouse

stop_thread_bongo = False
a = 0
b = 0


def create_bongos():
    print('Hallo')

    win2 = Toplevel()
    win2.attributes('-fullscreen', True)
   # win2.geometry('1700x800')

    bongos_high = Canvas(win2)
    bongos_high.place(relx=0.25, rely=0.5, relwidth=0.49, relheight=0.9, anchor=CENTER)

    bongos_low = Canvas(win2)
    bongos_low.place(relx=0.75, rely=0.5, relwidth=0.49, relheight=0.9, anchor=CENTER)
    bongos_low.update()
    a = bongos_low.winfo_width()
    b = bongos_low.winfo_height()

    # bongos_high.create_rectangle(100,450,650,750,fill='#c4b98f')
    bongos_high.create_oval(50, 50, a - 50, b - 200, fill='#4f2813')
    bongos_high.create_oval(70, 50, a - 70, b - 260, fill='#f5f7f0')
    bg_high = bongos_high.create_oval(100, 50, a - 110, b - 350, fill='#e0cdbc', width=5)

    bongos_low.create_oval(50, 50, a - 50, b - 100, fill='#4f2813')
    bongos_low.create_oval(70, 50, a - 70, b - 170, fill='#f5f7f0')
    bg_low = bongos_low.create_oval(100, 50, a - 110, b - 250, fill='#e0cdbc', width=5)

    button_close = customtkinter.CTkButton(master=win2, text='Close', fg_color='#cf5148', hover_color="red",
                                           command=back)
    button_close.place(relx=0.92, rely=0.95, relwidth=0.13, relheight=0.06, anchor=CENTER)
    pygame.init()

    def playback_bongo(channel, index):
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(soundlist_bongos[index]))

    def play_bongo():
        debounce = True
        channel = 1
        global stop_thread_bongo

        while True:  # if the close button is pressed, the back function is called and set  stop_thread to True
            st = time.time()
            global a, b

            if stop_thread_bongo:
                print('thread gestoppt')
                stop_thread_bongo = False
                close_depth_camera(1)
                thread = threading.Thread(target=handmouse)
                thread.start()

                # win2.destroy()
                win2.withdraw()
                break
            x1 = coord[0]
            y1 = coord[1]
            z1 = coord[2]
            x2 = coord[3]
            y2 = coord[4]
            z2 = coord[5]

            a = z1
            delta = b - a
            print(delta)

            if 900 > x1 > 5:
                bongos_low.itemconfig(bg_low, fill='red')
                if delta > 4 and not debounce:
                    playback_bongo(channel, 0)
                    channel += 1
                    if channel == 8:
                        channel = 1
                    debounce = True
            else:
                bongos_low.itemconfig(bg_low, fill='#e0cdbc')
            if x1 > 900:
                bongos_high.itemconfig(bg_high, fill='red')
                if delta > 3 and not debounce:
                    playback_bongo(channel, 1)
                    channel += 1
                    if channel == 8:
                        channel = 1
                    debounce = True
            else:
                bongos_high.itemconfig(bg_high, fill='#d9d4d0')

            if delta < 0:
                debounce = False
            time.sleep(0.01)

            b = z1

            time.sleep(0.01)

    thread_bongo = threading.Thread(target=play_bongo)
    thread_bongo.start()

    win2.mainloop()


def back():
    print('Button gedrückt')
    global stop_thread_bongo
    stop_thread_bongo = True


# A useful function to create a circle. Just for trying out. Not used here!
def create_circle(x, y, r, canvasName):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)
