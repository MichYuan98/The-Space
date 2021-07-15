import cv2
from .models import Room

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


class VideoCamera(object):
	def __init__(self, ip_address, room_id):
		self.video = cv2.VideoCapture(ip_address)
		self.id = room_id

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		resize = cv2.resize(image, (960, 540), interpolation=cv2.INTER_LINEAR)
		ret, jpeg = cv2.imencode('.jpg', resize)

		new_image = image[50:480, 0:640]
		num_people = self.detect(new_image)
		Room.objects.filter(pk=self.id).update(current_count=str(num_people))
		# print("camera running")
		return jpeg.tobytes()

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
		print(person - 1)
		return person - 1


