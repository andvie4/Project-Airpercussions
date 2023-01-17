import time

import numpy as np

from screeninfo import get_monitors

from HandTrackerRenderer import HandTrackerRenderer
from HandTracker import HandTracker

monitor = get_monitors()[0]  # Replace '0' by the index of your screen in case of multiscreen

cam_width = 1152
cam_height = 648

width = monitor.width
height = monitor.height
stop_camera_thread = False
coord = np.empty(7, dtype=int)


def open_depht_camera():
    tracker = HandTracker(

        lm_model='lite',
        use_lm=True,
        xyz=True,
        # use_lm=False

    )

    renderer = HandTrackerRenderer(
        tracker=tracker,
    )

    while True:
        global stop_camera_thread
        if stop_camera_thread:
            stop_camera_thread = False
            print('stop')

            break
        st = time.time()

        # Run hand tracker on next frame
        # 'bag' contains some information related to the frame
        # and not related to a particular hand like body keypoints in Body Pre Focusing mode
        # Currently 'bag' contains meaningful information only when Body Pre Focusing is used
        frame, hands, bag = tracker.next_frame()

        coordinates(hands)

        if frame is None: break
        # Draw hands
        frame = renderer.draw(frame, hands, bag)
        key = renderer.waitKey(delay=1)
        # end = time.time()
        # print(end - st, 'Zeit für Schleife')

        if key == 27 or key == ord('q'):
            break

    renderer.exit()
    tracker.exit()


def calculatepixel(x1, y1, x2, y2):
    if x2 == 0:
        pixelx1 = int(monitor.width / 2 + (3.125) * x1)  # depends on the angle
        pixely1 = int(monitor.height / 2 + (3.7) * y1)
        pixelx2 = 0
        pixely2 = 0

    else:
        pixelx1 = int(monitor.width / 2 + (3.125) * x1)  # depends on the angle
        pixely1 = int(monitor.height / 2 + (3.7) * y1)
        pixelx2 = int(monitor.width / 2 + (3.125) * x2)  # depends on the angle
        pixely2 = int(monitor.height / 2 + (3.7) * y2)

    global coord
    coord[0] = pixelx1
    coord[1] = pixely1
    coord[3] = pixelx2
    coord[4] = pixely2


def coordinates(hands):
    global coord
    if len(hands) == 0:
        for i in range(len(coord)):
            coord[i] = 0
        coord[6]=10

    if len(hands) > 0:
        x1 = hands[0].xyz[0]
        y1 = hands[0].xyz[1]
        x2 = 0
        y2 = 0
        z1= hands[0].xyz[2]
        #z1 = hands[0].norm_landmarks[5][2]
        thumb = hands[0].norm_landmarks[4][0] * 100
        middlefinger = hands[0].norm_landmarks[12][0] * 100
        # z5= hands[0].xyz[2]

        calculatepixel(x1, y1, x2, y2)
        coord[2] = z1/10
        coord[6] = thumb - middlefinger
        # coord[2]=z5
        if len(hands) > 1:
            z2 = hands[1].xyz[2]
            coord[5] = z2/10
            x1 = hands[0].xyz[0]
            y1 = hands[0].xyz[1]
            x2 = hands[1].xyz[0]
            y2 = hands[1].xyz[1]


            calculatepixel(x1, y1, x2, y2)


def close_depth_camera(x):
    if x == 1:
        global stop_camera_thread
        stop_camera_thread = True
