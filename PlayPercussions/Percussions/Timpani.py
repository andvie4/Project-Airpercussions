import threading
import time
import tkinter
from tkinter import *
import customtkinter
import pygame
from PlayPercussions.Sounds.SoundList import soundlist_timpani
from depthai_hand_tracker.demo import coord

stop_thread_timpani = False
debounce = True


def create_timpani():
    win4 = Toplevel()
    win4.attributes('-fullscreen', True)
    #win4.geometry('1000x700')

    timpani_low = Canvas(win4)
    timpani_low.place(relx=0.25, rely=0.5, relwidth=0.49, relheight=0.9, anchor=CENTER)

    timpani_high = Canvas(win4)
    timpani_high.place(relx=0.75, rely=0.5, relwidth=0.49, relheight=0.9, anchor=CENTER)
    timpani_low.update()
    a = timpani_low.winfo_width()
    b = timpani_low.winfo_height()

    timpani_low.create_arc(120, 40, 840, 840, start=180, extent=180, style=tkinter.CHORD, fill='#bf8970')
    timpani_low.create_oval(100, 100, a - 90, b - 320, fill='#96410b')
    lowtimp = timpani_low.create_oval(110, 110, a - 100, b - 340, fill='#e0cdbc', width=5)
    timpani_low.create_line(300, 783, 220, 950, width=10)
    timpani_low.create_line(670, 780, 750, 950, width=10)
    timpani_low.create_line(330, 800, 310, 880, width=10)
    timpani_low.create_line(640, 795, 660, 880, width=10)

    timpani_high.create_arc(125, 40, 785, 800, start=180, extent=180, style=tkinter.CHORD, fill='#bf8970')
    timpani_high.create_oval(110, 100, a - 140, b - 330, fill='#96410b')
    highttimp = timpani_high.create_oval(120, 110, a - 150, b - 345, fill='#e0cdbc', width=5)
    timpani_high.create_line(280, 740, 200, 900, width=10)
    timpani_high.create_line(630, 740, 730, 900, width=10)
    timpani_high.create_line(310, 760, 290, 825, width=10)
    timpani_high.create_line(600, 760, 620, 825, width=10)

    button_close = customtkinter.CTkButton(master=win4, text='Close', fg_color='#cf5148', hover_color="red",
                                           command=back)
    button_close.place(relx=0.92, rely=0.95, relwidth=0.13, relheight=0.06, anchor=CENTER)

    pygame.init()

    def playback_timpani(channel, index):
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(soundlist_timpani[index]))

    def play_timpani():
        end =0
        channel = 1

        global stop_thread_timpani, debounce

        while True:  # if the close button is pressed, the back function is called and set  stop_thread to True
            if stop_thread_timpani:
                print('thread gestoppt')
                stop_thread_timpani = False
                win4.withdraw()
                break
            x1 = coord[0]
            y1 = coord[1]
            z1 = coord[2]
            x2 = coord[3]
            y2 = coord[4]
            z2 = coord[5]

            start = z1
            delta = end - start

            if 800 > x1 > 5:
                timpani_high.itemconfig(highttimp, fill='red')
                if delta > 4 and not debounce:
                    playback_timpani(channel, 0)
                    channel += 1

                    debounce = True
            else:
                timpani_high.itemconfig(highttimp, fill='#e0cdbc')
            if x1 > 800:
                timpani_low.itemconfig(lowtimp, fill='red')
                if delta > 4 and not debounce:
                    playback_timpani(channel, 1)
                    channel += 1
                    debounce = True
            else:
                timpani_low.itemconfig(lowtimp, fill='#d9d4d0')
            if channel == 8:
                channel = 1

            if delta < 0:
                debounce = False
            time.sleep(0.01)
            end = z1

    thread_playtimpani = threading.Thread(target=play_timpani)
    thread_playtimpani.start()

    win4.mainloop()


def back():
    print('Button gedrückt')
    global stop_thread_timpani
    stop_thread_timpani = True
