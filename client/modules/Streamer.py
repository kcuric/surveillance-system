import socket

class Streamer(object):
    '''
    Sets the socket and the server address and get the camera from the Recorder class.2

    Arguments:
    host(str) IP address of a server to stream to
    port(str) port of a server to stream to
    '''
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = (host, port)

    '''
    Finalizer which is called after all the references to the object
    have been deleted.
    '''
    def __del__(self):
        self.sock.close()

    '''
    Gets a frame from camera and sends it to the server via UDP.
    '''
    def send_to_server(self, payload):
        length = len(payload)
        if(length < 65536):
            self.sock.sendto(payload, self.server_address)
            print("Sent to server! Payload size: {}".format(len(payload)))
