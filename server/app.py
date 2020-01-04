from flask import Flask, render_template, Response
from modules.Detector import Detector
import socket, sys, signal

# FLASK CONFIG
app = Flask(__name__)
app.static_folder = 'static'
app.config['TEMPLATES_AUTO_RELOAD'] = True

# SOCKET CONFIG
ip = "0.0.0.0"
port = 5005
server_adress = (ip, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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

# SIGNAL HANDLING
def receive_signal(signal_number, frame):
    global detector, sock, app
    del detector
    print("\nDetector released.")
    sock.close()
    print("Socket closed.")
    del app
    print("Application exited.")
    sys.exit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(rec(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    signal.signal(signal.SIGINT, receive_signal)
    signal.signal(signal.SIGQUIT, receive_signal)
    signal.signal(signal.SIGTSTP, receive_signal)
    app.run(debug=True) #ssl_context='adhoc'
