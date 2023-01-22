import cv2
def openCam():
    cam = cv2.VideoCapture(0)

    while(True):
        ret, frame = cam.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        cv2.imshow('frame', rgb)
        #print(cv2.waitKey(1))
        if cv2.waitKey(1) & 0xFF == 0x20:
            cv2.imwrite('current.jpg', frame)
            break
    cam.release()
    cv2.destroyAllWindows()
    return 'current.jpg'