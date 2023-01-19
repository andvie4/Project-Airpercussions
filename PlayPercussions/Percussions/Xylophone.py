import threading
import time
import tkinter
from tkinter import *
import customtkinter
import pygame
from PlayPercussions.Sounds.SoundList import soundlist_xylo, soundlist_xylo_accidental

from depthai_hand_tracker.demo import coord, close_depth_camera
from depthai_hand_tracker.mouse import handmouse

note_name = ['f', 'g', 'a', 'h', 'c1', 'd1', 'e1', 'f1', 'g1', 'a1', 'h1', 'c2', 'd2', 'e2', 'f2', 'g2', 'a2', 'h2',
             'c3', 'd3', 'e3', 'f3']
accidental_notenames_sharpsign = ['fis', 'gis', 'ais', 'cis', 'dis', 'fis', 'gis', 'ais', 'cis', 'dis', 'fis',
                                  'gis', 'ais', 'cis', 'dis']
accidental_notenames_bsign = ['ges', 'as', 'b', 'des', 'es', 'ges', 'as', 'b', 'des', 'es', 'ges', 'as', 'b', 'des',
                              'es']

rectangle_index1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
                    '16', '17', '18', '19', '20', '21']
rectangle_index2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
playback_index = 0
stop_thread_xylo = False
start = 0
end = 0
coord[6]=10
pygame.init()
pygame.mixer.set_num_channels(30)


def create_xylophone():
    win3 = Toplevel()
    win3.attributes('-fullscreen', True)
    # win3.geometry('1500x700')

    x1 = 40
    y1 = 1045
    x2 = 119
    y2 = 545
    x3 = 70
    y3 = 540
    x4 = 149
    y4 = 40

    # x1 = 40
    # y1 = 840
    # x2 = 100
    # y2 = 440
    # x3 = 70
    # y3 = 435
    # x4 = 130
    # y4 = 35

    xylophone = Canvas(win3)
    xylophone.pack(fill=tkinter.BOTH, expand=True)

    for i in range(0, 22):
        rectangle_index1[i] = xylophone.create_rectangle(x1, y1, x2, y2, fill='#754C14', width=5)
        xylophone.create_text(x1 + 30, y1 - 15, text=note_name[i], font='Helvetica 15 bold')
        x1 += 81
        x2 += 81
        y1 -= 6
        y2 += 6
    for y in range(0, 15):
        rectangle_index2[y] = xylophone.create_rectangle(x3, y3, x4, y4, fill='#754C14', width=5)
        xylophone.create_text(x3 + 30, y3 - 30, text=accidental_notenames_sharpsign[y], font='Helvetica 15 bold')
        xylophone.create_text(x3 + 30, y3 - 15, text=accidental_notenames_bsign[y], font='Helvetica 15 bold')

        x3 += 81
        x4 += 81
        y3 += 6
        y4 += 18
        if y == 2 or y == 4 or y == 7 or y == 9 or y == 12:  # for the bigger space between
            x3 += 81
            x4 += 81
            y3 += 6
            y4 += 18
    button_close = customtkinter.CTkButton(master=win3, text='Close', fg_color='#cf5148', hover_color="red",
                                           command=back)
    button_close.place(relx=0.92, rely=0.95, relwidth=0.13, relheight=0.06, anchor=CENTER)

    thread_xylo = threading.Thread(target=play_xylo, args=(win3, xylophone, rectangle_index1, rectangle_index2))
    thread_xylo.start()

    win3.mainloop()


def playback_xylophon(channel, index):
    pygame.mixer.Channel(channel).play(pygame.mixer.Sound(soundlist_xylo[index]))


def playback_accidental_notes(channel, index):
    pygame.mixer.Channel(channel).play(pygame.mixer.Sound(soundlist_xylo_accidental[index]))


def play_xylo(win, xylophone, rectangles1, rectangles2):
    debounce = False
    config = False
    channel = 1
    while True:
        global stop_thread_xylo, end
        if stop_thread_xylo:
            print('thread gestoppt')
            stop_thread_xylo = False
            close_depth_camera(1)
            thread = threading.Thread(target=handmouse)
            thread.start()
            win.withdraw()
            break

        x1 = coord[0]
        y1 = coord[1]
        z1 = coord[2]
        x2 = coord[3]
        y2 = coord[4]
        z2 = coord[5]
        distance = coord[6]
        start = z1
        delta = end - start

        if distance == 0:
            stop_thread_xylo = True

        if y1 < 450:
            if config:
                for x in range(15):
                    xylophone.itemconfig(rectangles2[x], fill='#754C14')
                    config = False
            idx = check_index1(x1)

            if idx is not None:
                idx = 21 - idx
            for number in range(22):
                if idx == number:
                    xylophone.itemconfig(rectangles1[number], fill='red')
                    if delta > 2 and not debounce:
                        playback_xylophon(channel, idx)
                        channel += 1
                        debounce = True
                    config = True
                else:
                    xylophone.itemconfig(rectangles1[number], fill='#754C14')

        if y1 > 450:
            if config:
                for x in range(22):
                    xylophone.itemconfig(rectangles1[x], fill='#754C14')
                    config = False
            idx2 = check_index2(x1)
            if idx2 is not None:
                idx2 = 14 - idx2
            for number in range(15):
                if idx2 == number:
                    xylophone.itemconfig(rectangles2[number], fill='red')
                    if delta > 2 and not debounce:
                        playback_accidental_notes(channel, idx2)
                        channel += 1
                        debounce = True
                    config = True
                else:
                    xylophone.itemconfig(rectangles2[number], fill='#754C14')
        if channel == 8:
            channel = 1
        if delta < 0:
            debounce = False
        time.sleep(0.005)

        end = z1


def check_index1(x1):
    a = 50
    b = 100
    for index in range(22):
        if a < x1 < b:
            return index
        a += 50
        b += 50


def check_index2(x1):
    a = 150
    b = 250
    for index in range(15):
        if a < x1 < b:
            return index
        a += 50
        b += 50


def back():
    print('Button gedrückt')
    global stop_thread_xylo
    stop_thread_xylo = True
