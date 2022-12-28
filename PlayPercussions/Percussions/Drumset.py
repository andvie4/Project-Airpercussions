import tkinter
from tkinter import *
import customtkinter
from PIL import Image, ImageTk


def create_drumset():
    win = Toplevel()
    win.attributes('-fullscreen', True)

    drumset = Canvas(win)

    drumset.pack(fill=tkinter.BOTH, expand=True)
    #img = ImageTk.PhotoImage(file='../PlayPercussions/Images/OnStage_Night.gif')
    #drumset.create_image(0, 0, image=img, anchor=NW)

    screen_width_middle = win.winfo_screenwidth() / 2
    screen_height_middle = win.winfo_screenheight() / 2
    print(screen_width_middle, screen_height_middle)

    # create Base-drum
    drumset.create_oval(screen_width_middle - 250, screen_height_middle + 125, screen_width_middle + 50,
                        screen_height_middle + 425,
                        activeoutline="red", width=5, fill='#D3D3D3')
    drumset.create_text(screen_width_middle-100, screen_height_middle + 200, text="I love Drums", font=("Helvetica", 20))
    # create Snare-drum
    drumset.create_oval(screen_width_middle - 460, screen_height_middle + 90, screen_width_middle - 250,
                        screen_height_middle + 260, fill='#F4A460', width=2)
    drumset.create_oval(screen_width_middle - 460, screen_height_middle + 90, screen_width_middle - 250,
                        screen_height_middle + 240,
                        fill='#f3ede7', activeoutline='red', width=3)
    drumset.create_line(screen_width_middle - 350, screen_height_middle + 260, screen_width_middle - 350,
                        screen_height_middle + 350, width=8,
                        fill='#C0C0C0')
    drumset.create_line(screen_width_middle - 350, screen_height_middle + 350, screen_width_middle - 425,
                        screen_height_middle + 400, width=8,
                        fill='#C0C0C0')
    drumset.create_line(screen_width_middle - 350, screen_height_middle + 350, screen_width_middle - 260,
                        screen_height_middle + 400, width=8,
                        fill='#C0C0C0')
    drumset.create_line(screen_width_middle - 325, screen_height_middle + 350, screen_width_middle - 350,
                        screen_height_middle + 350, width=5,
                        fill='#C0C0C0')

    # create Hi-hat
    drumset.create_oval(screen_width_middle - 600, screen_height_middle + 60, screen_width_middle - 380,
                        screen_height_middle - 50,
                        fill='#f3c56f', width=2)
    drumset.create_oval(screen_width_middle - 600, screen_height_middle + 50, screen_width_middle - 380,
                        screen_height_middle - 50,
                        fill='#fdd987', activeoutline='red', width=3)
    drumset.create_oval(screen_width_middle - 495, screen_height_middle - 5, screen_width_middle - 485,
                        screen_height_middle + 5,
                        fill='black')
    drumset.create_line(screen_width_middle - 490, screen_height_middle + 60, screen_width_middle - 490,
                        screen_height_middle + 300,
                        fill='#C0C0C0', width=6)
    drumset.create_line(screen_width_middle - 490, screen_height_middle - 5, screen_width_middle - 490,
                        screen_height_middle - 60,
                        fill='#C0C0C0', width=6)
    drumset.create_line(screen_width_middle - 490, screen_height_middle + 300, screen_width_middle - 590,
                        screen_height_middle + 350,
                        fill='#C0C0C0', width=6)
    drumset.create_line(screen_width_middle - 490, screen_height_middle + 300, screen_width_middle - 390,
                        screen_height_middle + 350,
                        fill='#C0C0C0', width=6)
    drumset.create_line(screen_width_middle - 490, screen_height_middle + 300, screen_width_middle - 550,
                        screen_height_middle + 300,
                        fill='#C0C0C0', width=4)
    # create Cymbals
    drumset.create_oval(screen_width_middle - 650, screen_height_middle - 200, screen_width_middle - 400,
                        screen_height_middle - 100,
                        fill='#fdd987', activeoutline='red', width=3)
    drumset.create_oval(screen_width_middle - 530, screen_height_middle - 155, screen_width_middle - 520,
                        screen_height_middle - 145, fill='black')
    drumset.create_line(screen_width_middle - 525, screen_height_middle - 100, screen_width_middle - 525,
                        screen_height_middle - 50,
                        fill='#C0C0C0', width=5)
    drumset.create_line(screen_width_middle - 525, screen_height_middle + 60, screen_width_middle - 525,
                        screen_height_middle + 250,
                        fill='#C0C0C0', width=5)
    drumset.create_line(screen_width_middle - 525, screen_height_middle + 250, screen_width_middle - 625,
                        screen_height_middle + 280,
                        fill='#C0C0C0', width=5)
    drumset.create_line(screen_width_middle - 525, screen_height_middle + 250, screen_width_middle - 425,
                        screen_height_middle + 280,
                        fill='#C0C0C0', width=5)
    drumset.create_line(screen_width_middle - 525, screen_height_middle + 250, screen_width_middle - 575,
                        screen_height_middle + 250,
                        fill='#C0C0C0', width=5)

    # create Tom-tom left
    round_rectangle(drumset,screen_width_middle-300, screen_height_middle-30,screen_width_middle-115,
                    screen_height_middle+130,180)
    drumset.create_oval(screen_width_middle - 300, screen_height_middle + 70, screen_width_middle - 115,
                        screen_height_middle - 70,
                        fill='#ecdbd3',activeoutline='red',width=3)

    # create Tom-tom right
    round_rectangle(drumset, screen_width_middle -85, screen_height_middle -30, screen_width_middle +100,
                    screen_height_middle + 130, 180)
    drumset.create_oval(screen_width_middle + 100, screen_height_middle + 70, screen_width_middle -85,
                        screen_height_middle - 70,
                        fill='#ecdbd3',activeoutline='red',width=3)
    # connection both Tom-toms
    drumset.create_line(screen_width_middle-115,screen_height_middle,screen_width_middle-85,screen_height_middle,
                        fill='#aaa9ad',width=10)
    drumset.create_line(screen_width_middle-100,screen_height_middle+5,screen_width_middle-100,screen_height_middle+125,
                        fill='#aaa9ad',
                        width=10)
    # create big Tom-tom
    round_rectangle(drumset, screen_width_middle+55,screen_height_middle+105,screen_width_middle+255,
                    screen_height_middle+370,200)
    drumset.create_oval(screen_width_middle+55,screen_height_middle+100,screen_width_middle+255,screen_height_middle+280,
                        fill='#ecdbd3',activeoutline='red',width=3)
    drumset.create_line(screen_width_middle+155,screen_height_middle+372,screen_width_middle+50,
                        screen_height_middle+420,fill='#C0C0C0', width=8)
    drumset.create_line(screen_width_middle + 155, screen_height_middle + 372, screen_width_middle + 260,
                        screen_height_middle + 420, fill='#C0C0C0', width=8)
    drumset.create_line(screen_width_middle + 155, screen_height_middle + 372, screen_width_middle + 50,
                        screen_height_middle + 372, fill='#C0C0C0', width=5)
    drumset.create_line(screen_width_middle + 155, screen_height_middle + 372, screen_width_middle + 230,
                        screen_height_middle + 380, fill='#C0C0C0', width=5)
    # create Cymbal right
    drumset.create_oval(screen_width_middle+170, screen_height_middle-150,screen_width_middle+450, screen_height_middle,
                        fill='#fdd987',activeoutline='red',width=3)
    drumset.create_oval(screen_width_middle+305,screen_height_middle-76,screen_width_middle+315,screen_height_middle-66,
                        fill='black')
    drumset.create_line(screen_width_middle+305,screen_height_middle,screen_width_middle+305,screen_height_middle+400,
                        fill='#C0C0C0',width=5)
    drumset.create_line(screen_width_middle+305,screen_height_middle+400,screen_width_middle+250,screen_height_middle+450,
                        fill='#C0C0C0',width=5)
    drumset.create_line(screen_width_middle + 305, screen_height_middle + 400, screen_width_middle + 380,
                        screen_height_middle + 420,
                        fill='#C0C0C0', width=5)
    drumset.create_line(screen_width_middle + 305, screen_height_middle + 400, screen_width_middle + 240,
                        screen_height_middle + 400,
                        fill='#C0C0C0', width=5)

    button_close = customtkinter.CTkButton(master=win, text='Close', fg_color='#cf5148', hover_color="red",
                                           command=win.destroy)
    button_close.place(relx=0.92, rely=0.95, relwidth=0.13, relheight=0.06, anchor=CENTER)
    win.mainloop()


def create_circle(x, y, r, canvasName):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, activeoutline='red')


def round_rectangle(canvas,x1, y1, x2, y2, radius, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True,fill='#EE7621')




