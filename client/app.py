from modules.Streamer import Streamer
from modules.Recorder import Recorder

def main():
    recorder = Recorder(0)
    stream = Streamer('127.0.0.1', 5005, recorder) #35.204.145.0
    stream.send_to_server()

if __name__ == "__main__":
    main()
