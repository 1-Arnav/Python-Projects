import cv2
import glob
import os

#makes a list of all image names
image = glob.glob("images/*.jpg")

#iterates thro the list

for img in image:
    img1 = cv2.imread(img,0)
    re = cv2.resize(img1, (100,100))
    cv2.imshow("Hey", re)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    
    cv2.imwrite("resizer_"+img , re)
    
    #path = 'D:/......'
    #cv2.imwrite(os.path.join(path , "resized_"+img1), re)