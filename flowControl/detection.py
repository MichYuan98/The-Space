# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
# from tensorflow.keras.preprocessing.image import img_to_array
# from tensorflow.keras.models import load_model
import cv2, os, urllib.request
import imutils
import numpy as np

# from django.conf import settings
from flowControl.models import Room

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


class HumanDetection(object):
    def __init__(self, room_object, room_id):
        self.room = room_object
        self.id = room_id
        self.video = cv2.VideoCapture(self.room.camera_ip_url)
        self.count = self.detect_by_frame()

    def __del__(self):
        self.video.release()

    def detect(self, frame):
        bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)

        person = 1
        for x, y, w, h in bounding_box_cordinates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            person += 1

        cv2.putText(frame, 'Status : Detecting ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
        cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
        # cv2.imshow('output', frame)
        # print(person)
        return person-1

    def detect_by_frame(self):
        num_people = 0
        check, frame = self.video.read()
        while check is True:
            check, frame = self.video.read()
            # cut water mark
            frame = frame[50:480, 0:640]
            # find count
            num_people = self.detect(frame)
            Room.objects.filter(pk=self.id).update(current_count=str(num_people))
            print("num of people: ", num_people)

            return num_people
