import socket

SERVER_HOST = "localhost"
SERVER_PORT = 8081

def main():
    # We set socket type to socket.SOCK_STREAM which means that it will use TCP
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((SERVER_HOST, SERVER_PORT))

    while True:
        in_str = input("Please input your command or EXIT to exit: ")

        cs.send(bytes(in_str, encoding='utf-8'))
        res = cs.recv(1024).decode()
        print("Response received:")
        print(res)

        if in_str == "EXIT":
            break

        
    cs.close()
    

if __name__ == '__main__':
    main()