import numpy as np
import requests as req
import cv2

capture=cv2.VideoCapture(0)
while(capture.isOpened()):
    ret,frame=capture.read()
    cv2.imshow("webcam",frame)
    if(cv2.waitKey(1)==ord("s")):
        break
    qrDetector=cv2.QRCodeDetector()
    data,bbox,rectifiedImage=qrDetector.detectAndDecode(frame)
    if(len(data)>0):
        print(data)
        res=req.post("https://esp32-rfid-api.vercel.app/web/llavero", data)
        if res.status_code==200:
            print(res.content)
            break
        else:
            print(res.status_code)
