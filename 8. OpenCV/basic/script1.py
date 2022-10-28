import cv2

# 1 = color ;   0 = greyscale ;   -1 = alpha arguement involved
img= cv2.imread("basic/galaxy.jpg",1)

# print(type(img))
# print(img)
# print(img.shape)  # gives size
# print(img.ndim)  #gives dimmensions

resized_img1 = cv2.resize(img, (1000,500))
resized_img = cv2.resize(img, ( int(img.shape[1]/2) , int(img.shape[0]/2)) ) 

cv2.imshow("Galaxy", resized_img1)
cv2.imwrite("basic/Galavy_resized.jpg", resized_img1)
cv2.waitKey(2000)
cv2.destroyAllWindows()