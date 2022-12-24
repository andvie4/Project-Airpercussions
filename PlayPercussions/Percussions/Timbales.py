import threading
import time
import tkinter
from tkinter import *
import customtkinter
import pygame
from PlayPercussions.Sounds.SoundList import soundlist_timbales
from depthai_hand_tracker.demo import coord

stop_thread = False

debounce = True


# import tk
# from PIL import Image, ImageTk


def create_timbales():
    win1 = Toplevel()  # must be Tk() instead of Toplevel(); TK() overwrites the Camera Picture
    win1.attributes('-fullscreen', True)
    # win1.geometry('1600x500')

    timbales = Canvas(win1)

    timbales.pack(fill=tkinter.BOTH, expand=True)
    # img = ImageTk.PhotoImage(file='')
    # timbales.create_image(0, 0, image=img, anchor=NW)

    screen_width_middle = win1.winfo_screenwidth() / 2
    screen_height_middle = win1.winfo_screenheight() / 2

    # create timbales holder
    timbales.create_line(screen_width_middle, screen_height_middle - 400, screen_width_middle,
                         screen_height_middle + 400,
                         width=8)
    timbales.create_line(screen_width_middle, screen_height_middle + 200, screen_width_middle - 150,
                         screen_height_middle + 350,
                         width=8)
    timbales.create_line(screen_width_middle, screen_height_middle + 200, screen_width_middle + 150,
                         screen_height_middle + 350,
                         width=8)
    timbales.create_line(screen_width_middle - 100, screen_height_middle - 20, screen_width_middle + 100,
                         screen_height_middle - 20,
                         width=12)

    # create Macho
    timbales.create_rectangle(screen_width_middle - 300, screen_height_middle - 75, screen_width_middle - 100,
                              screen_height_middle + 80, fill='#ffd700', outline='')
    timbales.create_oval(screen_width_middle - 300, screen_height_middle - 150, screen_width_middle - 100,
                         screen_height_middle,
                         width=3, fill='white')
    macho = timbales.create_oval(screen_width_middle - 295, screen_height_middle - 145, screen_width_middle - 105,
                                 screen_height_middle - 5,
                                 width=3, activeoutline='red')
    timbales.create_arc(screen_width_middle - 300, screen_height_middle + 50, screen_width_middle - 102,
                        screen_height_middle + 110, start=180, extent=180, fill="#ffd700", outline="")

    # style Macho
    timbales.create_arc(screen_width_middle - 300, screen_height_middle + 30, screen_width_middle - 102,
                        screen_height_middle + 80, start=180, extent=180, outline="#D4AF37", width=5, style=ARC)
    timbales.create_arc(screen_width_middle - 300, screen_height_middle + 50, screen_width_middle - 102,
                        screen_height_middle, start=180, extent=180, outline="#D4AF37", width=5, style=ARC)

    # create Hembra
    timbales.create_rectangle(screen_width_middle + 100, screen_height_middle - 75, screen_width_middle + 330,
                              screen_height_middle + 80, fill='#ffd700', outline='')
    timbales.create_oval(screen_width_middle + 330, screen_height_middle - 150, screen_width_middle + 100,
                         screen_height_middle,
                         width=3, fill='white')
    hembro = timbales.create_oval(screen_width_middle + 325, screen_height_middle - 145, screen_width_middle + 105,
                                  screen_height_middle - 5,
                                  width=3, activeoutline='red', tags=('hembro1', 'hembro2'))
    timbales.create_arc(screen_width_middle + 100, screen_height_middle + 50, screen_width_middle + 328,
                        screen_height_middle + 110, start=180, extent=180, fill="#ffd700", outline="")
    # style Hembra

    timbales.create_arc(screen_width_middle + 100, screen_height_middle + 30, screen_width_middle + 330,
                        screen_height_middle + 80, start=180, extent=180, outline="#D4AF37", width=5, style=ARC)
    timbales.create_arc(screen_width_middle + 100, screen_height_middle + 50, screen_width_middle + 330,
                        screen_height_middle, start=180, extent=180, outline="#D4AF37", width=5, style=ARC)

    # create Cowbell

    cowbell = timbales.create_polygon(screen_width_middle - 80, screen_height_middle - 350, screen_width_middle - 90,
                                      screen_height_middle - 320,
                                      screen_width_middle - 88, screen_height_middle - 280, screen_width_middle + 33,
                                      screen_height_middle - 310,
                                      screen_width_middle + 33, screen_height_middle - 320, screen_width_middle + 33,
                                      screen_height_middle - 320,
                                      screen_width_middle + 35, screen_height_middle - 330,
                                      fill='#cfd0cf', outline='black', width=3)
    timbales.create_line(screen_width_middle - 90, screen_height_middle - 320, screen_width_middle + 33,
                         screen_height_middle - 320)
    button_close = customtkinter.CTkButton(master=win1, text='Close', fg_color='#cf5148', hover_color="red",
                                           command=back)
    button_close.place(relx=0.92, rely=0.95, relwidth=0.13, relheight=0.06, anchor=CENTER)

    pygame.init()

    def playback_timbales(channel, index):
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(soundlist_timbales[index]))

    def play_timbales():
        channel = 1
        end = 0
        global stop_thread, debounce

        while True:  # if the close button is pressed, the back function is called and set  stop_thread to True
            if stop_thread:
                print('thread gestoppt')
                stop_thread = False
                win1.withdraw()
                break
            x1 = coord[0]
            y1 = coord[1]
            z1 = coord[2]
            x2 = coord[3]
            y2 = coord[4]
            z2 = coord[5]

            start = z1
            delta = end - start

            if 800 > x1 > 5 and y1 < 500:
                timbales.itemconfig(hembro, fill='red')
                if delta > 4 and not debounce:
                    playback_timbales(channel, 0)
                    channel += 1
                    debounce = True
            else:
                timbales.itemconfig(hembro, fill='#d9d4d0')
            if x1 > 800 and y1 < 500:
                timbales.itemconfig(macho, fill='red')
                if delta > 4 and not debounce:
                    playback_timbales(channel, 1)
                    channel += 1
                    debounce = True
            else:
                timbales.itemconfig(macho, fill='#d9d4d0')

            if y1 > 500:
                timbales.itemconfig(cowbell, fill='red')
                if delta > 4 and not debounce:
                    playback_timbales(channel, 2)
                    channel += 1
                    debounce = True
            else:
                timbales.itemconfig(cowbell, fill='#d9d4d0')

            if channel == 8:
                channel = 1

            if delta < 0:
                debounce = False
            time.sleep(0.01)
            end = z1

    thread_playtimb = threading.Thread(target=play_timbales)
    thread_playtimb.start()

    win1.mainloop()


def back():
    print('Button gedrückt')
    global stop_thread
    stop_thread = True
