import cv2
# import numpy as np
import random
from datetime import datetime











### Debug
### Sample
# for test in range(0, 5): ### debug
#     test_list = [1, 400, 600, 800, 1400]
#     x = test_list[test]


for x in range(1, 1551):


    print(x)

    time1 = cv2.getTickCount() # クロック時間


    num = "%05d" % x


    in_path = "src_edge_245_255/image-" + num + ".jpg"
    out_path = "src_edge_bitwise/image-" + num + ".jpg"
    # out_path = "test_Edge/image-" + num + "-" +datetime.now().strftime("%H-%M-%S")+".jpg"




################################################################################




    img_in = cv2.imread(in_path)

    img = cv2.bitwise_not(img_in)


################################################################################



    print(datetime.now().strftime("%H:%M:%S"))
    cv2.imshow("preview",img)


    ### save img
    # cv2.imwrite(out_path_debug, img);
    cv2.imwrite(out_path, img);




    cv2.destroyAllWindows()
    print("bitwise_not :", num)

    time2 = cv2.getTickCount()
    time = (time2 - time1)/cv2.getTickFrequency() # クロック時間の差を周波数で割ると秒
    print(time, "sec")


print("Finished!!")
