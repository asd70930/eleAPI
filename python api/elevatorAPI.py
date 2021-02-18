import cv2
import numpy as np

class ele:
    first = True
    initial = None
    init_isnone = True

    def __init__(self, ip):
        _, self.initial = self.getframe(ip)
        self.first = False
        if self.init_isnone:
            print('initial frame is null, please reinitial again ')
        else:
            print('initial frame is Done')

    def get_initial_status(self):
        return self.init_isnone

    def reinitial(self, ip):
        ret, frame = self.getframe(ip)
        if ret == False :
            self.initial = None
            self.init_isnone = True
            pass
        else:
            self.initial = frame
            self.init_isnone = False

    def getframe(self, ip):
        cap = cv2.VideoCapture(ip)
        ret, frame = cap.read()
        if self.first:
            if ret:
                self.init_isnone = False
            return ret, frame
        else:
            return ret, frame

    # compare the frame with initial frame ,
    # if elevator is empty output = 0 ,
    # if elevator is not empty output = 1 ,
    # if can't found ipcamera output = 4
    def compare(self, ip):
        ret, frame = self.getframe(ip)
        if ret == False:
            return 4
        else:
            sub = np.uint8(np.abs(np.int32(self.initial) - np.int32(frame)))
            gray = cv2.cvtColor(sub, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (11, 11), 0)
            binaryIMG = cv2.Canny(blurred, 20, 160)
            binaryIMG = cv2.dilate(binaryIMG, None, iterations=36)
            binaryIMG = cv2.erode(binaryIMG, None, iterations=36)
            binaryIMG = cv2.dilate(binaryIMG, None, iterations=12)
            cnts, _ = cv2.findContours(binaryIMG.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            count = 0
            for c in cnts:
                if cv2.contourArea(c) > 500:
                    count += 1
            # print('has something', count != 0)
            if count == 0:
                return 0
            elif count > 0:
                return 1
