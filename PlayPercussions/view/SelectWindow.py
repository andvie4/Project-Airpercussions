import threading
import time
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from PlayPercussions.Percussions.ListofPercussions import percussionlist

from PlayPercussions.Percussions.Bongos import create_bongos
from PlayPercussions.Percussions.Drumset import create_drumset
from PlayPercussions.Percussions.Steeldrum import create_steeldrum
from PlayPercussions.Percussions.Timbales import create_timbales

from PlayPercussions.Percussions.Timpani import create_timpani
from PlayPercussions.Percussions.Xylophone import create_xylophone
from depthai_hand_tracker.HandController import closemouse

from depthai_hand_tracker.demo import open_depht_camera
from pynput.mouse import Controller

label_list = []
index = 0

mouse = Controller()


def selectwindow():
    win = Toplevel()
    win.attributes('-fullscreen', True, )
   # win.geometry('1500x500')
    win.config(bg="white")
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    label = Label(win, text="Please select one Percussion!", font=("Papyrus", 30), bg="white", fg='black')
    label.place(relx=0.5, rely=0.5, anchor=CENTER)
    button_next = customtkinter.CTkButton(master=win, text='Next', fg_color='#6aa64e', hover_color="#5cb533",
                                          command=play)
    button_next.place(relx=0.92, rely=0.85, relwidth=0.13, relheight=0.06, anchor=CENTER)
    button_close = customtkinter.CTkButton(master=win, text='Close', fg_color='#cf5148', hover_color="red",
                                           command=win.destroy)
    button_close.place(relx=0.92, rely=0.95, relwidth=0.13, relheight=0.06, anchor=CENTER)
    x = 0.05
    y = 0.1

    label_list.clear()

    for i in range(len(percussionlist)):

        img = Image.open(open(percussionlist[i][1], 'rb'))
        img.thumbnail((int(screen_width / 6), int(screen_height / 4)))
        ph = ImageTk.PhotoImage(img, master=win)

        label = Label(win, text=percussionlist[i][0], image=ph, compound='bottom', font=("Papyrus", 20), cursor="hand2",
                      relief=RAISED)
        label.config(width=screen_width / 4.5, height=screen_height / 3)
        label.image = ph  # need to keep the reference of your image to avoid garbage collection

        if i == 3:
            x = 0.05
            y = 0.6
        label.place(relx=x, rely=y)
        x += 0.28

        label_list.append(label)

        label.bind('<Enter>', lambda e: e.widget.config(relief=SUNKEN))
        label.bind('<Leave>', lambda e: e.widget.config(relief=RAISED))
        label.bind("<Button-1>", get_label_text)

    win.mainloop()


def get_label_text(event):
    text = event.widget

    name = text.cget("text")
    print(name)
    global index
    index = ([i for i in range(len(percussionlist)) if name in percussionlist[i]][0])

    for i in range(len(label_list)):
        if i == index:
            label_list[i].config(bg='blue')
        else:
            label_list[i].config(bg='white')


def get_graphic():
    closemouse(1)
    open_dcamera()

    global index
    match index:
        case 0:
            label_list[index].config(bg='white')
            create_steeldrum()
        case 1:
            label_list[index].config(bg='white')
            create_timbales()
        case 2:
            label_list[index].config(bg='white')
            create_bongos()
        case 3:
            label_list[index].config(bg='white')
            create_xylophone()
        case 4:
            label_list[index].config(bg='white')
            create_timpani()
        case 5:
            label_list[index].config(bg='white')
            create_drumset()


def play():
    get_graphic()


def open_dcamera():
    thread_open_dcamera = threading.Thread(target=open_depht_camera)
    thread_open_dcamera.start()



def reopen():
    while True:
        print('Hallo')

def change(x):
    if x==0:
        print('Hallo')