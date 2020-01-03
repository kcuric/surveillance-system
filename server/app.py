from flask import Flask, render_template, Response

app = Flask(__name__)

import socket


ip = "0.0.0.0"
port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

def rec():
    
    while True:
        data, addr = sock.recvfrom(65535)
        print(len(data))
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + data + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(rec(), mimetype='multipart/x--mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
