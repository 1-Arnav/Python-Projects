"""
It kindof measure camera's frame rate
also can show images in different filters?!

Hit q TO EXIT THE PROGRAM

"""
import cv2, time

start_time = time.time()

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
sum=0
while True:
    sum=sum+1
    check, frame = video.read()

    print(check)
    print(frame)
    print(sum)

    #grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

tm = time.time() - start_time

print("\nRun time = ", tm)
print("\nFrame Rate = ", sum/tm , "  FPS")

video.release()
cv2.destroyAllWindows