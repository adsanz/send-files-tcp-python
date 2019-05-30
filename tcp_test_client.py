import socket

def send_file(filename):
    s.send(bytes(filename,"utf8"))
    file = open(filename, 'rb')
    while True:
        data = file.read(BUFFSIZE)
        s.send(data)
        if not data:
            s.close()
            file.close()
            print("Done sending!")
            break

if __name__ == "__main__":
    HOST = "127.0.0.1"        # The remote host
    PORT = 42050              # The same port as used by the server
    BUFFSIZE = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    filename = input("Choose the file to be sent: ")
    send_file(filename)
