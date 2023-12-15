import socket

def is_port_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host,port))
        return True
    except:
        return False
    finally:
        s.close()

def check_port_range(host, s_port, e_port):
    for port in range(s_port, e_port):
        if is_port_open(host, port):
            print(f"Port {port} is open.")
            try:
                serviceName = socket.getservbyport(port, "tcp")
                print(f"TCP service: {serviceName}")
                serviceName = socket.getservbyport(port, "udp")
                print(serviceName)
                print(f"UDP service: {serviceName}")
            except Exception as error:
                print(f"service port:{error}")
        else:
            print(f"Port {port} is close.")


def main():
    host = input("Enter host: ")
    min_port = int(input("Enter start range: "))
    max_port = int(input("Enter end range: "))
    #check...
    check_port_range(host, min_port, max_port)
        
        
if __name__ == '__main__':
    main()