import cv2
import numpy as np

def detect_faces(image: np.ndarray) -> list:
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # 转换为 face_recognition 格式 (top, right, bottom, left)
    return [(y, x+w, y+h, x) for (x,y,w,h) in faces]