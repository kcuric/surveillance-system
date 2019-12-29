import cv2

class Detector(): 
	
	def _find_faces(self, image: object) -> int:
		"""
		Uses OpenCV to recognize faces in the taken picture.
		Arguments:
		object: Previously taken image (or any image).
		Returns:
		int: Number of recognized faces in the picture.
		
		casc_path = 'haarcascade_frontalface_default.xml'
		face_cascade = cv2.CascadeClassifier(casc_path)
		"""
		face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30),
			flags=cv2.CASCADE_SCALE_IMAGE
		)
		return len(faces)