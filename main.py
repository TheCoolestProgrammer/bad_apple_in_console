import time
from datetime import timedelta
import cv2
import numpy as np
import os

# SAVING_FRAMES_PER_SECOND = 30

# filename, _ = os.path.splitext()
if __name__ == '__main__':
    cap = cv2.VideoCapture("bad_apple.mp4")
    fps = cap.get(cv2.CAP_PROP_FPS)
    # width = cap.get(3)
    # height = cap.get(3)
    # cap.open(360)
    # print(width,height)

    downgrade_value_x= 4
    downgrade_value_y=6
    # cap.set(cv2.CAP_PROP_POS_MSEC,(36000))
    # x,image = cap.read()
    # cv2.imwrite("frame.jpg", image)
    count=0
    while True:
        is_image, image = cap.read()
        if not is_image:


            break

        y = 0
        x = 0
        x_string=""
        while y<len(image):
        # for y in range(len(image)):
            x=0
            while x<  len(image[y]):
            # for x in range(len(image[y])):
                z= [image[y][x][0],image[y][x][1],image[y][x][2]]
                # print(image[y][x].all())
                if sum(z)> 255*3//2:
                    x_string +="□"
                    # print("□",end="")
                else:
                    x_string+=" "
                    # print(" ",end="")
                x+=downgrade_value_x
                # print(image[y][x], end=" ")
            # print()
            x_string+="\n"
            y+=downgrade_value_y
        print(x_string)

        # print("_________________")
        # time.sleep(1/(20))
        os.system("cls")
        count+=1
