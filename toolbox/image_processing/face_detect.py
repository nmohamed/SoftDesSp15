""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

kernel = np.ones((21,21),'uint8')
face_cascade = cv2.CascadeClassifier('/home/nora/SoftDesSp15/toolbox/image_processing/haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)

while(True):

	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	for (x,y,w,h) in faces:
		frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
		# cv2.rectangle(frame,(x,y),(x+w,y+h),(0,(int(x+.4*w), int(y+.8*h))0,255))
		cv2.circle(frame, (int(x+.3*w), int(y+.3*h)), 20, (255, 255, 255), 15)
		cv2.circle(frame, (int(x+.3*w), int(y+.3*h)), 3, (0, 0, 0), 15 )
		cv2.circle(frame, (int(x+.7*w), int(y+.3*h)), 20, (255, 255, 255), 15 )
		cv2.circle(frame, (int(x+.7*w), int(y+.3*h)), 3, (0, 0, 0), 15 )
		# cv2.ellipse(frame, (int(x+.5*w), int(y+.7*h)), (0, 0, 255), 15)
		cv2.circle(frame, (int(x+.5*w), int(y+.8*h)), 3, (0, 0, 255), 40 )
		cv2.line(frame, (int(x+.4*w), int(y+.8*h)), 
						(int(x+.6*w), int(y+.8*h)),
						(0,0,0), 5)

	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()