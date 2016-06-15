import cv2
from os import listdir
from os.path import isfile, join
import os

vidcap=cv2.VideoCapture('2.mp4')
success, image = vidcap.read()
count=0
count1=0
crop = []
while success:
		success, image = vidcap.read()
		count += 1
		face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
		eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
		if image==None:
			print image
		else:
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			faces = face_cascade.detectMultiScale(
				gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30),
				flags = cv2.CASCADE_SCALE_IMAGE
			)
			count1 += 1

			for (x,y,w,h) in faces:
				cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
				roi_gray = gray[y:y+h, x:x+w]
				roi_color = image[y:y+h, x:x+w]
				eyes = eye_cascade.detectMultiScale(roi_gray)
				for (ex,ey,ew,eh) in eyes:
					cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
			sub_face = image[y:y+h, x:x+w]
			crop.append(sub_face)
			if cv2.waitKey(10) == 27:
				break
print "no. of frames", count
print "no. of crops", count1 
