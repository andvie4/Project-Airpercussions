import threading
import time
from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont

from PlayPercussions.view.SelectWindow import selectwindow
from depthai_hand_tracker.HandController import closemouse
from depthai_hand_tracker.demo import coord

from pygame import mixer

from PlayPercussions.Button import create_button
import pyautogui
import winsound
from pynput.mouse import Button, Controller


i = 0

def gui():
    backgroundmusic('play', 1)
    root = Tk()
    # set window size
    #root.attributes('-fullscreen', True, )
    root.geometry("1500x500")
    screen_width = root.winfo_screenwidth()  # winfo.screenwdth returns not always the real width
    screen_height = root.winfo_screenheight()

    # root.geometry(f'{screen_width}x{screen_height}')
    # set background picture
    bg = Image.open(open('../PlayPercussions/Images/Background_drums.png', 'rb'))
    bg.thumbnail((screen_width, screen_height))
    bg = ImageTk.PhotoImage(bg)
    mylabel = Label(root, image=bg, width=screen_width, height=screen_height, bg="#fbfafb")
    mylabel.place(x=0, y=0, relwidth=1, relheight=1)
    # set headline
    headline = Label(root, text="Air Percussions", bg="#fbfafb")
    headline.place(relx=0.3, rely=0.08, anchor='center')
    headfont = tkFont.Font(family="Papyrus", size=80, weight="bold")
    headline.config(font=headfont)

    # create 'mouse'
  #  canvas = Canvas(root, width=370, height=700, bg='#fbfafb')
   # canvas.pack(anchor='se', side=BOTTOM)
   # rectangle = canvas.create_rectangle(10, 10, 30, 30, fill='red')
    # set buttons

    button_play = create_button(root, next_window, "Play")
    button_play.place(relx=0.9, rely=0.45, relheight=0.08, relwidth=0.17, anchor=CENTER)

    button_help = create_button(root, open_help, "Help")
    button_help.place(relx=0.9, rely=0.55, relheight=0.08, relwidth=0.17, anchor=CENTER)

    button_about = create_button(root, open_about, "About")
    button_about.place(relx=0.9, rely=0.65, relheight=0.08, relwidth=0.17, anchor=CENTER)

    button_exit = create_button(root, lambda: shut_down(root), "Quit")
    button_exit.place(relx=0.9, rely=0.85, relheight=0.08, relwidth=0.17, anchor=CENTER)

    root.mainloop()


def shut_down(root):
    closemouse(1)
    backgroundmusic('stop', 0)
    root.quit()


def next_window():
    winsound.PlaySound('BackgroundMusic/Buttonjingle.wav', winsound.SND_ASYNC)
    backgroundmusic('stop', 0)

    selectwindow()


def buttonpress():
    winsound.PlaySound('BackgroundMusic/Buttonjingle.wav', winsound.SND_ASYNC)
    backgroundmusic('stop', 0)
    selectwindow()


def backgroundmusic(command, volume):
    mixer.init()
    mixer.music.load("../PlayPercussions/BackgroundMusic/PercussionBackgroundMusic.mp3")
    mixer.music.set_volume(volume)
    if command == 'play':
        mixer.music.play(-1)


def open_help():
    filename = "../src/textfiles/help.txt"
    top = Toplevel()
    top.title("Help")
    Label(top, text=open(filename, 'r').read()).pack()
    top.mainloop()


def open_about():
    print()

def set_cursor():
            x1 = coord[0]
            y1 = coord[1]
            z1 = coord[2]
            dist = coord[6]
            print(x1, y1)
            if x1 >0:

             if x1>300:
                if y1 < 450:
                    if 300 < x1 < 600:
                        pyautogui.moveTo(1500, 800)
                        if dist < 1:
                            print('klick')
                            #mouse.press(Button.left)
                            #mouse.release(Button.left)
                    if 600 < x1 < 900:
                        pyautogui.moveTo(1000, 800)
                    if 900 < x1 < 1200:
                        pyautogui.moveTo(500, 800)
                if y1 > 450:
                    if 300 < x1 < 600:
                        pyautogui.moveTo(1500, 400)
                    if 600 < x1 < 900:
                        pyautogui.moveTo(1000, 400)
                    if 900 < x1 < 1200:
                        pyautogui.moveTo(500, 400)

 # def ausgabe():
  #      x1 = coord[0]
   #     y1 = coord[1]
    #    z1 = coord[2]
     #   dist = coord[6]



     #   if y1 == 0:
      #      canvas.itemconfig(rectangle, fill='red')

       # if y1 > 0:
        #    canvas.itemconfig(rectangle, fill='green')
         #   if x1 > 300:
          #      canvas.itemconfig(rectangle, fill='red')

           # if x1<300:
            #    if y1 < 200:
             #       canvas.moveto(rectangle, 1, 540)
              #      pyautogui.moveTo(1800, 900)
               #     if dist < 1:
                #        print('klick')
               # elif 200 < y1 < 400:
                #    canvas.moveto(rectangle, 1, 330)
                 #   pyautogui.moveTo(1800, 700)
             #   elif 400 < y1 < 600:
              #      canvas.moveto(rectangle, 1, 230)
               #     pyautogui.moveTo(1800, 600)
               # else:
                #    canvas.moveto(rectangle, 1, 130)
                 #   pyautogui.moveTo(1800, 500)
                  #  if dist < 1:
                        # next_window()
                       # mouse.press(Button.left)
                       # mouse.release(Button.left)
                   #     print('klick')




       # root.after(1, ausgabe)

   # root.after(1, ausgabe)