from modules.Streamer import Streamer
from modules.Recorder import Recorder
import sys, signal

recorder = Recorder(0)
stream = Streamer('127.0.0.1', 5005) #35.204.145.0

# SIGNAL HANDLING
def receive_signal(signal_number, frame):
    global stream, recorder
    del stream
    print("\nStreamer released.")
    del recorder
    print("Recorder released.")
    print("Application exited.")
    sys.exit()

def main():
    while True:
        frame = recorder.get_frame()
        stream.send_to_server(frame)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, receive_signal)
    signal.signal(signal.SIGQUIT, receive_signal)
    signal.signal(signal.SIGTSTP, receive_signal)
    main()
