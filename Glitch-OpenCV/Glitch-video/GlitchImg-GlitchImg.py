import cv2
# import numpy as np
import random
from datetime import datetime



### Debug
### Sample
# for test in range(0, 5): ### debug
#     test_list = [1, 400, 600, 800, 1400]
#     x = test_list[test]







for x in range(1, 1559):






    print(x)

    time1 = cv2.getTickCount() # クロック時間


    num = "%05d" % x
    in_path = "src_glitch/image-" + num + ".jpg"
    out_path = "src_glitch_glitch/image-" + num + ".jpg"
    out_path_debug = "test-Glitch/image-" + num + "-" +datetime.now().strftime("%H-%M-%S")+".jpg"




    img = cv2.imread(in_path)


    WH = 720 # H
    ADD = 50



################################################################################




    ##### Prepare

    pre_x = random.randint(1,11)

    if pre_x < 3:
        ### scratch
        sc_r_0_20_v = random.randint(2,17)

        ### scratch vertical (|)
        for i in range(0, WH):
            for j in range(0, WH-16):
                if j%sc_r_0_20_v < 1:
                    tmp0 = img[i,j,0]
                    tmp1 = img[i,j,1]
                    tmp2 = img[i,j,2]
                    img[i,j] = img[i,sc_r_0_20_v]
                    img[i,sc_r_0_20_v] = (tmp0, tmp1, tmp2)


################################################################################



    ##### Base

    r_area = random.randint(1,10)
    r_area_x = random.randint(1,21)
    ### scratch
    sc_r_0_20_h_area = random.randint(5,21)

    if r_area < 1:
        for i in range(20,WH-20):
            for j in range(20,WH-20):
                r_area_x = random.randint(1,20)
                r_area_y = random.randint(1,20)
                if (i % r_area_x) < 10 and (j % r_area_y) < 12:
                    # img[i,j] = (255, 255, 255)


                    if i%sc_r_0_20_h_area < 1:
                        tmp0 = img[i,j,0]
                        tmp1 = img[i,j,1]
                        tmp2 = img[i,j,2]

                        img[i,j] = img[i+sc_r_0_20_h_area,j]
                        img[i+sc_r_0_20_h_area,j] = (tmp0, tmp1, tmp2)


###########



    r_blur = random.randint(1,13)

    if r_blur < 4:
        ### Blur
        for i in range(0,WH):
            for j in range(0,WH):
                if j%2 == 0:
                    tmp0 = img[i,j,0]
                    tmp1 = img[i,j,1]
                    tmp2 = img[i,j,2]
                    img[i,j] = img[i,j+1]
                    img[i,j+1] = (tmp0, tmp1, tmp2)


###########



    ### Draw Line
    r_draw_line = random.randint(1,11)
    r_0_20_h = random.randint(1,21)
    r_0_20_v = random.randint(1,21)
    r_10_10_0 = random.randint(-10,10)
    r_10_10_1 = random.randint(-10,10)
    r_10_10_2 = random.randint(-10,10)


    if r_draw_line < 4:
        for i in range(0, WH):
            for j in range(0, WH):

                ### Draw vertical line (|)
                if j%r_0_20_v < 2:
                    if img[i, j, 0] < 180:
                        img[i,j,0] = img[i,j,0] + r_10_10_0 + 10
                        img[i,j,1] = img[i,j,1] + r_10_10_1 + 10
                        img[i,j,2] = img[i,j,2] + r_10_10_2 + 10


    elif r_draw_line == 11:
        for i in range(0, WH):
            for j in range(0, WH):


                ### Draw vertical line (|)
                if j%r_0_20_v < 2:
                    if img[i, j, 0] < 180:
                        img[i,j,0] = img[i,j,0] + r_10_10_0 + 10
                        img[i,j,1] = img[i,j,1] + r_10_10_1 + 10
                        img[i,j,2] = img[i,j,2] + r_10_10_2 + 10

###########




    ### Edit Color Channel
    r_color = random.randint(1, 9)

    MIN = 51
    MAX = 179
    r_MM0 = random.randint(MIN, MAX)
    r_MM1 = random.randint(MIN, MAX)
    r_MM2 = random.randint(MIN, MAX)
    r0 = random.randint(MIN, MAX)
    r1 = random.randint(MIN, MAX)
    r2 = random.randint(MIN, MAX)
    r2 = random.randint(MIN, MAX)

    if r_color < 3:
        for i in range(0, WH):
            for j in range(0, WH):

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


    elif r_color < 5:
        for i in range(0, WH):
            for j in range(0, WH):

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


    elif r_color < 7:
        for i in range(0, WH):
            for j in range(0, WH):

                ### Edit Blue Channel
                if img[i, j, 0] > r_MM0: # Blue
                    ran_b = random.randint(r0, 180)
                    img[i,j,0] = (img[i,j,0] + ran_b)/2
                else:
                    ran_b = random.randint(50, r0)
                    img[i,j,0] =  (img[i,j,0] + ran_b)/2


                ### Edit Red Channel
                if img[i, j ,2] > r_MM2: # red
                    ran_r = random.randint(r2, 180)
                    img[i,j,2] = (img[i,j,1] + ran_r)/2
                else:
                    ran_r = random.randint(50, r2)
                    img[i,j,2] = img[i,j,2] = (img[i,j,1] + ran_r)/2


    elif r_color == 7:
        for i in range(0, WH):
            for j in range(0, WH):

                ### Edit Red Channel
                if img[i, j ,2] > r_MM2: # red
                    ran_r = random.randint(r2, 180)
                    img[i,j,2] = (img[i,j,1] + ran_r)/2
                else:
                    ran_r = random.randint(50, r2)
                    img[i,j,2] = img[i,j,2] = (img[i,j,1] + ran_r)/2


    elif r_color == 8:
        for i in range(0, WH):
            for j in range(0, WH):

                ### Edit Green Channel
                if img[i, j, 1] > r_MM1: # Green
                    ran_g = random.randint(r1, 180)
                    img[i,j,1] = (img[i,j,1] + ran_g)/2
                else:
                    ran_g = random.randint(50, r1)
                    img[i,j,1] = (img[i,j,1] + ran_g)/2


    elif r_color == 9:
        for i in range(0, WH):
            for j in range(0, WH):

                ### Edit Blue Channel
                if img[i, j, 0] > r_MM0: # Blue
                    ran_b = random.randint(r0, 180)
                    img[i,j,0] = (img[i,j,0] + ran_b)/2
                else:
                    ran_b = random.randint(50, r0)
                    img[i,j,0] =  (img[i,j,0] + ran_b)/2




###########


    ### scratch
    sc_r_0_20_h = random.randint(2,20)
    sc_r_0_20_v = random.randint(3,20)

    r_scscratch = random.randint(1, 9)


    if r_scscratch < 3:

        ### scratch vertical (|)
        for i in range(0, WH-21):
            for j in range(0, WH-21):
                if j%sc_r_0_20_v < 1:
                    tmp0 = img[i,j,0]
                    tmp1 = img[i,j,1]
                    tmp2 = img[i,j,2]
                    img[i,j] = img[i,sc_r_0_20_v]
                    img[i,sc_r_0_20_v] = (tmp0, tmp1, tmp2)



###########




    ### Overflow Blue
    for i in range(0, WH):
        for j in range(0, WH):
            if img[i,j,0] > 225 and img[i,j,1] < 50 and img[i,j,2] < 50:
                img[i,j,0] = 255
                img[i,j,1] = 0
                img[i,j,2] = 0

    ## Overflow Green
    for i in range(0, WH):
        for j in range(0, WH):
            if img[i,j,1] > 220 and img[i,j,0] < 50 and img[i,j,2] < 50:
                img[i,j,0] = 0
                img[i,j,1] = 255
                img[i,j,2] = 0

    ## Overflow Green
    for i in range(0, WH):
        for j in range(0, WH):
            if img[i,j,2] > 220 and img[i,j,0] < 50 and img[i,j,1] < 50:
                img[i,j,0] = 0
                img[i,j,1] = 0
                img[i,j,2] = 255




###########


    r_replace = random.randint(1, 10)

    if r_replace < 3:
        for i in range(0,WH):
            for j in range(0,WH):
                r_replace_x = random.randint(5,21)
                r_replace_y = random.randint(5,21)
                if (i % r_replace_x) < 2 and (j % r_replace_y) < 2:
                    if (random.randint(1,5)) < 2:
                        tmp0 = img[i,j,0]
                        tmp1 = img[i,j,1]
                        tmp2 = img[i,j,2]

                        img[i,j,0] = img[j,i,0]
                        img[i,j,1] = img[j,i,1]
                        img[i,j,2] = img[j,i,2]

                        img[j,i,0] = tmp0
                        img[j,i,1] = tmp1
                        img[j,i,2] = tmp2


###########


    ### ex Edit Color Channel
    ex_r_color = random.randint(1, 20)

    MIN = 51
    MAX = 179
    r_MM0 = random.randint(MIN, MAX)
    r_MM1 = random.randint(MIN, MAX)
    r_MM2 = random.randint(MIN, MAX)
    r0 = random.randint(MIN, MAX)
    r1 = random.randint(MIN, MAX)
    r2 = random.randint(MIN, MAX)
    r2 = random.randint(MIN, MAX)

    if ex_r_color < 3:
        for i in range(0, WH):
            for j in range(0, WH):

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


    elif ex_r_color < 5:
        for i in range(0, WH):
            for j in range(0, WH):

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


    elif ex_r_color < 7:
        for i in range(0, WH):
            for j in range(0, WH):

                ### Edit Blue Channel
                if img[i, j, 0] > r_MM0: # Blue
                    ran_b = random.randint(r0, 180)
                    img[i,j,0] = (img[i,j,0] + ran_b)/2
                else:
                    ran_b = random.randint(50, r0)
                    img[i,j,0] =  (img[i,j,0] + ran_b)/2


                ### Edit Red Channel
                if img[i, j ,2] > r_MM2: # red
                    ran_r = random.randint(r2, 180)
                    img[i,j,2] = (img[i,j,1] + ran_r)/2
                else:
                    ran_r = random.randint(50, r2)
                    img[i,j,2] = img[i,j,2] = (img[i,j,1] + ran_r)/2


    elif ex_r_color == 7:
        for i in range(0, WH):
            for j in range(0, WH):

                ### Edit Red Channel
                if img[i, j ,2] > r_MM2: # red
                    ran_r = random.randint(r2, 180)
                    img[i,j,2] = (img[i,j,1] + ran_r)/2
                else:
                    ran_r = random.randint(50, r2)
                    img[i,j,2] = img[i,j,2] = (img[i,j,1] + ran_r)/2


    elif ex_r_color == 8:
        for i in range(0, WH):
            for j in range(0, WH):

                ### Edit Green Channel
                if img[i, j, 1] > r_MM1: # Green
                    ran_g = random.randint(r1, 180)
                    img[i,j,1] = (img[i,j,1] + ran_g)/2
                else:
                    ran_g = random.randint(50, r1)
                    img[i,j,1] = (img[i,j,1] + ran_g)/2


    elif ex_r_color == 9:
        for i in range(0, WH):
            for j in range(0, WH):

                ### Edit Blue Channel
                if img[i, j, 0] > r_MM0: # Blue
                    ran_b = random.randint(r0, 180)
                    img[i,j,0] = (img[i,j,0] + ran_b)/2
                else:
                    ran_b = random.randint(50, r0)
                    img[i,j,0] =  (img[i,j,0] + ran_b)/2





###########

    ### ex_scratch
    sc_r_0_20_h = random.randint(3,20)
    sc_r_0_20_v = random.randint(2,20)

    r_scscratch = random.randint(1, 13)


    if r_scscratch < 3:
        ### scratch vertical (|)
        for i in range(0, WH-21):
            for j in range(0, WH-21):
                if j%sc_r_0_20_v < 1:
                    tmp0 = img[i,j,0]
                    tmp1 = img[i,j,1]
                    tmp2 = img[i,j,2]
                    img[i,j] = img[i,sc_r_0_20_v]
                    img[i,sc_r_0_20_v] = (tmp0, tmp1, tmp2)



###########



    ex_r_blur = random.randint(1,12)

    if r_blur < 3:
        ### Blur
        for i in range(0,WH):
            for j in range(0,WH):
                if j%2 == 0:
                    tmp0 = img[i,j,0]
                    tmp1 = img[i,j,1]
                    tmp2 = img[i,j,2]
                    img[i,j] = img[i,j+1]
                    img[i,j+1] = (tmp0, tmp1, tmp2)




################################################################################


    ###### ex1
    ex_effects = random.randint(1,4)


    if ex_effects == 1:
        r_area = random.randint(1,10)
        r_area_x = random.randint(1,21)
        ### scratch
        sc_r_0_20_h_area = random.randint(5,21)

        if r_area < 1:
            for i in range(20,WH-20):
                for j in range(20,WH-20):
                    r_area_x = random.randint(1,20)
                    r_area_y = random.randint(1,20)
                    if (i % r_area_x) < 10 and (j % r_area_y) < 12:
                        # img[i,j] = (255, 255, 255)


                        if i%sc_r_0_20_h_area < 1:
                            tmp0 = img[i,j,0]
                            tmp1 = img[i,j,1]
                            tmp2 = img[i,j,2]

                            img[i,j] = img[i+sc_r_0_20_h_area,j]
                            img[i+sc_r_0_20_h_area,j] = (tmp0, tmp1, tmp2)






    ###########


        ### scratch
        sc_r_0_20_h = random.randint(3,20)
        sc_r_0_20_v = random.randint(2,15)

        r_scscratch = random.randint(1, 8)


        if r_scscratch < 3:
            ### scratch vertical (|)
            for i in range(0, WH-21):
                for j in range(0, WH-16):
                    if j%sc_r_0_20_v < 1:
                        tmp0 = img[i,j,0]
                        tmp1 = img[i,j,1]
                        tmp2 = img[i,j,2]
                        img[i,j] = img[i,sc_r_0_20_v]
                        img[i,sc_r_0_20_v] = (tmp0, tmp1, tmp2)



    ###########


        ### ex Edit Color Channel
        ex_r_color = random.randint(1, 30)

        MIN = 51
        MAX = 179
        r_MM0 = random.randint(MIN, MAX)
        r_MM1 = random.randint(MIN, MAX)
        r_MM2 = random.randint(MIN, MAX)
        r0 = random.randint(MIN, MAX)
        r1 = random.randint(MIN, MAX)
        r2 = random.randint(MIN, MAX)
        r2 = random.randint(MIN, MAX)

        if ex_r_color < 3:
            for i in range(0, WH):
                for j in range(0, WH):

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


        elif ex_r_color < 5:
            for i in range(0, WH):
                for j in range(0, WH):

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


        elif ex_r_color < 7:
            for i in range(0, WH):
                for j in range(0, WH):

                    ### Edit Blue Channel
                    if img[i, j, 0] > r_MM0: # Blue
                        ran_b = random.randint(r0, 180)
                        img[i,j,0] = (img[i,j,0] + ran_b)/2
                    else:
                        ran_b = random.randint(50, r0)
                        img[i,j,0] =  (img[i,j,0] + ran_b)/2


                    ### Edit Red Channel
                    if img[i, j ,2] > r_MM2: # red
                        ran_r = random.randint(r2, 180)
                        img[i,j,2] = (img[i,j,1] + ran_r)/2
                    else:
                        ran_r = random.randint(50, r2)
                        img[i,j,2] = img[i,j,2] = (img[i,j,1] + ran_r)/2




    ###########

        ### ex_scratch
        sc_r_0_20_h = random.randint(2,21)
        sc_r_0_20_v = random.randint(3,21)

        r_scscratch = random.randint(1, 13)


        if r_scscratch < 3:
            ### scratch vertical (|)
            for i in range(0, WH-20):
                for j in range(0, WH-20):
                    if j%sc_r_0_20_v < 1:
                        tmp0 = img[i,j,0]
                        tmp1 = img[i,j,1]
                        tmp2 = img[i,j,2]
                        img[i,j] = img[i,sc_r_0_20_v]
                        img[i,sc_r_0_20_v] = (tmp0, tmp1, tmp2)







################################################################################



    elif ex_effects == 2:




    ###########


        ### scratch
        sc_r_0_20_h = random.randint(2,21)
        sc_r_0_20_v = random.randint(3,21)

        r_scscratch = random.randint(1, 9)


        if r_scscratch < 3:
            ### scratch vertical (|)
            for i in range(0, WH-20):
                for j in range(0, WH-20):
                    if j%sc_r_0_20_v < 1:
                        tmp0 = img[i,j,0]
                        tmp1 = img[i,j,1]
                        tmp2 = img[i,j,2]
                        img[i,j] = img[i,sc_r_0_20_v]
                        img[i,sc_r_0_20_v] = (tmp0, tmp1, tmp2)



    ###########


        ### ex Edit Color Channel
        ex_r_color = random.randint(1, 20)

        MIN = 51
        MAX = 179
        r_MM0 = random.randint(MIN, MAX)
        r_MM1 = random.randint(MIN, MAX)
        r_MM2 = random.randint(MIN, MAX)
        r0 = random.randint(MIN, MAX)
        r1 = random.randint(MIN, MAX)
        r2 = random.randint(MIN, MAX)
        r2 = random.randint(MIN, MAX)

        if ex_r_color < 3:
            for i in range(0, WH):
                for j in range(0, WH):

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








    ###########

        ### ex_scratch
        sc_r_0_20_h = random.randint(2,21)
        sc_r_0_20_v = random.randint(3,21)

        r_scscratch = random.randint(1, 13)


        if r_scscratch < 3:
            ### scratch vertical (|)
            for i in range(0, WH-20):
                for j in range(0, WH-20):
                    if j%sc_r_0_20_v < 1:
                        tmp0 = img[i,j,0]
                        tmp1 = img[i,j,1]
                        tmp2 = img[i,j,2]
                        img[i,j] = img[i,sc_r_0_20_v]
                        img[i,sc_r_0_20_v] = (tmp0, tmp1, tmp2)



    ###########



        ex_r_blur = random.randint(1,12)

        if r_blur < 3:
            ### Blur
            for i in range(0,WH):
                for j in range(0,WH):
                    if j%2 == 0:
                        tmp0 = img[i,j,0]
                        tmp1 = img[i,j,1]
                        tmp2 = img[i,j,2]
                        img[i,j] = img[i,j+1]
                        img[i,j+1] = (tmp0, tmp1, tmp2)







################################################################################





    print(datetime.now().strftime("%H:%M:%S"))
    cv2.imshow("preview",img)


    ### save img
    # cv2.imwrite(out_path_debug, img);
    cv2.imwrite(out_path, img);




    cv2.destroyAllWindows()
    print("Glitched :", num)

    time2 = cv2.getTickCount()
    time = (time2 - time1)/cv2.getTickFrequency() # クロック時間の差を周波数で割ると秒
    print(time, "sec")


print("Finished!!")
