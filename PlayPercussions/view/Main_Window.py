from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
from PlayPercussions.view.SelectWindow import selectwindow
from depthai_hand_tracker.HandController import closemouse
from pygame import mixer
from PlayPercussions.Button import create_button
#import winsound


def gui():
    backgroundmusic('play', 1)
    root = Tk()
    # set window size
    root.attributes('-fullscreen', True, )
    #root.geometry("1500x500")
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
    root.quit()


def next_window():
    #winsound.PlaySound('BackgroundMusic/Buttonjingle.wav', winsound.SND_ASYNC)
    backgroundmusic('stop', 0)

    selectwindow()


def buttonpress():
    #winsound.PlaySound('BackgroundMusic/Buttonjingle.wav', winsound.SND_ASYNC)
    backgroundmusic('stop', 0)
    selectwindow()


def backgroundmusic(command, volume):
    mixer.init()
    mixer.music.load("../PlayPercussions/BackgroundMusic/PercussionBackgroundMusic.mp3")
    mixer.music.set_volume(volume)
    if command == 'play':
        mixer.music.play(-1)
    if command == 'stop':
        mixer.music.stop()


def open_help():
    filename = "../src/textfiles/help.txt"
    top = Toplevel()
    top.title("Help")
    Label(top, text=open(filename, 'r').read()).pack()
    top.mainloop()


def open_about():
    # to be done
    print()
