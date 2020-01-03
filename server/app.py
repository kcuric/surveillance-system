from flask import Flask, render_template, Response
from modules.Detector import Detector
import socket

# FLASK CONFIG
app = Flask(__name__)
app.static_folder = 'static'
app.config['TEMPLATES_AUTO_RELOAD'] = True

# SOCKET CONFIG
ip = "0.0.0.0"
port = 5005
server_adress = (ip, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_adress)

# DETECTOR CONFIG
detector = Detector()

def rec():
    while True:
        data, addr = sock.recvfrom(65535)
        if(detector.find_faces(data)):
            print("INTRUDER!")
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + data + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(rec(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True) #ssl_context='adhoc'
