import socket


def handle_connection(conn):
    filename = conn.recv(BUFFSIZE).decode("utf8")
    file = open("sent_"+filename, "ab")
    while True:
        data = conn.recv(BUFFSIZE)
        file.write(data)
        if not data:
            print("Done, file saved as {}".format("sent_"+filename) )
            break


if __name__ == "__main__":
    HOST = "127.0.0.1"        # server ip
    PORT = 42050              # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    BUFFSIZE = 1024
    s.listen(5)
    conn, addr = s.accept()
    print("Connected")
    handle_connection(conn)
