import cv2

class Recorder(object):
    def __init__(self, camera_num):
        '''
        Uses opencv to capture from camera with id 'camera_num'.

        Arguments:
        camera_num(int) id of the camera you want to capture with
        '''
        self.video = cv2.VideoCapture(camera_num)
        self.video.set(3, 480)
        self.video.set(4, 360)

    def __del__(self):
        '''
        Finalizer which is called after all the references to the object
        have been deleted.
        '''
        self.video.release()

    def get_frame(self) -> str:
        '''
        Changes the default opencv raw image capturing to jpeg encoding.

        Returns:
        jpeg_encoded_string(str) jpeg encoded image converted to string
        '''
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        jpeg_encoded_image = jpeg.tostring()
        return jpeg_encoded_image

