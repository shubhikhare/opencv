import cv2
from os import listdir
from os.path import isfile, join
import os

imagePath = os.popen("pwd").read().replace("\n", "")
cascPath = "haarcascade_frontalface_default.xml"
path = "/home/shubhi/new/croppedimages/"
imageList = listdir(imagePath)

for img in imageList:
	faceCascade = cv2.CascadeClassifier(cascPath)
	image = cv2.imread(imagePath + "/"+ str(img))

	if image==None:
		print image
	else:
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30),
			flags = cv2.CASCADE_SCALE_IMAGE
		)

		for (x, y, w, h) in faces:
			cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

		sub_face = image[y:y+h, x:x+w]
		cv2.imwrite("{2}cropped_1_{0}_{1}".format(str(x), str(img), str(path)), sub_face)	

print 'face cropping done..!!'
cv2.waitKey(0)