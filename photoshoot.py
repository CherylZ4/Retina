import cv2
import datetime

""" def takePhoto():
    cap = cv2.VideoCapture(0)
    while(True):
        if cv2.waitKey(1) & 0xFF == ord('space'):
            cv2.imwrite('capture.jpg', frame)
            print('Photo Taken')
            break """
    

def openCam():
    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%y-%m-%d-%H:%M:%S")
    cam = cv2.VideoCapture(0)

    while(True):
        ret, frame = cam.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        cv2.imshow('frame', rgb)
        #print(cv2.waitKey(1))
        if cv2.waitKey(1) & 0xFF == 0x20:
            cv2.imwrite(f'{current_time}.jpg', frame)
            break
    cam.release()
    return current_time