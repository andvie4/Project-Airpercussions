import threading
import tkinter
from tkinter import *
import customtkinter
from PlayPercussions.Control.SoundControl import Soundevent, stop_thread
from PlayPercussions.Sounds.SoundList import soundlist_timbales


def create_timbales():
    win1 = Toplevel()  # must be Tk() instead of Toplevel(); TK() overwrites the Camera Picture
   # win1.attributes('-fullscreen', True)
    win1.geometry('1600x500')

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

    thread_playtimb = threading.Thread(target=Soundevent,
                                       args=('Timbales', win1, soundlist_timbales, timbales, None, hembro,
                                             macho, cowbell))
    thread_playtimb.start()

    win1.mainloop()


def back():
    print('Button gedrückt')
    stop = True
    stop_thread(stop)

