import cv2

imagePath = "frame301.jpg"
cascPath = "haarcascade_frontalface_default.xml"
path = "/home/shubhi/new/croppedimages/"
print "1"
faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('img', gray)
cv2.waitKey()

'''minisize = (image.shape[1],image.shape[0])
miniframe = cv2.resize(image, minisize)'''

faces = faceCascade.detectMultiScale(
	gray,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30, 30),
	flags = cv2.CASCADE_SCALE_IMAGE
)

#faces=  faceCascade.detectMultiScale(gray,1.1,5)

print faces

for (x, y, w, h) in faces:
	print "2"
	cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)


sub_face = image[y:y+h, x:x+w]

cv2.imwrite("{2}cropped_1_{0}_{1}".format(str(x), str(imagePath), str(path)), sub_face)	
cv2.imshow('imag', sub_face)
cv2.waitKey()

print "3"

