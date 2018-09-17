import cv2
import numpy as np
import random
from datetime import datetime


img = cv2.imread("01.jpg")
img_origin = cv2.imread("01.jpg")

# img = cv2.imread("ImageSample-3.jpg")
# img_origin = cv2.imread("ImageSample-3.jpg")


"""
for a in range(100, 900):
    for b in range(100, 900):
        if a%2 == 0:
            if b%2 == 0:
                img[a,b] = 255
        else:
            if b%2 != 0:
                img[a,b] = 255
"""

MIN = 50
MAX = 200

r0 = random.randint(MIN, MAX)
r1 = random.randint(MIN, MAX)
r2 = random.randint(MIN, MAX)


r_0_10_a = random.randint(1,11)
r_0_10_b = random.randint(1,11)


r_10_10_0 = random.randint(-10,10)
r_10_10_1 = random.randint(-10,10)
r_10_10_2 = random.randint(-10,10)




r_0_20 = random.randint(1,21)
r_0_30 = random.randint(1,31)


for i in range(0,999):
    for j in range(0,999):
        tmp0 = img[i,j,0]
        tmp1 = img[i,j,1]
        tmp2 = img[i,j,2]
        img[i,j] = img[i+1,j]
        img[i+1,j] = (tmp0, tmp1, tmp2)


for i in range(11,988):
    for j in range(11,988):
        z = random.randint(-10,10)
        tmp0 = img[i,j,0]
        tmp1 = img[i,j,1]
        tmp2 = img[i,j,2]
        img[i,j] = img[i+z,j]
        img[i,j+z] = (tmp0, tmp1, tmp2)


for i in range(51,949):
    for j in range(51,949):

        if i%r_0_10_a == 10:
            if j%r_0_10_b > 3:
                r_10_30 = random.randint(-50,50)
                for u in range(1, r_10_30):
                    img[i+u,j,0] = img[i,j,0]
                    img[i+u,j,1] = img[i,j,1]
                    img[i+u,j,2] = img[i,j,2]




for i in range(0,999):
    for j in range(0,999):

        # img[i,j] = [img[i,j,0], img[i,j,1], img[i,j,2]] ### origin
        # img[i,j] = [img[i,j,0], 0, 0] ### Blue
        # img[i,j] = [0, img[i,j,1], 0] ### Green
        # img[i,j] = [0, 0, img[i,j,2]] ### origin


        # if i%10 ==0:
            # img[i,j] = (255, 0, 0) # Blue
            # img[i,j] = (0, 255, 0) # Green
            # img[i,j] = (0, 0, 255) # Blue


        if i%r_0_20 == 0:
            if img[i, j, 0] < 150:
                img[i,j,0] = img[i,j,0] + r_10_10_0
                img[i,j,1] = img[i,j,1] + r_10_10_1
                img[i,j,2] = img[i,j,2] + r_10_10_2

        if img[i, j, 0] > r1: # Blue
            ran_b = random.randint(r0, 200)
            img[i,j,0] = ran_b
            # img[i,j,0] = 0
        else:
            ran_b = random.randint(30, r0)
            img[i,j,0] = ran_b


        if img[i, j, 1] > r1: # Green
            ran_g = random.randint(r1, 200)
            img[i,j,1] = ran_g
        else:
            ran_g = random.randint(30, r1)
            img[i,j,1] = ran_g







        if img[i, j ,2] > r2: # red
            # ran_r = random.randint(r2, 200)
            # img[i,j,2] = ran_r
            img[i,j,2] = img[i,j,2]-20
        else:
            # ran_r = random.randint(30, r2)
            # img[i,j,2] = ran_r
            img[i,j,2] = img[i,j,2]+20



        if img[i, j ,0] > 170:
            if i%10 == 0:
                img[i,j,1] = img[i,j,1] - 20
                # img[i,j,1] = img[i,j,0]




        if img[i,j ,0] < 50:
            if img[i,j ,1] < 50:
                if img[i,j ,2] < 50:
                    if i%40 == 0:
                        img[i,j,1] = img[i,j,2] + 50
                        img[i,j,0] = img[i,j,0] + 20




cv2.imshow("preview",img)
# cv2.imshow("origin",img_origin)


fileName = datetime.now().strftime("%d%H%M%S")
cv2.imwrite(("./out/" + fileName + ".jpg"), img);



cv2.waitKey(0)
cv2.destroyAllWindows()
