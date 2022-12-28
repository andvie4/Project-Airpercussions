import threading
from tkinter import *
import customtkinter
from PlayPercussions.Control.SoundControl import Soundevent, stop_thread
from PlayPercussions.Sounds.SoundList import soundlist_bongos




def create_bongos():


    win2 = Toplevel()
    # win2.attributes('-fullscreen', True)
    win2.geometry('1700x800')

    bongos_high = Canvas(win2)
    bongos_high.place(relx=0.25, rely=0.5, relwidth=0.49, relheight=0.9, anchor=CENTER)

    bongos_low = Canvas(win2)
    bongos_low.place(relx=0.75, rely=0.5, relwidth=0.49, relheight=0.9, anchor=CENTER)
    bongos_low.update()
    a = bongos_low.winfo_width()
    b = bongos_low.winfo_height()

    # bongos_high.create_rectangle(100,450,650,750,fill='#c4b98f')
    bongos_high.create_oval(50, 50, a - 50, b - 200, fill='#4f2813')
    bongos_high.create_oval(70, 50, a - 70, b - 260, fill='#f5f7f0')
    bg_high = bongos_high.create_oval(100, 50, a - 110, b - 350, fill='#e0cdbc', width=5)

    bongos_low.create_oval(50, 50, a - 50, b - 100, fill='#4f2813')
    bongos_low.create_oval(70, 50, a - 70, b - 170, fill='#f5f7f0')
    bg_low = bongos_low.create_oval(100, 50, a - 110, b - 250, fill='#e0cdbc', width=5)

    button_close = customtkinter.CTkButton(master=win2, text='Close', fg_color='#cf5148', hover_color="red",
                                           command=back)
    button_close.place(relx=0.92, rely=0.95, relwidth=0.13, relheight=0.06, anchor=CENTER)

    thread_bongo = threading.Thread(target=Soundevent, args=('Bongos', win2, soundlist_bongos, bongos_low, bongos_high,
                                                              bg_low, bg_high,None))
    thread_bongo.start()

    win2.mainloop()


def back():
    print('Button gedrückt')
    stop = True
    stop_thread(stop)
    # global stop_thread_bongo
    # stop_thread_bongo = True


# A useful function to create a circle. Just for trying out. Not used here!
def create_circle(x, y, r, canvasName):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)
