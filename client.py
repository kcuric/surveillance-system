from modules.Streamer import Streamer

def main():
    stream = Streamer('35.204.145.0', 5005, 0)
    stream.send_to_server()

if __name__ == "__main__":
    main()