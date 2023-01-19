import threading
import time
import tkinter
from tkinter import *
import customtkinter
import math
import pygame
from PlayPercussions.Sounds.SoundList import soundlist_steeldrum
from depthai_hand_tracker.demo import coord, close_depth_camera
from depthai_hand_tracker.mouse import handmouse
from screeninfo import get_monitors

note_name = ['A', 'E', 'H', 'F#/Ges', 'C#/Des', 'G#/As', 'D#/Es', 'B', 'F', 'C', 'G', 'D']
polygon_index = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
stop_thread_steeldrum = False
coord[6]=10

def calcirclepoints(angle, radius1, radius2):
    pointslist = []

    for i in range(12):
        rad = math.radians(angle)
        x1 = int(radius1 * math.cos(rad))
        y1 = int(math.sqrt(radius1 ** 2 - x1 ** 2))
        x2 = int(radius2 * math.cos(rad))
        y2 = int(math.sqrt(radius2 ** 2 - x2 ** 2))

        pointslist.append((x1, y1, x2, y2))
        angle += 30
    return pointslist


def create_steeldrum():
    points = calcirclepoints(0, 250, 450)

    win0 = Toplevel()
    #win0.attributes('-fullscreen', True)
    win0.geometry('1500x800')

    for monitor in get_monitors():
        width = monitor.width
        height = monitor.height

    steeldrum = Canvas(win0)

    steeldrum.pack(fill=tkinter.BOTH, expand=True)
    # img = ImageTk.PhotoImage(file='../PlayPercussions/Images/Trinidad.gif')
    # steeldrum.create_image(0, 0, image=img, anchor=NW)

    screen_width_middle = width / 2
    screen_height_middle = height / 2
    print(screen_width_middle, screen_height_middle)

    steeldrum.create_oval(screen_width_middle - 500, screen_height_middle - 500, screen_width_middle + 500,
                          screen_height_middle + 500, fill='#696969')

    increase = 1

    for i in range(12):
        if i == 11:
            increase = -11
        if i > 5:
            polygon_index[i] = steeldrum.create_polygon(screen_width_middle + points[i][0],
                                                        screen_height_middle + points[i][1],
                                                        screen_width_middle + points[i][2],
                                                        screen_height_middle + points[i][3],
                                                        screen_width_middle + points[i + increase][2],
                                                        screen_height_middle + points[i + increase][3],
                                                        screen_width_middle + points[i + increase][0],
                                                        screen_height_middle + points[i + increase][1],
                                                        fill='grey', outline='black')

        if i <= 5:
            polygon_index[i] = steeldrum.create_polygon(screen_width_middle + points[i][0],
                                                        screen_height_middle - points[i][1],
                                                        screen_width_middle + points[i][2],
                                                        screen_height_middle - points[i][3],
                                                        screen_width_middle + points[i + increase][2],
                                                        screen_height_middle - points[i + increase][3],
                                                        screen_width_middle + points[i + increase][0],
                                                        screen_height_middle - points[i + increase][1],
                                                        fill='grey', outline='black')

    letterpoints = calcirclepoints(15, 190, 0)
    for i in letterpoints:
        print(i)

    for i in range(12):
        if i < 6:
            steeldrum.create_text(screen_width_middle + letterpoints[i][0], screen_height_middle - letterpoints[i][1],
                                  text=note_name[i], font=('Helvetica', 20))
        if i >= 6:
            steeldrum.create_text(screen_width_middle + letterpoints[i][0],
                                  screen_height_middle + letterpoints[i][1],
                                  text=note_name[i], font=('Helvetica', 20))

    steeldrum.create_oval(screen_width_middle + 150, screen_height_middle + 150, screen_width_middle - 150,
                          screen_height_middle - 150)

    button_close = customtkinter.CTkButton(master=win0, text='Close', fg_color='#cf5148', hover_color="red",
                                           command=back)
    button_close.place(relx=0.92, rely=0.95, relwidth=0.13, relheight=0.06, anchor=CENTER)

    pygame.init()

    def playback_steeldrum(channel, index):
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(soundlist_steeldrum[index]))

    def play_steeldrum():
        debounce = True
        global stop_thread_steeldrum, width, height
        end = 0
        channel = 1

        while True:  # if the close button is pressed, the back function is called and set  stop_thread to True
            if stop_thread_steeldrum:
                print('thread gestoppt')
                stop_thread_steeldrum = False
                close_depth_camera(1)
                thread = threading.Thread(target=handmouse)
                thread.start()
                win0.withdraw()
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
            print(distance)
            if distance == 0:
               stop_thread_steeldrum=True

            idx = check_index(x1)
            if idx is not None:
                if y1 < 450:
                    idx = 11 - idx

                for y in range(12):
                    if idx == y:
                        steeldrum.itemconfig(polygon_index[y], fill='red')
                        if delta > 4 and not debounce:
                            playback_steeldrum(channel, idx)
                            channel += 1
                            debounce = True
                    else:
                        steeldrum.itemconfig(polygon_index[y], fill='grey')
            if channel == 8:
                channel = 1

            if delta < 0:
                debounce = False
            time.sleep(0.005)
            end = z1

    thread_steeldrum = threading.Thread(target=play_steeldrum)
    thread_steeldrum.start()
    win0.mainloop()


# checks in which sector is the hand
def check_index(x1):
    a = 50
    b = 250
    for index in range(6):
        if a < x1 < b:
            return index
        a += 200
        b += 200


def back():
    print('Button gedrückt')
    global stop_thread_steeldrum
    stop_thread_steeldrum = True
