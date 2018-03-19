import time

import cv2
import mss
import numpy as np

# import win32gui as win

with mss.mss() as sct:
    # hwnd = win.FindWindow(None, 'Calculator')
    # Create MSER object
    mser = cv2.MSER_create()
    monitor_number = 2
    mon = sct.monitors[monitor_number]

    monitor = {'top': mon['top'],
               'left': mon['left'],
               'width': mon['width'],
               'height': mon['height'],
               'mon': monitor_number}

    while 'Screen capturing':
        # rect = win.GetWindowPlacement(hwnd.__int__())[-1]
        # print(rect)
        # point_left = win.ClientToScreen(hwnd, (rect[0],rect[1]))
        # print(point_left)
        # point_right = win.ClientToScreen(hwnd, (rect[2],rect[3]))
        # print(point_right)
        # # Part of the screen to capture
        # monitor = {'top': point_left[0], 'left': point_left[1], 'width': point_right[0], 'height': point_right[1]}

        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))
        # Convert to gray scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        vis = img.copy()

        # detect regions in gray scale image
        regions, _ = mser.detectRegions(gray)

        hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]

        cv2.polylines(vis, hulls, 1, (0, 255, 0))

        # Display the picture
        cv2.imshow('OpenCV/Numpy normal', vis)

        mask = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8)

        for contour in hulls:
            cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #             cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        # print('fps: {0}'.format(1 / (time.time()-last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
