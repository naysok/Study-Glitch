import cv2
# import numpy as np
import random
from datetime import datetime

### 40.363846017 sec
### 44.626873741 sec
###
###
###

Index = 100
for x in range(Index, Index+1): ### debug

# for x in range(1, 100):

    time1 = cv2.getTickCount() # クロック時間


    num = "%05d" % x
    in_path = "src_cropped/image-" + num + ".jpg"
    out_path = "test-Glitch/image-" + num + ".jpg"
    out_path_debug = "test-Glitch/image-" + num + "-" +datetime.now().strftime("%H-%M-%S")+".jpg"




    img = cv2.imread(in_path)


    WH = 720 # H
    ADD = 50








    ### Blur
    for i in range(0,WH):
        for j in range(0,WH):
            if j%2 == 0:
                tmp0 = img[i,j,0]
                tmp1 = img[i,j,1]
                tmp2 = img[i,j,2]
                img[i,j] = img[i,j+1]
                img[i,j+1] = (tmp0, tmp1, tmp2)




            ### Draw Line
            r_0_20_h = random.randint(1,21)
            r_0_20_v = random.randint(1,21)
            r_10_10_0 = random.randint(-10,10)
            r_10_10_1 = random.randint(-10,10)
            r_10_10_2 = random.randint(-10,10)


            ### Draw horizontal line (-)
            if i%r_0_20_h < 2:
                if img[i, j, 0] < 180:
                    img[i,j,0] = img[i,j,0] + r_10_10_0 + 10
                    img[i,j,1] = img[i,j,1] + r_10_10_1 + 10
                    img[i,j,2] = img[i,j,2] + r_10_10_2 + 10

            ### Draw vertical line (|)
            if j%r_0_20_v < 2:
                if img[i, j, 0] < 180:
                    img[i,j,0] = img[i,j,0] + r_10_10_0 + 10
                    img[i,j,1] = img[i,j,1] + r_10_10_1 + 10
                    img[i,j,2] = img[i,j,2] + r_10_10_2 + 10




            ### Edit Color Channel

            MIN = 51
            MAX = 179
            r_MM0 = random.randint(MIN, MAX)
            r_MM1 = random.randint(MIN, MAX)
            r_MM2 = random.randint(MIN, MAX)
            r0 = random.randint(MIN, MAX)
            r1 = random.randint(MIN, MAX)
            r2 = random.randint(MIN, MAX)
            r2 = random.randint(MIN, MAX)


            ### Edit Blue Channel
            if img[i, j, 0] > r_MM0: # Blue
                ran_b = random.randint(r0, 180)
                img[i,j,0] = (img[i,j,0] + ran_b)/2
            else:
                ran_b = random.randint(50, r0)
                img[i,j,0] =  (img[i,j,0] + ran_b)/2


            ### Edit Green Channel
            if img[i, j, 1] > r_MM1: # Green
                ran_g = random.randint(r1, 180)
                img[i,j,1] = (img[i,j,1] + ran_g)/2
            else:
                ran_g = random.randint(50, r1)
                img[i,j,1] = (img[i,j,1] + ran_g)/2


            ### Edit Red Channel
            if img[i, j ,2] > r_MM2: # red
                ran_r = random.randint(r2, 180)
                img[i,j,2] = (img[i,j,1] + ran_r)/2
            else:
                ran_r = random.randint(50, r2)
                img[i,j,2] = img[i,j,2] = (img[i,j,1] + ran_r)/2




            ### Overflow Blue
            if img[i,j,0] > 225 and img[i,j,1] < 50 and img[i,j,2] < 50:
                img[i,j,0] = 255
                img[i,j,1] = 0
                img[i,j,2] = 0

            ## Overflow Green
            if img[i,j,1] > 220 and img[i,j,0] < 50 and img[i,j,2] < 50:
                img[i,j,0] = 0
                img[i,j,1] = 255
                img[i,j,2] = 0

            ## Overflow Green
            if img[i,j,2] > 220 and img[i,j,0] < 50 and img[i,j,1] < 50:
                img[i,j,0] = 0
                img[i,j,1] = 0
                img[i,j,2] = 255





    ### scratch
    sc_r_0_20_h = random.randint(5,21)
    sc_r_0_20_v = random.randint(5,21)

    ### scratch horizontal (-)

    for i in range(0, WH-20):
        for j in range(0, WH-20):
            if i%sc_r_0_20_h < 1:
                tmp0 = img[i,j,0]
                tmp1 = img[i,j,1]
                tmp2 = img[i,j,2]

                img[i,j] = img[i+sc_r_0_20_h,j]
                img[i+sc_r_0_20_h,j] = (tmp0, tmp1, tmp2)

            ### scratch vertical (|)

            if j%sc_r_0_20_v < 1:
                tmp0 = img[i,j,0]
                tmp1 = img[i,j,1]
                tmp2 = img[i,j,2]
                img[i,j] = img[i,sc_r_0_20_v]
                img[i,sc_r_0_20_v] = (tmp0, tmp1, tmp2)









    print(datetime.now().strftime("%H:%M:%S"))
    cv2.imshow("preview",img)

    cv2.imwrite(out_path_debug, img);
    #cv2.imwrite(out_path, img);

    cv2.destroyAllWindows()
    print("Glitched :", num)

    time2 = cv2.getTickCount()
    time = (time2 - time1)/cv2.getTickFrequency() # クロック時間の差を周波数で割ると秒
    print(time, "sec")


print("Finished!!")
