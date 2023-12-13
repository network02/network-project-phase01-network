import socket

SERVER_HOST = "localhost"
SERVER_PORT = 8081

def main():
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((SERVER_HOST, SERVER_PORT))
    cs.send(b"GET user2")

    res = cs.recv(1024).decode()

    print(res)

    cs.close()
    


if __name__ == '__main__':
    main()