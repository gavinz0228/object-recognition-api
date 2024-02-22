import cv2
import cvlib as cv
from cvlib.object_detection import YOLO

MODEL_NAME = "yolov3"
CONFIDENCE = 0.6

YOLOV3_WEIGHTS = "./yolov3/yolov3.weights"
YOLOV3_CONFIG = "./yolov3/yolov3.cfg"
YOLOV3_CLASS = "./yolov3/yolov3_classes.txt"

yolo = YOLO(YOLOV3_WEIGHTS, YOLOV3_CONFIG, YOLOV3_CLASS)

def detect_objects(file_path):
    image = cv2.imread(file_path)
    return yolo.detect_objects(image, confidence=CONFIDENCE)

def detect_faces(file_path):
    image = cv2.imread(file_path)
    return cv.detect_face(image, enable_gpu=True)
    