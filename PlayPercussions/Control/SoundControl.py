import threading
import time
import pygame
from depthai_hand_tracker.demo import coord, close_depth_camera
from depthai_hand_tracker.mouse import handmouse

stopthread = False


class Soundevent:
    def __init__(self, name,win, soundlist, canvas1, canvas2,canvas3, oval1, oval2):

        self.name = name
        self.win = win
        self.soundlist = soundlist
        self.canvas1 = canvas1
        self.canvas2 = canvas2
        self.canvas3= canvas3
        self.oval1 = oval1
        self.oval2 = oval2

        if name == 'Bongos' or name == 'Timpani':
            self.soundbongo()

    pygame.init()

    def playback_bongo(self, channel, index):
        pygame.mixer.Channel(channel).play(pygame.mixer.Sound(self.soundlist[index]))

    def soundbongo(self):

        b = 0
        debounce = True
        channel = 1
        while True:
            global stopthread
            if stopthread:
                print('thread gestoppt')
                stopthread = False
                close_depth_camera(1)
                thread = threading.Thread(target=handmouse)
                thread.start()
                self.win.withdraw()
                break
            x1 = coord[0]
            y1 = coord[1]
            z1 = coord[2]
            x2 = coord[3]
            y2 = coord[4]
            z2 = coord[5]

            a = z1

            delta = b - a

            if 900 > x1 > 5:
                self.canvas1.itemconfig(self.oval1, fill='red')
                if delta > 4 and not debounce:
                    self.playback_bongo(channel, 0)
                    channel += 1
                    if channel == 8:
                        channel = 1
                    debounce = True
            else:
                self.canvas1.itemconfig(self.oval1, fill='#e0cdbc')
            if x1 > 900:
                self.canvas2.itemconfig(self.oval2, fill='red')
                if delta > 3 and not debounce:
                    self.playback_bongo(channel, 1)
                    channel += 1
                    if channel == 8:
                        channel = 1
                    debounce = True
            else:
                self.canvas2.itemconfig(self.oval2, fill='#d9d4d0')

            if delta < 0:
                debounce = False
            time.sleep(0.01)

            b = z1

            time.sleep(0.01)






def stop_thread(stop):
    if stop:
        global stopthread
        stopthread = True
