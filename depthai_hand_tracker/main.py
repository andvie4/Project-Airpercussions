import threading
import time

from PlayPercussions.view.Main_Window import gui

from depthai_hand_tracker.mouse import  handmouse

if __name__ == '__main__':

    thread_gui = threading.Thread(target=gui)
    thread_gui.start()
    time.sleep(1)
    #controlmouse()
    handmouse()



