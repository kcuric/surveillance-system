import socket

class Streamer(object):
    '''
    Sets the socket and the server address and get the camera from the Recorder class.2

    Arguments:
    host(str) IP address of a server to stream to
    port(str) port of a server to stream to
    '''
    def __init__(self, host, port, recorder):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (host, port)
        self.camera = recorder

    '''
    Gets a frame from camera and sends it to the server via UDP.
    '''
    def send_to_server(self):
        while True:
            frame = self.camera.get_frame()
            length = len(frame)
            if(length < 65536):
                self.sock.sendto(frame, self.server_address)
                print("sent to server")
