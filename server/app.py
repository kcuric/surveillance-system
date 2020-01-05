from flask import Flask, render_template, Response, jsonify
from modules.Detector import Detector
from modules.EmailSender import EmailSender
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
face_detected = dict()

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

def rec(sock, camera_num):
    global face_detected
    email_sent = False
    while True:
        data, addr = sock.recvfrom(65535)
        if(detector.find_faces(data)):
            face_detected[camera_num] = True
            if(email_sent == False):
                sender = EmailSender(camera_num, data)
                sender.send_email('kristoficmiro0@gmail.com')
                email_sent = True
        else:
            face_detected[camera_num] = False
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + data + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/camera1')
def camera1():
    return Response(
        rec(sockets[0], 1), 
        mimetype='multipart/x-mixed-replace; boundary=frame', 
    )

@app.route('/camera2')
def camera2():
    return Response(
        rec(sockets[1], 2), 
        mimetype='multipart/x-mixed-replace; boundary=frame',
    )

@app.route('/face_detected')
def check_for_faces():
    return jsonify(face_detected)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, receive_signal)
    signal.signal(signal.SIGQUIT, receive_signal)
    signal.signal(signal.SIGTSTP, receive_signal)
    app.run(debug=True) #ssl_context='adhoc'
