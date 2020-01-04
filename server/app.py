from flask import Flask, render_template, Response
from modules.Detector import Detector
import socket, sys, signal

# FLASK CONFIG
app = Flask(__name__)
app.static_folder = 'static'
app.config['TEMPLATES_AUTO_RELOAD'] = True

# SOCKET CONFIG
ip = "0.0.0.0"
ports = [5005, 5006]
sockets = list()

for port in ports:
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    new_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_socket.bind((ip, port))
    sockets.append(new_socket)

# DETECTOR CONFIG
detector = Detector()

# SIGNAL HANDLING
def receive_signal(signal_number, frame):
    global detector, sock, app
    del detector
    print("\nDetector released.")
    for socket in sockets:
        del socket
    print("Socket closed.")
    del app
    print("Application exited.")
    sys.exit()

def rec(sock):
    while True:
        data, addr = sock.recvfrom(65535)
        if(detector.find_faces(data)):
            print("INTRUDER!")
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + data + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/camera1')
def camera1():
    return Response(rec(sockets[0]), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camera2')
def camera2():
    return Response(rec(sockets[1]), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    signal.signal(signal.SIGINT, receive_signal)
    signal.signal(signal.SIGQUIT, receive_signal)
    signal.signal(signal.SIGTSTP, receive_signal)
    app.run(debug=True) #ssl_context='adhoc'
