from ultralytics import YOLO
import cv2

#load model
LP_detector = YOLO('/home/phong/PycharmProjects/LPRecog/TrainingStage/train22/weights/best.pt')
Vehicles_detector = YOLO('yolov8n.pt')

#load video
cam = cv2.VideoCapture(0)

#read frames
ret = True
while ret:
    ret, frame = cam.read()
    if ret:
        pass
        #detect vehicles
        detectV = Vehicles_detector(frame)[0]

