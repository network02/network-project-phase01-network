import socket

def main():
    host = input("Enter host: ")
    min_port = int(input("Enter start range: "))
    max_port = int(input("Enter end range: "))

    for port in range(min_port,max_port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host,port))
            print(f"Port {port} is open.")

        except Exception as error:
            print(f"Port {port} is close.")
        
        finally:
            s.close()


if __name__ == '__main__':
    main()